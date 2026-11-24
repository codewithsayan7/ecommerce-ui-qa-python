# Sample Bug Report

- **Bug ID:** BUG-104
- **Title:** Checkout allows proceeding when cart is empty
- **Module:** Cart / Checkout
- **Severity:** High
- **Priority:** Medium
- **Environment:** Chrome 131, Windows 11, https://www.saucedemo.com/

## Steps to Reproduce
1. Log in as `standard_user`.
2. Click the shopping cart icon without adding any items.
3. Click the `Checkout` button.

## Expected Result
The `Checkout` button should be disabled or display a message stating the cart is empty.

## Actual Result
The application navigates to the customer information page and allows placing an order with $0.00 total.
