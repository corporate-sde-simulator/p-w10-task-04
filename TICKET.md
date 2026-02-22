# DATA-202: Build User Management REST API

**Status:** In Progress · **Priority:** Medium
**Sprint:** Sprint 31 · **Story Points:** 8
**Reporter:** Nisha Gupta (Tech Lead) · **Assignee:** You (Intern)
**Labels:** `api`, `rest`, `python`, `crud`
**Task Type:** Feature Ship

---

## Description

Build a complete REST API for user management. The spec is defined, the test suite
is written — you need to implement the API handlers.

## API Specification

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| GET | /users | List all users | 200 |
| GET | /users/:id | Get user by ID | 200 / 404 |
| POST | /users | Create user | 201 / 400 |
| PUT | /users/:id | Update user | 200 / 404 |
| DELETE | /users/:id | Delete user | 204 / 404 |

## Acceptance Criteria

- [ ] All 5 endpoints implemented
- [ ] Proper HTTP status codes
- [ ] Input validation (name required, email format)
- [ ] 404 for non-existent users
- [ ] All tests pass
