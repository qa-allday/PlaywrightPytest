class ApiHelpers:
    def __init__(self, request_context):
        self.request = request_context

    def get_products(self):
        response = self.request.get("productsList")
        return response

    def get_brands(self):
        response = self.request.get("brandsList")
        return response

    def login(self, email, password):
        response = self.request.post(
            "verifyLogin",
            form={"email": email, "password": password}
        )
        return response

    def get_user_detail_by_email(self, email):
        response = self.request.get(
            "getUserDetailByEmail",
            params={"email": email}
        )
        return response

    def create_user_account(self, user_data):
        response = self.request.post(
            "createAccount",
            form=user_data
        )
        return response