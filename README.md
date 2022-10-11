# n5geh.tools.entirety

[![semantic-release](https://github.com/N5GEH/n5geh.tools.entirety/actions/workflows/semantic-release.yml/badge.svg)](https://github.com/N5GEH/n5geh.tools.entirety/actions/workflows/semantic-release.yml)
[![issue-tracker](https://github.com/N5GEH/n5geh.tools.entirety/actions/workflows/issue-tracker.yml/badge.svg)](https://github.com/N5GEH/n5geh.tools.entirety/actions/workflows/issue-tracker.yml)

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

## Built With

- Django 4.0.5
- Bootstrap 5.2.0-beta1
- htmx 1.7.0

## Getting Started

### Prerequisites

#### Installing dependencies

pip

```bash
  cd ./app/Entirety
  pip install -r requirements.txt
```

pre-commit

```bash
  pre-commit install
```

#### create .env File

```bash
  cp .env.EXAMPLE .env
```

## Usage

Migrate Database

```bash
  python manage.py makemigrations projects users examples
  python manage.py migrate
```

Starting the Django server:

```bash
  python manage.py runserver
```

## Contributing

See the [contributing guide](./docs/CONTRIBUTING.md) for detailed instructions on how to get started with our project.

## Development

To run the application in your development setup you'll need to
provide following settings in your env file.

### Required

* [DJANGO_SECRET_KEY](./docs/SETTINGS.md#django_secret_key)
* [OIDC_OP_AUTHORIZATION_ENDPOINT](./docs/SETTINGS.md#oidc_op_authorization_endpoint)
* [OIDC_OP_JWKS_ENDPOINT](./docs/SETTINGS.md#oidc_op_jwks_endpoint)
* [OIDC_OP_TOKEN_ENDPOINT](./docs/SETTINGS.md#oidc_op_token_endpoint)
* [OIDC_OP_USER_ENDPOINT](./docs/SETTINGS.md#oidc_op_user_endpoint)
* [OIDC_RP_CLIENT_ID](./docs/SETTINGS.md#oidc_rp_client_id)
* [OIDC_RP_CLIENT_SECRET](./docs/SETTINGS.md#oidc_rp_client_secret)

### Optional

* [DJANGO_DEBUG](./docs/SETTINGS.md#django_debug)
* [COMPRESS_ENABLED](./docs/SETTINGS.md#compress_enabled)

For a full list of settings see [settings](./docs/SETTINGS.md).

## Changelog

See [changelog](./docs/CHANGELOG.md) for detailed overview of changes.

## Contact

[@SBlechmann](https://github.com/SBlechmann)

[@sbanoeon](https://github.com/sbanoeon)

[@djs0109](https://github.com/djs0109)

[@dnikolay-ebc](https://github.com/dnikolay-ebc)

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
