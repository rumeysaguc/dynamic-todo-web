# Todo Web Application

This is a todo web application built using Django for the backend, htmx for dynamic behavior on the frontend, and Tailwind CSS for styling. Django Rest Framework is utilized for data serialization. If you wish to access all task data in JSON format, you can use the `localhost:8000/api/tasks` URL.

## Technologies Used

- **Django:** Django, a Python-based web framework, is used to develop the backend of this application.
- **htmx:** Htmx is a library used for adding dynamic behavior to web pages. In our application, htmx is used for performing backend operations without page reloads.
- **Tailwind CSS:** Tailwind CSS is a utility-first CSS framework used for styling the user interface of our application.
- **Django Rest Framework:** Django Rest Framework is employed for serializing data and building RESTful APIs.
- **Flake8:** I used flake8 becouse of formatting my python code. (flake8 example.py and black example.py)

## Getting Started

To run this application locally, you'll need Docker and Docker Compose installed on your system. Follow the steps below:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the following command to build and start the Docker containers:

    ```
    docker-compose up
    ```

4. Once the containers are up and running, you can access the application in your web browser at `http://localhost:8000`.

## API Endpoint

- To access all task data in JSON format, use the following URL:

    ```
    http://localhost:8000/api/tasks
    ```
