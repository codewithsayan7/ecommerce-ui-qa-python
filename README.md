# E-Commerce UI Automation Suite (Python + Selenium + Pytest)

Automated end-to-end UI tests for an e-commerce storefront (`saucedemo.com`) built with Python, Selenium WebDriver, and Pytest using the Page Object Model (POM).

## What This Covers
- Login validation (valid user, locked-out user, wrong password, empty fields)
- Product catalog sorting and adding/removing items in the cart
- Checkout form validation (missing postal code / customer fields) and order confirmation
- Automatic screenshot capture on test failure
- HTML test report generation with `pytest-html`

## Project Structure
- `pages/` - Page Object classes (`login_page.py`, `inventory_page.py`, `cart_page.py`)
- `tests/` - Pytest test modules (`test_login.py`, `test_cart_and_checkout.py`)
- `docs/` - Manual test case sheet (`test_cases.csv`) and sample bug report (`bug_report_sample.md`)
- `conftest.py` - WebDriver setup, headless mode option, and failure screenshot hook

## Setup and Run
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest --html=reports/report.html --self-contained-html
```

To run headless (used in CI):
```bash
pytest --headless
```
