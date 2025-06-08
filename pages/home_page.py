class HomePage:
    def __init__(self, page):
        self.page = page
        self.home_menu_icon = page.locator("//*[contains(@class,'navbar')]//*[contains(text(),'Home')]")
        self.products_menu_icon = page.locator("//*[contains(@class,'navbar')]//*[contains(text(),'Products')]")
        self.cart_menu_icon = page.locator("//*[contains(@class,'navbar')]//*[contains(text(),'Cart')]")
        self.signup_login_menu_icon = page.locator("//*[contains(@class,'navbar')]//*[contains(text(),'Signup')]")
        self.testcases_menu_icon = page.locator("//*[contains(@class,'navbar')]//*[contains(text(),'Test Cases')]")
        self.apitesting_menu_icon = page.locator("//*[contains(@class,'navbar')]//*[contains(text(),'API Testing')]")
        self.video_tutorials_menu_icon = page.locator("//*[contains(@class,'navbar')]//*[contains(text(),'Video T')]")
        self.contact_us_menu_icon = page.locator("//*[contains(@class,'navbar')]//*[contains(text(),'Contact Us')]")
        self.logout_menu_icon = page.locator("//*[contains(@class,'navbar')]//*[contains(text(),'Logout')]")
        self.delete_account_menu_icon = page.locator("//*[contains(@class,'navbar')]//*[contains(text(),'Delete Account')]")