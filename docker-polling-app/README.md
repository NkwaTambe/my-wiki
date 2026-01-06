# Docker Polling App

This is a simple polling application built with Docker.

## How to Run

1.  **Start the application:**
    ```bash
    docker-compose up --build
    ```

2.  **Access the application:**
    Open your browser and go to `http://localhost`.

## Pushing Images to Docker Hub

1.  **Log in to Docker Hub:**
    ```bash
    docker login
    ```

2.  **Build the images:**
    ```bash
    docker-compose build
    ```

3.  **Tag the images:**
    ```bash
    docker tag docker-polling-app_backend <your-dockerhub-username>/polling-app-backend:latest
    docker tag docker-polling-app_frontend <your-dockerhub-username>/polling-app-frontend:latest
    ```

4.  **Push the images:**
    ```bash
    docker push <your-dockerhub-username>/polling-app-backend:latest
    docker push <your-dockerhub-username>/polling-app-frontend:latest
    ```
