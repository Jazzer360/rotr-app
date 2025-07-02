# Copilot Custom Instructions for rotr-app

## Project Overview
This repository is a Reflex (rx) Python web application for ROTR, structured with modular components, pages, and utilities. It uses a template pattern for page layout and includes custom navigation, footer, and survey popup components.

## Coding Guidelines
- Use Python 3.12+ and Reflex (rx) for all web UI code.
- Organize new features into appropriate subfolders: `components/`, `pages/`, `data/`, or `util/`.
- All pages should use the `template` function from `rotr_app/template.py` to ensure consistent layout.
- Reuse and extend existing components where possible.
- Use type hints for all new functions and classes.
- Do not include comments in the code unless absolutely necessary; instead, use descriptive variable and function names.
- Follow PEP8 style guidelines.

## Component Usage
- Import shared UI elements from `rotr_app/components`.
- For new popups or modals, follow the pattern in `survey_popup.py`.
- For navigation changes, update `navbar.py` and the relevant JSON in `data/static/navbar.json`.

## Data
- Store static data in `rotr_app/data/static/` as JSON files.
- Use `json_loader.py` for loading static data.
- For Firestore integration, use `firestore.py`.

## Miscellaneous
- Keep all user-facing text in English.
- Do not include secrets or credentials in the repository.

---
For questions, contact the repository maintainer.
