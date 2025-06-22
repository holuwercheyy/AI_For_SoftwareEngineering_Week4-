## Feature: PowerLearn Academy Login Validation
#### Tests for valid and invalid login scenarios

### Test Case 1: Valid Login (Successful Authentication)
  **Steps**:
  1. Navigate to "https://academy.powerlearnprojectafrica.org/login"
  2. Enter valid email in the [Email] field
  3. Enter valid password in the [Password] field
  4. Click the [Login] button
  5. Verify redirection to the dashboard URL: "/dashboard"
  6. Validate presence of user-specific elements (e.g., profile icon)

### Test Case 2: Invalid Login (Authentication Failure)
  **Steps**:
  1. Navigate to "https://academy.powerlearnprojectafrica.org/login"
  2. Enter invalid email (e.g., "invalid_user@test.com") in the [Email] field
  3. Enter invalid password (e.g., "wrong_password123") in the [Password] field
  4. Click the [Login] button
  5. Verify URL remains on "/login"
  6. Validate visibility of error message: "Invalid credentials"
  7. Confirm login button is still enabled for retry