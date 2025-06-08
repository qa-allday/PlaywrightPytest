from playwright.sync_api import expect

class SignUpLoginPage:
    def __init__(self, page):
        self.page = page
        # Initial page elements
        self.login_email = page.locator("[data-qa=login-email]")
        self.login_password = page.locator("[data-qa=login-password]")
        self.login_button = page.locator("[data-qa=login-button]")
        self.signup_name = page.locator("[data-qa=signup-name]")
        self.signup_email = page.locator("[data-qa=signup-email]")
        self.signup_button = page.locator("[data-qa=signup-button]")

        # Signup Step#2 page elements
        self.signup2_name = page.locator("[data-qa=name]")
        self.signup2_email = page.locator("[data-qa=email]")
        self.signup2_password = page.locator("#password")
        self.signup2_first_name = page.locator("#first_name")
        self.signup2_last_name = page.locator("#last_name")
        self.signup2_address1 = page.locator("#address1")
        self.signup2_country = page.locator("#country")
        self.signup2_state = page.locator("#state")
        self.signup2_city = page.locator("#city")
        self.signup2_zipcode = page.locator("#zipcode")
        self.signup2_mobile_num = page.locator("#mobile_number")
        self.signup2_create_account_btn = page.locator("[data-qa=create-account]")

        # Signup Final page elements
        self.signup2_continue_btn = page.locator("[data-qa=continue-button]")

    def login_to_application(self, email, password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()

    def register_new_user(self, name, email):
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()

    def start_registration(self, user):
        self.signup_name.fill(user["name"])
        self.signup_email.fill(user["email"])
        self.signup_button.click()

    def fill_in_registration_form(self, user):
        self.signup2_password.fill(user["password"])
        self.signup2_first_name.fill(user["firstName"])
        self.signup2_last_name.fill(user["lastName"])
        self.signup2_address1.fill(user["address1"])
        self.signup2_country.select_option(user["country"])
        self.signup2_state.fill(user["state"])
        self.signup2_city.fill(user["city"])
        self.signup2_zipcode.fill(user["zipcode"])
        self.signup2_mobile_num.fill(user["mobile"])