from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


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
        self.wait = WebDriverWait(driver, 10)

    def heading(self):
        element = self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE))
        return element.text

    def add_backpack(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BACKPACK_BTN)).click()

    def remove_backpack(self):
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_BACKPACK_BTN)).click()
        self.wait.until(EC.invisibility_of_element_located(self.CART_BADGE))

    def cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()

    def sort_by(self, value):
        dropdown = self.wait.until(EC.visibility_of_element_located(self.SORT_DROPDOWN))
        Select(dropdown).select_by_value(value)

    def get_prices(self):
        self.wait.until(EC.presence_of_all_elements_located(self.ITEM_PRICES))
        elements = self.driver.find_elements(*self.ITEM_PRICES)
        return [float(element.text.replace("$", "")) for element in elements]
