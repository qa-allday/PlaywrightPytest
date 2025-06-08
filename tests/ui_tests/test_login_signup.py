import re
import pytest
from playwright.sync_api import expect
from helpers.user_data import generate_new_user_data

class TestLoginSignup:
    @pytest.fixture(autouse=True)
    def setup_method(self, page, home_page, app_config):
        page.goto(app_config.WEB_URL)
        home_page.signup_login_menu_icon.click()

    def test_register_new_user(self, page, home_page, signup_login_page):
        user = generate_new_user_data()
        # Check that signup name field is visible
        expect(signup_login_page.signup_name).to_be_visible()
        # Start registration
        signup_login_page.start_registration(user)
        # Verify name and email fields
        expect(signup_login_page.signup2_name).to_have_value(user["name"])
        expect(signup_login_page.signup2_email).to_have_value(user["email"])
        # Fill in registration form
        signup_login_page.fill_in_registration_form(user)
        # Click create account button
        signup_login_page.signup2_create_account_btn.click()
        # Verify account created
        expect(page.get_by_text("ACCOUNT CREATED!")).to_be_visible()
        expect(signup_login_page.signup2_continue_btn).to_be_visible()
        # Continue after account creation
        signup_login_page.signup2_continue_btn.click()
        # Check home page - logout and delete account buttons visible
        expect(home_page.logout_menu_icon).to_be_visible()
        expect(home_page.delete_account_menu_icon).to_be_visible()
        expect(home_page.signup_login_menu_icon).not_to_be_visible()
        # Delete the account
        home_page.delete_account_menu_icon.click()
        expect(page.get_by_text("ACCOUNT DELETED!")).to_be_visible()
        expect(signup_login_page.signup2_continue_btn).to_be_visible()
        # Continue after deleting the account
        signup_login_page.signup2_continue_btn.click()
        expect(home_page.signup_login_menu_icon).to_be_visible()

    def test_login_with_valid_credentials_and_logout(self, page, home_page, signup_login_page, app_config):
        # Login
        signup_login_page.login_to_application(app_config.TESTER, app_config.PASSWORD)
        expect(home_page.delete_account_menu_icon).to_be_visible()
        # Logout
        home_page.logout_menu_icon.click()
        expect(page).to_have_url(re.compile(".*login"))
        expect(home_page.signup_login_menu_icon).to_be_visible()
        expect(signup_login_page.login_email).to_be_visible()