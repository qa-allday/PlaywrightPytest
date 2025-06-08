from playwright.sync_api import expect

class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.product_search_field = page.locator("#search_product")
        self.products_search_btn = page.locator("#submit_search")
        self.view_cart_link = page.locator("//*[contains(text(),'View Cart')]")
        self.continue_shopping_btn = page.locator("//button[contains(text(),'Continue Shopping')]")

    def search_product(self, product):
        self.product_search_field.fill(product)
        self.products_search_btn.click()

    def verify_search_products(self, name, count=1):
        all_cards_count = self.page.locator("//*[contains(@class,'productinfo')]").count()
        # Lowercase transformation for comparison
        labeled_cards_count = self.page.locator(
            f"//*[contains(@class,'productinfo')]//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{name.lower()}')]"
        ).count()

        assert all_cards_count == count, f"Expected {count} products, but found {all_cards_count}"
        assert labeled_cards_count == all_cards_count, "Mismatch in labeled cards count"

    def add_product_to_cart(self, name, position=1):
        # Hover over the product
        self.page.locator(
            f"(//*[contains(text(),'{name}')]//ancestor::*[contains(@class,'product-image-wrapper')])[{position}]"
        ).hover()

        # Hover over the overlay add-to-cart button
        self.page.locator(
            f"(//*[contains(@class,'overlay')]//*[contains(text(),'{name}')]/following-sibling::a)[{position}]"
        ).hover()

        # Click the overlay add-to-cart button
        self.page.locator(
            f"(//*[contains(@class,'overlay')]//*[contains(text(),'{name}')]/following-sibling::a)[{position}]"
        ).click()

        # Validate modal content
        modal_content = self.page.locator("//div[@class='modal-content']")
        expect(modal_content).to_contain_text("Added!")
        expect(modal_content).to_contain_text("Your product has been added to cart.")
        expect(self.view_cart_link).to_be_visible()
        expect(self.continue_shopping_btn).to_be_visible()

    def add_products_to_cart(self, products):
        for product in products:
            for _ in range(product["count"]):
                self.add_product_to_cart(product["name"])
                self.continue_shopping_btn.click()