# TEQ
 Test Exam Quiz - app for student testing

A full-stack platform for creating and evaluating diverse types of educational or technical tasks. The system supports automatic answer checking, code execution, and test running.

## Project Structure

- **Backend**: Django (Python)
- **Frontend**: Vue.js 3
- **Databases**: PostgreSQL (relational), MongoDB (non-relational)
- **Async Tasks**: Celery with Redis
- **Containerized**: Docker + Docker Compose

## Features

- Create tasks of various types:
    - Multiple/single choice
    - Short and long text answers
    - Code-based answers (Python, C++, Java)
- Automatic answer validation and grading
- Run and test code submissions in sandboxed environments

## Setup

1. Configure `.env` files for frontend and backend
2. Start all services:
   ```bash
   docker-compose up --build
3. Migrate database
    ```bash
   docker exec -it django-server python manage.py migrate
