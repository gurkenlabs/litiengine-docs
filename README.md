# LITIENGINE Docs

Source repository for the official LITIENGINE docs.

Documentation: [https://docs.litiengine.com/](https://docs.litiengine.com/)

[![Sponsor LITIENGINE on Open Collective](https://opencollective.com/litiengine/tiers/badge.svg)](https://opencollective.com/litiengine)

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
