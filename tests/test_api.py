import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from userAPI import UserAPI

class TestUserAPI:
    @pytest.fixture
    def api(self):
        return UserAPI()

    def test_list_empty(self, api):
        result = api.list_users()
        assert result['count'] == 0
        assert result['status'] == 200

    def test_create_user(self, api):
        result = api.create_user({'name': 'Alice', 'email': 'alice@test.com'})
        assert result['status'] == 201
        assert result['user']['name'] == 'Alice'
        assert result['user']['id'] == 1

    def test_create_missing_name(self, api):
        result = api.create_user({'email': 'test@test.com'})
        assert result['status'] == 400

    def test_create_bad_email(self, api):
        result = api.create_user({'name': 'Bob', 'email': 'not-an-email'})
        assert result['status'] == 400

    def test_get_user(self, api):
        api.create_user({'name': 'Alice', 'email': 'alice@test.com'})
        result = api.get_user(1)
        assert result['status'] == 200
        assert result['user']['name'] == 'Alice'

    def test_get_nonexistent(self, api):
        result = api.get_user(999)
        assert result['status'] == 404

    def test_update_user(self, api):
        api.create_user({'name': 'Alice', 'email': 'alice@test.com'})
        result = api.update_user(1, {'name': 'Alice Updated'})
        assert result['status'] == 200
        assert result['user']['name'] == 'Alice Updated'

    def test_delete_user(self, api):
        api.create_user({'name': 'Alice', 'email': 'alice@test.com'})
        result = api.delete_user(1)
        assert result['status'] == 204
        assert api.get_user(1)['status'] == 404

    def test_duplicate_email(self, api):
        api.create_user({'name': 'Alice', 'email': 'alice@test.com'})
        result = api.create_user({'name': 'Bob', 'email': 'alice@test.com'})
        assert result['status'] == 400
