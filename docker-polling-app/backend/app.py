import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

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

    return jsonify({"status": "success"})

@app.route("/results", methods=["GET"])
def results():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT option, vote_count FROM votes")
    votes = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(dict(votes))

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
