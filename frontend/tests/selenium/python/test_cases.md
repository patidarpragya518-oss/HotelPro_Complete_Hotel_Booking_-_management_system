# Test Cases for Hotel Management System (Selenium automation)

| Test Case ID | Title | Preconditions | Steps | Expected Result |
|--------------:|-------|---------------|-------|-----------------|
| TC-001 | Login - valid credentials | App running (frontend & backend), test user exists | 1. Navigate to /cuslogin 2. Enter valid email 3. Enter valid password 4. Click Login | User redirected to /rooms (customer) or /dashboard (admin). |
| TC-002 | Login - invalid password | App running | 1. Navigate to /cuslogin 2. Enter valid email 3. Enter invalid password 4. Click Login | Alert shown (unauthorized) and user stays on login page. |
| TC-003 | Registration - new user | App running | 1. Navigate to /cusreg 2. Fill required fields 3. Click Register | User created in backend; success message shown. |
| TC-004 | Room Booking - create booking | User logged in (customer) | 1. Navigate to booking page 2. Fill booking form 3. Submit | Booking created in backend and booking appears in list. |
| TC-005 | Payment - checkout (example) | Booking selected, payment provider configured | 1. Navigate to payment/checkout 2. Enter card/test payment details 3. Submit payment | Payment success page shown; backend receives confirmation. |

Notes:
- These tests assume the IDs/classes present in the current frontend (e.g., login email input id `form3Example3`). Update selectors if UI changes.
- For test isolation, tests should create and delete test data via backend API when possible.
