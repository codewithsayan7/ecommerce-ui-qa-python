from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
        self.wait = WebDriverWait(driver, 10)

    def start_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))

    def fill_customer_info(self, first_name, last_name, postal_code):
        first_name_input = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        postal_code_input = self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE)
        )
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)

        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN)).click()

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()

    def confirmation_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        ).text

    def error_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_BANNER)
        ).text
