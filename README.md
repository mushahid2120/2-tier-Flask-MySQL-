# Docker Project: 2-Tier Flask-MySQL Application

This repository demonstrates the implementation of a two-tier architecture using Docker. The project includes a **Flask** application as the front-end tier and **MySQL** as the back-end database tier. The components are containerized using Docker for seamless deployment and scalability.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [License](#license)

---

## Features

- Two-tier architecture with Flask and MySQL
- Fully containerized using Docker
- Persistent data storage with Docker volumes
- Easy setup and deployment with `docker-compose`
- Scalable and portable infrastructure

---

## Prerequisites

Ensure you have the following installed on your system:

- **Docker** (version 20.10 or later)
- **Docker Compose** (version 2.0 or later)
- **Git** (for cloning the repository)

---

## Setup Instructions

Follow these steps to set up and run the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mushahid2120/Docker-Project-2-tier-Flask-MySQL-.git
   cd Docker-Project-2-tier-Flask-MySQL-

2. **Clone the Repository**:
- Copy the `.env.example` file to .env and update the environment variables:
    ```bash
    cp .env.example .env
- Modify the variables as needed:
    ```bash
    DB_USER=<your_mysql_user>
    DB_PASSWORD=<your_mysql_password>
    DB_NAME=<your_database_name>

3. **Build and Start the Containers:**
    ```bash
    docker-compose up --build

4.**Access the Application:**
- Flask Application: http://localhost:5000
- MySQL Database: Accessible on localhost:3306 (credentials  from .env)

## Project Structure
    ```bash
    Docker-Project-2-tier-Flask-MySQL-
    │
    ├── flask-app/                 # Flask application source code
    │   ├── app.py                 # Main application entry point
    │   ├── requirements.txt       # Python dependencies
    │   └── ...
    │
    ├── db/                        # MySQL initialization scripts
    │   ├── init.sql               # Database schema and seed data
    │   └── ...
    │
    ├── docker-compose.yml         # Docker Compose configuration
    ├── Dockerfile                 # Dockerfile for Flask application
    ├── .env.example               # Environment variables example
    └── README.md                  # Project documentation


### Usage
- To stop the containers:
    ```bash
    docker compose down
- To build and restart:
    ```bash
    docker-compose up --build
- Logs can be accessed using:
    ```bash
    docker-compose logs -f

## Technologies Used
- **Flask** : Python-based web framework for building the application.
- **MySQL** : Relational database for managing persistent data.
- **Docker** : Containerization platform for consistent deployments.
- **Docker Compose** : Tool for defining and managing multi-container Docker applications.