# Selenium tests for Hotel-Management-System-Mern-Stack (frontend)

This folder contains pytest-based Selenium tests (Python) for the frontend login flow.

Quick start
1. Create a Python virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Start backend and frontend servers used by the app (defaults used in tests):
- Frontend: http://localhost:3000
- Backend:  http://localhost:5000

3. Run tests:

```powershell
pytest -q
```

Notes
- Tests default to Chrome and will use webdriver-manager to fetch a driver.
- You can run in headless mode by setting the environment variable `HEADLESS=1` before running pytest.
- If your frontend runs on a different port, set environment variable `BASE_URL` (e.g. `http://localhost:3001`).
