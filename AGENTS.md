# AGENTS.md

## Project Overview
- **Purpose:** Simple Python tool for generating secure, random passwords. Designed for educational use or as a base for more advanced projects.
- **Current State:** Now a Django project scaffolded with an app named `generator`.
- **Primary Language:** Python 3.x

## Key Files
- `main.py`: Legacy entry point from initial version. Not used in Django workflow.
- `manage.py`: Django project management script.
- `PasswordGenerator/`: Django project settings and URLs.
- `generator/`: Django app for password generation logic.
- `requirements.txt`: Python dependencies (now includes Django).
- `README.md`: Project description, requirements, and intended usage.

## Developer Workflows
- **Run the Django project:**
  - Use `python manage.py runserver` to start the development server.
  - Access at http://127.0.0.1:8000/ by default.
- **No build or test scripts** are present. Add tests in future as needed.

## Patterns & Conventions
- Keep code simple and easy to understand—prioritize readability for educational purposes.
- Place Django app logic in `generator/`.
- Use standard Django and Python idioms; no custom frameworks or patterns are in use.
- No external dependencies required beyond Django (as of now).

## Extending the Project
- Implement password generation logic in Django views within `generator/views.py`.
- If adding features (e.g., CLI, GUI, tests), create new files/modules as needed and update this guide.
- Document any new conventions or workflows in this file for future agents.

## Integration Points
- None currently. No external APIs, services, or libraries are integrated.

## Example: Adding Password Generation
- Define a Django view (e.g., `generate_password_view`) in `generator/views.py`.
- Use Python's `random` or `secrets` module for secure password generation.
- Wire up the view in `generator/urls.py` and include it in the project URLs.

---

**Update this file as the project evolves to keep agent guidance current.**
