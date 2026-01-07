# Start from a Python base image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
# We install build dependencies, run pip, then remove them in a single RUN command
# to keep the final image layer smaller.
COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
