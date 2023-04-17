# Software engineering, practical exercise

## Documentation

- [Requirements Specification](https://github.com/niilolehtonen/ohte-harjoitustyo/blob/master/documents/vaatimusmaarittely.md)

- [Work Time Log](https://github.com/niilolehtonen/ohte-harjoitustyo/blob/master/documents/tyoaikakirjanpito.md)


- [Changelog](https://github.com/niilolehtonen/ohte-harjoitustyo/blob/master/documents/changelog.md)

## Installation

1. Install dependecies:

```bash
poetry install
```

2. Initialize database:

```bash
poetry run invoke build
```

3. Start the application:

```bash
poetry run invoke start
```
