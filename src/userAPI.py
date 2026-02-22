"""
User Management API — implement CRUD endpoints.

This is a Feature Ship task. The stubs are defined with
"""

import re
from typing import Dict, List, Optional


class UserAPI:
    def __init__(self):
        self.users: Dict[int, dict] = {}
        self.next_id = 1

    def list_users(self) -> dict:
        \"\"\"GET /users — return all users.\"\"\"
        pass

    def get_user(self, user_id: int) -> dict:
        \"\"\"GET /users/:id — return a single user or 404.\"\"\"
        pass

    def create_user(self, data: dict) -> dict:
        \"\"\"POST /users — create a new user.

        Required fields: name (str), email (str, valid format)
        Optional: age (int, >= 0)

        Return: {'user': {...}, 'status': 201} on success
        Return: {'error': '...', 'status': 400} on validation failure
        \"\"\"
        # 1. Validate 'name' exists and is non-empty string
        # 2. Validate 'email' exists and matches basic email format
        # 3. Check for duplicate email
        # 4. Assign auto-incremented ID
        # 5. Store user and return with status 201
        pass

    def update_user(self, user_id: int, data: dict) -> dict:
        \"\"\"PUT /users/:id — update an existing user.\"\"\"
        # Return 404 if user doesn't exist
        pass

    def delete_user(self, user_id: int) -> dict:
        \"\"\"DELETE /users/:id — delete a user.\"\"\"
        # Return 404 if user doesn't exist
        pass

    def _validate_email(self, email: str) -> bool:
        \"\"\"Check if email matches basic format.\"\"\"
        pass
