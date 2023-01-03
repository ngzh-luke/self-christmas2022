# We will use python:3.10-alpine as the base image for building the Flask container
FROM python:3.10-alpine

# It specifies the working directory where the Docker container will run
WORKDIR /app

# Copying all the application files to the working directory
COPY . .
# Install all the dependencies required to run the Flask application
RUN pip install -r requirements.txt
RUN pip install Flask gunicorn

# Expose the Docker container for the application to run on port 9999
EXPOSE 9999
# The command required to run the Dockerized application
CMD exec gunicorn --bind :9999 --workers 1 --threads 8 --timeout 0 app:app
```
