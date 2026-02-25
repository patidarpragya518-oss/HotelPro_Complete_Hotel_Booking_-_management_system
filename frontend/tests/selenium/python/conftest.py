import os
import time
import random
import string
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def random_email():
    return f"testuser_{int(time.time())}@example.com"


@pytest.fixture(scope="session")
def base_url():
    return os.environ.get("BASE_URL", "http://localhost:3000")


@pytest.fixture(scope="session")
def backend_url():
    return os.environ.get("BACKEND_URL", "http://localhost:5000")


@pytest.fixture(scope="session")
def create_test_user(backend_url):
    """Create a temporary customer via backend API for login tests.

    Returns dict with email and password. Adjust if your backend requires different fields.
    """
    email = random_email()
    password = "TestPass123!"
    payload = {"cusname": "Selenium Test", "cusemail": email, "phoneno": "0710000000", "password": password}
    try:
        resp = requests.post(f"{backend_url}/customer/", json=payload, timeout=5)
        # some backends return status 200 with JSON, others 201; we don't strictly assert here
    except Exception:
        pytest.skip("Could not reach backend to create test user; ensure backend is running at BACKEND_URL")

    return {"email": email, "password": password}


@pytest.fixture
def driver():
    """Start a Chrome WebDriver using webdriver-manager. Use HEADLESS=1 to run headless."""
    headless = os.environ.get("HEADLESS", "0") == "1"
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = ChromeService(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=chrome_options)
    yield drv
    try:
        drv.quit()
    except Exception:
        pass
