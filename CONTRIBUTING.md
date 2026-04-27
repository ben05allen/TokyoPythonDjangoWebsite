# Contributing to the Tokyo Python Meetup Website

Thank you for your interest in contributing! This project is the official website for the **Tokyo Python Meetup Community**, and contributions are open exclusively to members of that community.

---

## Who Can Contribute?

This repository is a community project, maintained **by Tokyo Python Meetup members, for Tokyo Python Meetup members**. To contribute, you must be an active or past attendee of the Tokyo Python Meetup.

If you're unsure whether you qualify, or if you'd like to get involved with the community, you can find us on [Meetup.com](https://www.meetup.com/tokyopython). Pull requests from outside the community will be closed without review — no hard feelings!

---

## Getting Started

### Prerequisites

Make sure the following tools are available on your system:

- [uv](https://astral.sh/uv) — Python package and project manager
- [prek](https://github.com/nicholasgasior/prek) — pre-commit hook runner (`cargo install prek`)

### Setup

```bash
uv sync
uv run manage.py migrate
uv run manage.py createsuperuser
uv run manage.py runserver
```

### Install Pre-commit Hooks

```bash
prek install
```

This ensures your code is automatically formatted and linted before each commit.

---

## Development Workflow

### Branches

- Work on a feature branch cut from `main`.
- Use a descriptive branch name, e.g. `feature/event-listing-page` or `fix/navbar-mobile`.

### Adding Dependencies

```bash
uv add <package>           # runtime dependency
uv add --dev <package>     # development-only dependency
```

### Formatting & Linting

```bash
pre-commit run --all-files
```

Please make sure your code passes linting before opening a pull request.

---

## Design Guidelines

This project follows a defined design system — **"The Architectural Minimalist"** — documented in [`DESIGN.md`](./DESIGN.md). Before working on any frontend changes, please read that document. Key principles to keep in mind:

- **No 1px solid borders.** Sections are separated through background color shifts, not lines.
- **No standard drop shadows.** Elevation is achieved through tonal layering.
- **Typography:** Headlines use Manrope; body text uses Inter. Respect the scale.
- **Python Red (`#E4231E`) is an accent colour** — use it sparingly for CTAs and branding.
- Use whitespace generously. If a section feels crowded, increase the spacing.

---

## Submitting a Pull Request

1. Fork the repository and create your branch from `main`.
2. Make your changes, ensuring the dev server runs cleanly (`uv run manage.py runserver`).
3. Run linting: `pre-commit run --all-files`.
4. Open a pull request against `main` with a clear description of what you've changed and why.
5. A maintainer from the community will review your PR. Please be patient — we're all volunteers!

---

## Reporting Issues

If you find a bug or have a feature idea, please [open an issue](https://github.com/ben05allen/TokyoPythonDjangoWebsite/issues) first so we can discuss it before any work begins.

---

## Code of Conduct

We follow the same culture of respect and inclusion that we bring to our meetups. Be kind, be constructive, and have fun building something for our community together.
