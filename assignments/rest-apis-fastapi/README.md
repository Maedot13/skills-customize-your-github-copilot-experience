# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, fast REST APIs using the FastAPI framework. You will create a functional API with multiple endpoints, request validation, and response models by building a simple task management system.

## 📝 Tasks

### 🛠️ Set Up FastAPI and Create Basic Endpoints

#### Description
Initialize a FastAPI application and create basic GET and POST endpoints for managing tasks.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create a FastAPI application instance
- Define a `Task` model with `id`, `title`, `description`, and `completed` fields
- Implement a GET endpoint to retrieve all tasks
- Implement a POST endpoint to create a new task
- Run the server and test endpoints using interactive API documentation


### 🛠️ Add Path Parameters and Request Validation

#### Description
Extend the API with endpoints that use path parameters to retrieve and update individual tasks.

#### Requirements
Completed program should:

- Create a GET endpoint that retrieves a specific task by `id`
- Create a PUT endpoint to update a task by `id`
- Create a DELETE endpoint to remove a task by `id`
- Implement proper validation for request data (ensure required fields are present)
- Return appropriate HTTP status codes (200, 201, 404)
- Test all endpoints with sample requests


### 🛠️ Add Query Parameters and Advanced Features (Stretch Goal)

#### Description
Enhance the API with query parameters for filtering and implement in-memory data persistence.

#### Requirements
Completed program should:

- Add a query parameter to filter tasks by completion status
- Add a query parameter to limit the number of returned results
- Implement a simple in-memory task storage (list or dictionary)
- Include proper error handling with descriptive error messages
- Document the API endpoints with docstrings and FastAPI's automatic OpenAPI documentation
