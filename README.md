# CRM API

A Django REST API for managing CRM data with JWT authentication, ownership-based access control, filtering, search, ordering, and API documentation.

# Features

- User registration
- JWT login
- JWT token refresh
- Protected `me` endpoint
- Clients CRUD
- Leads CRUD
- Interactions CRUD
- Tasks CRUD
- Ownership validation
- Filtering, search, and ordering
- Swagger/OpenAPI documentation with drf-spectacular
- Automated API tests

# Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- `django-filter`
- `drf-spectacular`
- SQLite

# Project Apps

- `users`
- `clients`
- `leads`
- `interactions`
- `tasks`

# Setup

## 1. Clone the repository

```bash
git clone https://github.com/adrianatortja/crm-api.git
cd crm-api
```

## 2. Create and activate a virtual environment

### Windows PowerShell

```bash
python -m venv venv
venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Apply migrations

```bash
python manage.py migrate
```

## 5. Run the server

```bash
python manage.py runserver
```

# Authentication

JWT authentication is used for protected endpoints.

Add this header to protected requests:

```http
Authorization: Bearer <access_token>
```

# Endpoints

## Auth

- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `POST /api/auth/refresh/`
- `GET /api/auth/me/`

## Clients

- `GET /api/clients/`
- `POST /api/clients/`
- `GET /api/clients/<id>/`
- `PATCH /api/clients/<id>/`
- `DELETE /api/clients/<id>/`

## Leads

- `GET /api/leads/`
- `POST /api/leads/`
- `GET /api/leads/<id>/`
- `PATCH /api/leads/<id>/`
- `DELETE /api/leads/<id>/`

## Interactions

- `GET /api/interactions/`
- `POST /api/interactions/`
- `GET /api/interactions/<id>/`
- `PATCH /api/interactions/<id>/`
- `DELETE /api/interactions/<id>/`

## Tasks

- `GET /api/tasks/`
- `POST /api/tasks/`
- `GET /api/tasks/<id>/`
- `PATCH /api/tasks/<id>/`
- `DELETE /api/tasks/<id>/`

# Filtering, Search, and Ordering

The API supports filtering, search, and ordering on list endpoints.

## Clients

- Filter: `status`
- Search: `name`, `company`, `email`
- Order: `name`, `created_at`

Examples:

- `/api/clients/?status=active`
- `/api/clients/?search=acme`
- `/api/clients/?ordering=name`

## Leads

- Filter: `status`, `source`, `client`
- Search: `title`, `notes`, `client__name`
- Order: `title`, `created_at`

Examples:

- `/api/leads/?status=new`
- `/api/leads/?source=linkedin`
- `/api/leads/?search=website`
- `/api/leads/?ordering=title`

## Interactions

- Filter: `interaction_type`, `lead`
- Search: `subject`, `notes`, `lead__title`
- Order: `created_at`, `subject`

Examples:

- `/api/interactions/?interaction_type=call`
- `/api/interactions/?search=follow up`
- `/api/interactions/?ordering=subject`

## Tasks

- Filter: `status`, `lead`, `due_date`
- Search: `title`, `description`, `lead__title`
- Order: `due_date`, `created_at`, `title`

Examples:

- `/api/tasks/?status=pending`
- `/api/tasks/?due_date=2026-04-30`
- `/api/tasks/?search=proposal`
- `/api/tasks/?ordering=due_date`

# Ownership Rules

Each authenticated user can only access their own data.

This includes:

- only their own clients
- only leads connected to their own clients
- only their own interactions
- only their own tasks

# API Documentation

After running the server, open:

- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- OpenAPI schema: `http://127.0.0.1:8000/api/schema/`

# Running Tests

Run the full test suite with:

```bash
python manage.py test

```

# Notes

This project was built as a backend portfolio project to practice building a real-world CRM API with authentication, ownership-based access control, validation, filtering, search, ordering, and documentation.

It demonstrates:

- clean Django app structure
- RESTful CRUD endpoints
- JWT authentication
- protected user-scoped data access
- practical API filtering and search
- auto-generated API docs with drf-spectacular


