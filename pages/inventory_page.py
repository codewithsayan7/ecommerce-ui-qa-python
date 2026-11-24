from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_BTN = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver

    def heading(self):
        return self.driver.find_element(*self.PAGE_TITLE).text

    def add_backpack(self):
        self.driver.find_element(*self.ADD_BACKPACK_BTN).click()

    def remove_backpack(self):
        self.driver.find_element(*self.REMOVE_BACKPACK_BTN).click()

    def cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

    def sort_by(self, value):
        Select(self.driver.find_element(*self.SORT_DROPDOWN)).select_by_value(value)

    def get_prices(self):
        elements = self.driver.find_elements(*self.ITEM_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]
