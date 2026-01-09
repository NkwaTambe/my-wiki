# Stage 1: The "assets" stage
# For a simple static site, this stage just holds the source files.
# In a more complex project, this stage would build the assets (e.g., using Node.js).
FROM alpine:latest AS assets

# Copy the static files into a temporary location in this stage.
COPY . /assets

# Stage 2: The "final" stage
# This is the lean runtime image that will serve the files.
FROM nginx:stable-alpine

# Copy the static files from the "assets" stage into the Nginx public directory.
COPY --from=assets /assets /usr/share/nginx/html

# Expose port 80 for the Nginx server.
EXPOSE 80
