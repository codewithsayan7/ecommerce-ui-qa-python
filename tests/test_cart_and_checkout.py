import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def login_as_standard_user(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")


@pytest.mark.smoke
def test_add_and_remove_item_updates_cart_badge(driver):
    login_as_standard_user(driver)
    inventory = InventoryPage(driver)

    inventory.add_backpack()
    assert inventory.cart_count() == 1

    inventory.remove_backpack()
    assert inventory.cart_count() == 0


@pytest.mark.regression
def test_sort_products_by_price_low_to_high(driver):
    login_as_standard_user(driver)
    inventory = InventoryPage(driver)

    inventory.sort_by("lohi")
    prices = inventory.get_prices()
    assert prices == sorted(prices)


@pytest.mark.smoke
def test_complete_checkout_flow(driver):
    login_as_standard_user(driver)
    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.start_checkout()
    cart.fill_customer_info("Sayan", "Banerjee", "723101")
    cart.finish_order()

    assert "Thank you for your order!" in cart.confirmation_text()


@pytest.mark.regression
def test_checkout_blocks_missing_postal_code(driver):
    login_as_standard_user(driver)
    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.start_checkout()
    cart.fill_customer_info("Sayan", "Banerjee", "")

    assert "Postal Code is required" in cart.error_text()
