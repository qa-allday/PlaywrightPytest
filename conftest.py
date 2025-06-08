import pytest
from playwright.sync_api import sync_playwright
import config
from api.api_helpers import ApiHelpers
from pages.products_page import ProductsPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.signup_login_page import SignUpLoginPage
from utils.file_utils import FileUtils

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def app_config():
    return config

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def api_request_context(playwright_instance,app_config):
    request_context = playwright_instance.request.new_context(
        base_url=app_config.API_URL
    )
    yield request_context
    request_context.dispose()

@pytest.fixture
def products_page(page):
    return ProductsPage(page)

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def signup_login_page(page):
    return SignUpLoginPage(page)

@pytest.fixture(name="api")
def api_helpers(api_request_context):
    return ApiHelpers(api_request_context)

@pytest.fixture
def file_utils():
    return FileUtils()