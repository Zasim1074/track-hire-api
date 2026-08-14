# TrackHire API

Production-oriented backend API for a TrackHire, built with **FastAPI, PostgreSQL, and SQLAlchemy 2.0**.

* For now the developement is under progress

TrackHire is being developed as a real-world backend engineering project rather than a tutorial CRUD application. The system is designed around role-based workflows for **Candidates, HR/Recruiters, Companies, Jobs, and Applications**.

The project is being built incrementally with production-oriented architecture, validation, security, database migrations, testing, containerization, and deployment in mind.

---

## 🚧 Project Status

**Currently under active development.**

### Completed

* [x] FastAPI application bootstrap
* [x] PostgreSQL database setup
* [x] Environment-based configuration
* [x] Pydantic Settings configuration
* [x] SQLAlchemy 2.0 engine setup
* [x] SQLAlchemy session management
* [x] PostgreSQL connectivity verification

### Planned

* [ ] Database models
* [ ] Alembic migrations
* [ ] User management
* [ ] Authentication
* [ ] JWT access tokens
* [ ] Role-based authorization
* [ ] Candidate workflows
* [ ] Company management
* [ ] Job management
* [ ] Job applications
* [ ] Bookmarks
* [ ] Resume upload
* [ ] Searching and filtering
* [ ] Pagination
* [ ] Admin APIs
* [ ] Validation and error handling
* [ ] Structured logging
* [ ] Automated testing
* [ ] Docker
* [ ] Production deployment
* [ ] Redis where justified by actual requirements

---

# Tech Stack

| Technology        | Purpose                                           |
| ----------------- | ------------------------------------------------- |
| Python 3.13+      | Backend language                                  |
| FastAPI           | REST API framework                                |
| PostgreSQL        | Primary relational database                       |
| SQLAlchemy 2.0    | ORM and database interaction                      |
| Pydantic v2       | Data validation and schemas                       |
| Pydantic Settings | Application configuration                         |
| psycopg           | PostgreSQL driver                                 |
| Alembic           | Database migrations                               |
| Pytest            | Testing                                           |
| Docker            | Containerization                                  |
| Redis             | Caching / supporting infrastructure when required |

---

# Architecture

The backend is being developed with clear separation of responsibilities.

```text
Client
  │
  ▼
FastAPI
  │
  ├── API / Routers
  │
  ▼
Services
  │
  ▼
Repositories
  │
  ▼
SQLAlchemy
  │
  ▼
PostgreSQL
```

Supporting infrastructure:

```text
                 ┌──────────────────┐
                 │    FastAPI App   │
                 └────────┬─────────┘
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
      Configuration    API Layer       Database
          │               │                │
          ▼               ▼                ▼
     Pydantic        Services         SQLAlchemy
      Settings           │                │
                         ▼                ▼
                    Repositories     PostgreSQL
```

The architecture will evolve as complexity increases. Patterns such as repositories and service layers will be introduced where they provide meaningful separation rather than adding unnecessary abstraction.

---

# Project Structure

Current structure:

```text
track-hire-api/
│
├── app/
│   ├── api/
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── test_connection.py
│   │
│   ├── models/
│   │
│   ├── repositories/
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │
│   └── main.py
│
├── alembic/
│
├── tests/
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Configuration

Application configuration is managed through **Pydantic Settings**.

Sensitive configuration is loaded from environment variables rather than being hardcoded into the source code.

Example:

```env
DATABASE_URL=postgresql+psycopg://trackhire_user:PASSWORD@localhost:5432/trackhire_db
ALGORITHM=HS256
SECRET_KEY=YOUR_SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES=1000
```

The `.env` file must **never be committed to Git**.

A sanitized `.env.example` file is maintained for development setup.

---

# Database

TrackHire uses PostgreSQL as its primary database.

The application communicates with PostgreSQL through:

```text
FastAPI
   │
   ▼
SQLAlchemy 2.0
   │
   ▼
psycopg
   │
   ▼
PostgreSQL
```

Database sessions are managed through FastAPI dependency injection.

The application uses a connection pool rather than establishing a new database connection for every request.

---

# Local Development

## 1. Clone the repository

```bash
git clone <repository-url>
cd track-hire-api
```

## 2. Create a virtual environment

```bash
python3.13 -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create:

```text
.env
```

based on:

```text
.env.example
```

Configure your local PostgreSQL connection.

---

## 5. Start the development server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Database Connectivity Test

The project contains a development database connectivity check.

Run:

```bash
python -m app.db.test_connection
```

Expected result:

```text
Database connected successfully!
```

This verifies the complete connection path:

```text
Application
     ↓
Pydantic Settings
     ↓
SQLAlchemy Engine
     ↓
psycopg
     ↓
PostgreSQL
```

---

# API

The API follows REST-oriented conventions and will progressively introduce:

* HTTP status codes
* Request validation
* Response schemas
* Authentication
* Authorization
* Pagination
* Filtering
* Searching
* Consistent error responses

The API documentation is automatically generated by FastAPI.

Once the server is running:

```text
/docs
```

provides the Swagger UI.

---

# Core Domain

The application is centered around two primary user workflows.

```text
                    TrackHire
                       │
             ┌─────────┴─────────┐
             │                   │
          Candidate          HR / Recruiter
             │                   │
             ▼                   ▼
        Find Jobs            Create Jobs
             │                   │
             ▼                   ▼
         Apply Job          Manage Applications
             │                   │
             └─────────┬─────────┘
                       ▼
                   Companies
```

Planned major entities:

```text
User
 ├── Candidate
 └── HR / Recruiter

Company
Job
Application
Bookmark
Resume
```

The exact database relationships will be designed before implementing the models.

---

# Security

Security will be treated as a first-class concern.

Planned security mechanisms include:

* Password hashing
* JWT authentication
* Role-based authorization
* Protected API endpoints
* Input validation
* Environment-based secrets
* Secure file upload handling
* Authorization checks at the appropriate application layer

Secrets and credentials will never be committed to source control.

---

# Testing

Testing will be introduced after the core domain functionality is established.

Planned test coverage:

```text
Unit Tests
    │
    ├── Services
    ├── Utilities
    └── Validation
          │
          ▼
Integration Tests
    │
    ├── Database
    ├── Authentication
    └── API workflows
          │
          ▼
End-to-End Critical Flows
```

Pytest will be used as the primary testing framework.

---

# Database Migrations

Alembic will be used to manage database schema changes.

The intended workflow:

```text
SQLAlchemy Models
       │
       ▼
Alembic Migration
       │
       ▼
Review Migration
       │
       ▼
PostgreSQL
```

Migration files will be committed to source control so database schema changes are reproducible across environments.

---

# Docker

Docker will be introduced after the application and database architecture stabilize.

The target development environment will eventually support:

```text
Docker Compose
    │
    ├── TrackHire API
    │
    └── PostgreSQL
```

Additional infrastructure such as Redis will only be introduced when the application has a concrete requirement for it.

---

# Production Considerations

The project is being developed with production engineering principles in mind:

* Environment-based configuration
* Database connection pooling
* Transaction boundaries
* Schema validation
* Separation of responsibilities
* Secure authentication
* Role-based authorization
* Database migrations
* Structured logging
* Automated testing
* Containerization
* Deployment configuration
* Error handling
* API observability

The goal is not to maximize the number of technologies used, but to understand **why each component exists and when it is appropriate**.

---

# Development Philosophy

TrackHire is intentionally being developed incrementally.

Features are introduced only after their underlying infrastructure and design decisions are understood.

The development process follows:

```text
Requirement
    ↓
Design
    ↓
Implementation
    ↓
Code Review
    ↓
Refactoring
    ↓
Testing
    ↓
Documentation
```

The project prioritizes:

1. Correctness
2. Maintainability
3. Security
4. Testability
5. Performance
6. Simplicity

Performance optimizations and additional infrastructure will be introduced based on actual requirements rather than premature optimization.

---

# Roadmap

## Phase 1 — Foundation

* [x] FastAPI setup
* [x] PostgreSQL setup
* [x] Environment configuration
* [x] SQLAlchemy engine
* [x] Database sessions
* [ ] Declarative base
* [ ] Alembic integration

## Phase 2 — Identity

* [ ] User model
* [ ] Password hashing
* [ ] Registration
* [ ] Login
* [ ] JWT authentication
* [ ] Current-user dependency
* [ ] Role-based authorization

## Phase 3 — Job Platform

* [ ] Companies
* [ ] Jobs
* [ ] Job publishing
* [ ] Job updating
* [ ] Job deletion
* [ ] Job searching
* [ ] Filtering
* [ ] Pagination
* [ ] Bookmarks

## Phase 4 — Applications

* [ ] Job applications
* [ ] Application status
* [ ] Candidate workflow
* [ ] Recruiter workflow
* [ ] Application authorization
* [ ] Resume upload

## Phase 5 — Administration

* [ ] Admin roles
* [ ] User management
* [ ] Company management
* [ ] Job moderation
* [ ] Administrative APIs

## Phase 6 — Quality & Production

* [ ] Unit tests
* [ ] Integration tests
* [ ] Structured logging
* [ ] Error handling
* [ ] Docker
* [ ] CI/CD
* [ ] Production deployment
* [ ] Performance analysis
* [ ] Redis where justified

---

# Author

**Jaseem Quraishi**

Frontend Engineer transitioning toward full-stack/backend engineering.

TrackHire is being developed as a serious backend engineering project to demonstrate practical experience with Python, FastAPI, PostgreSQL, SQLAlchemy, authentication, authorization, testing, and production backend architecture.
