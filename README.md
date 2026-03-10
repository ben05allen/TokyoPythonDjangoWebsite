# Tokyo Python Meetup Website

## Setup (with uv)

```bash
uv sync
uv run manage.py migrate
uv run manage.py createsuperuser
uv run manage.py runserver
```

## Development

- Make sure that `uv` is available: e.g. `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Make sure `prek` is available: e.g. `cargo install prek`
- Install `prek` hooks: `prek install`
- Add packages: `uv add <package>` or `uv add --dev <package>`
- Format & lint: `uv run ruff check --fix .` or `pre-commit run --all-files`
- Run server: `uv run manage.py runserver`
