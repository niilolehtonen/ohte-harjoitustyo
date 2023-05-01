# Software engineering, practical exercise

## Budget application
- This application allows users to keep track of their monthly budget. A user can add an income or expense and the application displays how much of your budget you still have left. Everytime a user adds an income or an expense to the application the window will refresh and display changes in the budget.

## Documentation

- [Requirements Specification](https://github.com/niilolehtonen/ohte-harjoitustyo/blob/master/documents/vaatimusmaarittely.md)

- [Work Time Log](https://github.com/niilolehtonen/ohte-harjoitustyo/blob/master/documents/tyoaikakirjanpito.md)

- [Changelog](https://github.com/niilolehtonen/ohte-harjoitustyo/blob/master/documents/changelog.md)

- [Architecture Description](https://github.com/niilolehtonen/ohte-harjoitustyo/blob/master/documents/architecture.md)

## Releases

- [Release v1.0(Week 5)](https://github.com/niilolehtonen/ohte-harjoitustyo/releases/tag/Week5)

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

## Other command line commands

Command for running PyTest:

```
poetry run invoke test
```

Command for fetching test coverage:

```
poetry run invoke coverage-report
```

Command for running PyLint:
```
poetry run invoke lint
```
