# Cell Experiment Management System

This project is a Django application for managing cell culture experiments. It includes features to create, edit, delete, and list experiments with associated metadata, cell lines, and infections.

## Setup Instructions

Follow these steps to set up the project environment and run the application locally.

### Prerequisites

- Python 3.8 or higher
- [Poetry](https://python-poetry.org/) for dependency management

### Installation

1. **Install dependencies using Poetry:**

    ```sh
    poetry install
    ```

2. **Activate the virtual environment:**

    ```sh
    poetry shell
    ```

### Database Setup

1. **Apply database migrations:**

    ```sh
    python manage.py migrate
    ```

2. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

3. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

### Accessing the Application

- Open your web browser and go to `http://127.0.0.1:8000` to access the application.
- Log in to the admin interface at `http://127.0.0.1:8000/admin` using the superuser credentials.

### Usage

Once the server is running, you can start creating, editing, and deleting cell experiments via the web interface.

---
