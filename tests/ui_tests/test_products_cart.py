import pytest
from playwright.sync_api import expect

class TestProductsCart:
    @pytest.fixture(autouse=True)
    def setup_method(self,page, home_page, app_config):
        page.goto(app_config.WEB_URL)
        home_page.products_menu_icon.click()

    def test_search_product(self,page, products_page):
        expect(page.get_by_text("ALL PRODUCTS")).to_be_visible()
        products_page.search_product("blue")
        expect(page.get_by_text("SEARCHED PRODUCTS")).to_be_visible()
        products_page.verify_search_products("blue", 7)

    def test_add_products_to_cart(self,products_page, home_page, cart_page):
        products = [
            {"name": "Blue Top", "count": 3, "price": 500},
            {"name": "Blue Slim Fit Jeans", "count": 1, "price": 1400},
        ]
        products_page.search_product("blue")
        products_page.add_products_to_cart(products)

        home_page.cart_menu_icon.click()
        cart_page.verify_product_rows(products)