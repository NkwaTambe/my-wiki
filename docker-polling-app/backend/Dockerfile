# Stage 1: The "builder" stage
# This stage installs all dependencies, including build-time requirements.
FROM python:3.9-alpine AS builder

# Install OS-level dependencies needed for building Python packages
RUN apk add --no-cache gcc python3-dev musl-dev postgresql-dev

# Set the working directory
WORKDIR /app

# Copy the requirements file and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: The "final" stage
# This stage creates the lean, final runtime image.
FROM python:3.9-alpine

# Install only the required runtime OS-level libraries
RUN apk add --no-cache postgresql-libs

# Set the working directory
WORKDIR /app

# Copy the installed Python packages from the "builder" stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app /app

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
