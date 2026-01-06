# Docker Project Plan: Multi-Service Polling App

This document outlines a project that fulfills the requirements for both the Docker Compose assignment and the continuous assessment.

## 1. Project Overview

We will create a simple web-based polling application using three services orchestrated with Docker Compose:

*   **Frontend:** A static web page built with HTML, CSS, and JavaScript, served by an **Nginx** web server. Users can view poll questions and cast their votes.
*   **Backend API:** A RESTful API built with **Python (Flask)**. It will handle voting logic and communication with the database.
*   **Database:** A **PostgreSQL** database to store poll questions and vote counts.

This project demonstrates key Docker concepts:
*   Creating custom images using `Dockerfile`.
*   Orchestrating multiple containers with `docker-compose.yml`.
*   Networking between containers.
*   Managing persistent data using volumes.
*   Building and pushing images to Docker Hub.

## 2. Project Architecture

```
+-----------------+      +----------------------+      +------------------+
|   User Browser  | <--> |  Frontend (Nginx)    | <--> |  Backend (API)   |
|                 |      |  (Container)         |      |  (Container)     |
+-----------------+      +----------------------+      +------------------+
                                                         |
                                                         v
                                                     +------------------+
                                                     | Database (Postgres)|
                                                     | (Container)      |
                                                     +------------------+
```

## 3. Proposed File Structure

A good approach would be to create a new directory for this project, for example, `docker-polling-app`, and place all the files within it.

```
docker-polling-app/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## 4. Implementation Steps

### Step 1: Backend API (Flask)

*   **`backend/app.py`**: A simple Flask application with endpoints like `/vote` and `/results`.
*   **`backend/requirements.txt`**: Lists Python dependencies (e.g., `Flask`, `psycopg2-binary`).
*   **`backend/Dockerfile`**:
    *   Start from a `python:3.9-slim` base image.
    *   Copy `requirements.txt` and install dependencies.
    *   Copy the application code.
    *   Expose the port (e.g., 5000) and define the `CMD` to run the app.

### Step 2: Frontend (Nginx)

*   **`frontend/index.html`**: The main HTML file for the polling interface.
*   **`frontend/Dockerfile`**:
    *   Start from an `nginx:stable-alpine` base image.
    *   Copy the static files (`index.html`, etc.) into the Nginx public directory (`/usr/share/nginx/html`).
    *   Expose port 80.

### Step 3: Docker Compose

*   **`docker-compose.yml`**:
    *   Define three services: `frontend`, `backend`, `db`.
    *   For `frontend` and `backend`, specify the `build` context to their respective directories.
    *   For `db`, use the official `postgres:13` image.
    *   Set up a network for the services to communicate.
    *   Use a named volume for the PostgreSQL data to ensure persistence.
    *   Pass environment variables to the backend and database services (e.g., database credentials).

## 5. Fulfilling The Assignment

**Task: Use Docker Compose to orchestrate multiple services.**
*   The `docker-compose.yml` file will define and run the three services.

**Task: Each built from your own Dockerfiles.**
*   The `backend` and `frontend` services will have their own custom `Dockerfile`.

**Task: Push all custom images to Docker Hub.**
1.  Log in to Docker Hub: `docker login`
2.  Build the images using Docker Compose: `docker-compose build`
3.  Tag the custom images (Docker Compose may name them `docker-polling-app_backend` and `docker-polling-app_frontend`):
    *   `docker tag docker-polling-app_backend <your-dockerhub-username>/polling-app-backend:latest`
    *   `docker tag docker-polling-app_frontend <your-dockerhub-username>/polling-app-frontend:latest`
4.  Push the images:
    *   `docker push <your-dockerhub-username>/polling-app-backend:latest`
    *   `docker push <your-dockerhub-username>/polling-app-frontend:latest`

## 6. Preparing for the Assessment

This project has sufficient technical complexity and practical usefulness for the assessment. To prepare for the presentation, you should be ready to explain:

*   The role of each service and container.
*   The contents of each `Dockerfile` and why each instruction is used.
*   The structure of the `docker-compose.yml` file, including networking and volumes.
*   How the services communicate with each other.
*   How you would scale the application (e.g., adding more backend replicas).
