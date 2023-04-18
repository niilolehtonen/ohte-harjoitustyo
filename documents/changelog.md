# Changelog

## Week 3

- Initialized poetry environment
- Created a file that handles database connection and a file that can be used to initialize & modify the database
- Created a User-class, the user object can hold the username & password for a singular user
- Created a UserRepository-class which is used to access user information from the database
- Wrote a test for the UserRepository-class, that tests inserting an user to the database (this logic will be used in registration)
- Started working on UI
- Added first invokes

## Week 4

- UI now has 3 windows: Login, Register and Budget(the main app).
- Added 'Build'-function for initializing the database.
- A user can now create an account and login to the application. ('Error handling regarding this functionality still work in progress. Invalid username,password etc..')
