# E-Commerce UI Automation Suite (Python + Selenium + Pytest)

Automated end-to-end UI tests for the SauceDemo practice storefront using Python, Selenium WebDriver, and Pytest with the Page Object Model (POM).

## What This Covers
- Login validation (valid user, locked-out user, wrong password, and empty fields)
- Product catalog sorting and adding/removing items in the cart
- Checkout form validation and order confirmation
- Screenshot capture when a test fails
- HTML test report generation with `pytest-html`

## Project Structure
- `pages/` - Page Object classes for login, inventory, and cart pages
- `tests/` - Pytest test modules
- `docs/` - Manual test cases and a sample bug report
- `conftest.py` - WebDriver fixture, headless mode option, and failure screenshot hook
- `.github/workflows/` - GitHub Actions workflow for headless test execution

## Setup and Run
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
mkdir -p reports
pytest --html=reports/report.html --self-contained-html
```

To run headless (used in CI):
```bash
mkdir -p reports
pytest --headless --html=reports/report.html --self-contained-html
```

The UI tests use the public SauceDemo practice site. The browser must be available locally for non-CI runs.
