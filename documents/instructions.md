# Instructions

Download the latest code from the GitHub repository and unpack the zip-file.

## Installation

1. Install dependecies:

```
poetry install
```

2. Initialize database:

```
poetry run invoke build
```

3. Start the application:

```
poetry run invoke start
```

## Using the application

Head over to the register page by clicking 'Create an account'.


Type in your desired credentials, click on 'Register' and go back to the login screen by pressing 'Back to login'.


Type your credentials to the login fields and press 'Login'.

You are now in the budget view. You can add an income or an expense and see the sum under the 'Budget for this month'-label change accordingly. When you are done using the application, the 'Logout' button will log you out and take you back to the login screen. When you log back in you should see the previously added incomes & expenses.
