import pytest
from helpers.user_data import generate_new_user_api_data


class TestApi:
    @pytest.fixture(autouse=True)
    def teardown_method(self, file_utils):
        file_utils.delete_all_files_in_dir()

    def test_get_all_products(self, api, file_utils):
        response = api.get_products()
        data = response.json()
        assert data["responseCode"] == 200
        assert len(data["products"]) > 0

        saved_path = file_utils.save_json_with_timestamp(data, "products")
        assert file_utils.compare_json_files("products.json", saved_path)

    def test_get_user_account_details_by_email(self, api, file_utils, app_config):
        response = api.get_user_detail_by_email(app_config.TESTER)
        data = response.json()
        assert data["responseCode"] == 200
        assert len(data["user"].keys()) > 0
        file_utils.save_json_with_timestamp(data, "userByEmail")

    def test_create_register_user_account(self, api, file_utils):
        user = generate_new_user_api_data()
        response = api.create_user_account(user)
        data = response.json()
        assert data["responseCode"] == 201
        assert data["message"] == "User created!"
        file_utils.save_json_with_timestamp(data, "createdUser")

    def test_verify_login_with_invalid_details(self, api):
        response = api.login("wrong@test.com", "password")
        data = response.json()
        assert data["responseCode"] == 404
        assert data["message"] == "User not found!"