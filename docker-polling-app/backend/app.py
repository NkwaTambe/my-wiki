import os
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import redis

app = Flask(__name__)
CORS(app)

# Establish a connection to Redis
r = redis.Redis(host=os.environ.get("REDIS_HOST"), port=6379, db=0, decode_responses=True)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
    )
    return conn

@app.route("/vote", methods=["POST"])
def vote():
    data = request.get_json()
    vote = data.get("vote")

    if vote not in ["option_a", "option_b"]:
        return jsonify({"status": "error", "message": "Invalid vote"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE votes SET vote_count = vote_count + 1 WHERE option = %s", (vote,))
    conn.commit()
    cur.close()
    conn.close()

    # After a successful vote, the cache is outdated. Delete it.
    r.delete("poll_results")

    return jsonify({"status": "success"})

@app.route("/results", methods=["GET"])
def results():
    # First, try to get the results from the Redis cache
    cached_results = r.get("poll_results")

    if cached_results:
        # If found (cache hit), return the cached data
        return jsonify(json.loads(cached_results))
    else:
        # If not in cache (cache miss), query the database
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT option, vote_count FROM votes")
        votes = cur.fetchall()
        cur.close()
        conn.close()

        results_dict = dict(votes)
        
        # Store the new results in Redis with a 10-second expiration
        r.set("poll_results", json.dumps(results_dict), ex=10)

        return jsonify(results_dict)

if __name__ == "__main__":
    # Create table on startup if it doesn't exist
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS votes (option TEXT PRIMARY KEY, vote_count INTEGER);")
    cur.execute("INSERT INTO votes (option, vote_count) VALUES ('option_a', 0) ON CONFLICT (option) DO NOTHING;")
    cur.execute("INSERT INTO votes (option, vote_count) VALUES ('option_b', 0) ON CONFLICT (option) DO NOTHING;")
    conn.commit()
    cur.close()
    conn.close()

    app.run(host="0.0.0.0", port=5000)
