from selenium.webdriver.common.by import By


class CartPage:
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ERROR_BANNER = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def start_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()

    def fill_customer_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def finish_order(self):
        self.driver.find_element(*self.FINISH_BTN).click()

    def confirmation_text(self):
        return self.driver.find_element(*self.COMPLETE_HEADER).text

    def error_text(self):
        return self.driver.find_element(*self.ERROR_BANNER).text
