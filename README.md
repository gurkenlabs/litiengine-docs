# LITIENGINE Documentation

Source repository for the official LITIENGINE documentation.

Documentation: [https://docs.litiengine.com/](https://docs.litiengine.com/)

## Local development

Install the documentation dependencies:

```bash
pip install -r requirements-docs.txt
```

Run the local documentation server:

```bash
zensical serve
```

Build the static site for production:

```bash
zensical build --clean --strict
```
