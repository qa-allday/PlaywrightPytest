from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page

    def verify_product_row(self, product):
        # Check product price
        price_locator = self.page.locator(
            f"//*[contains(text(),'{product['name']}')]//ancestor::tr/*[@class='cart_price']"
        )
        expect(price_locator).to_contain_text(str(product["price"]))

        # Check product quantity
        quantity_locator = self.page.locator(
            f"//*[contains(text(),'{product['name']}')]//ancestor::tr/*[@class='cart_quantity']"
        )
        expect(quantity_locator).to_contain_text(str(product["count"]))

        # Calculate and check total
        total = product["count"] * product["price"]
        total_locator = self.page.locator(
            f"//*[contains(text(),'{product['name']}')]//ancestor::tr/*[@class='cart_total']"
        )
        expect(total_locator).to_contain_text(str(total))

    def verify_product_rows(self, products):
        for product in products:
            self.verify_product_row(product)