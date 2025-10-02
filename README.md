# Flask Task Manager API

A simple RESTful API for task management with in-memory storage.

## Installation

```bash
pip install flask
python app.py
```

Server runs at `http://localhost:5000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get single task |
| POST | /tasks | Create task |
| PUT/PATCH | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |

## Example Usage

Create a task:
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk and eggs"}'
```

Get all tasks:
```bash
curl http://localhost:5000/tasks
```

## Task Structure

```json
{
  "id": 1,
  "title": "Task title",
  "description": "Optional description",
  "status": "pending"
}
```

## Note

Uses in-memory storage. Data is lost on server restart.
