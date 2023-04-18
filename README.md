# Software engineering, practical exercise

## Documentation

- [Requirements Specification](https://github.com/niilolehtonen/ohte-harjoitustyo/blob/master/documents/vaatimusmaarittely.md)

- [Work Time Log](https://github.com/niilolehtonen/ohte-harjoitustyo/blob/master/documents/tyoaikakirjanpito.md)

- [Changelog](https://github.com/niilolehtonen/ohte-harjoitustyo/blob/master/documents/changelog.md)

- [Architecture Description](https://github.com/niilolehtonen/ohte-harjoitustyo/blob/master/documents/architecture.md)

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
