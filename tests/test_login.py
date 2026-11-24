import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_valid_user_can_login(driver):
    login = LoginPage(driver).open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.heading() == "Products"


@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
        ("standard_user", "wrong_pass", "Username and password do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
)
def test_invalid_login_shows_error(driver, username, password, expected_error):
    login = LoginPage(driver).open()
    login.login(username, password)

    assert expected_error in login.get_error_message()
