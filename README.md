\# Docker Week 2 Demo — Flask Application



\## Project Overview



This project demonstrates how to containerize a simple Python Flask web application using Docker.



The application displays a success message in the browser when accessed through port 5000.



\## Technologies Used



\* Python 3.12

\* Flask

\* Docker

\* Docker Desktop

\* Git and GitHub



\## Project Structure



```text

docker-week2-demo/

├── app.py

├── requirements.txt

├── Dockerfile

├── .dockerignore

└── README.md

```



\## Application Features



\* Simple Flask web application.

\* Docker image creation using a Dockerfile.

\* Dependency installation during the image build.

\* Container execution with port mapping.

\* Browser-based application verification.



\## Build the Docker Image



Open a terminal in the project directory and run:



```bash

docker build -t docker-week2-demo .

```



\## Run the Docker Container



Run the following command:



```bash

docker run --name docker-week2-container -p 5000:5000 docker-week2-demo

```



\## Access the Application



Open the following address in your browser:



```text

http://localhost:5000

```



Expected output:



```text

Hello! My Week 2 Docker application is running successfully.

```



\## Verify the Container



List running containers:



```bash

docker ps

```



View container logs:



```bash

docker logs docker-week2-container

```



\## Stop the Container



Open another terminal and run:



```bash

docker stop docker-week2-container

```



\## Learning Outcomes



\* Learned the purpose and structure of a Dockerfile.

\* Learned how to create a Docker image.

\* Learned how to run a container.

\* Learned how to map container ports to the host machine.

\* Learned how to verify a containerized application.

\* Practiced troubleshooting Docker image and container errors.



\## Conclusion



Successfully containerized and tested a Python Flask application using Docker. The application runs inside a container and is accessible through the browser using port 5000.



