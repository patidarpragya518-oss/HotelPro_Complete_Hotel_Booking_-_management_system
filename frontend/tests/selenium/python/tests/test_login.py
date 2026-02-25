import os
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def take_screenshot(driver, name="screenshot"):
    out_dir = os.environ.get("SCREENSHOT_DIR", "./screenshots")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{name}_{int(time.time())}.png")
    driver.save_screenshot(path)
    return path


def test_login_success(driver, base_url, create_test_user):
    """Positive test: use the created test user and assert redirect to /rooms"""
    email = create_test_user["email"]
    password = create_test_user["password"]

    driver.get(f"{base_url}/cuslogin")

    # Wait for email input
    wait = WebDriverWait(driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.ID, "form3Example3")))
    email_input.clear()
    email_input.send_keys(email)

    pwd_input = driver.find_element(By.ID, "form3Example4")
    pwd_input.clear()
    pwd_input.send_keys(password)

    # Click login button
    btn = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    btn.click()

    # Wait for redirect or location change
    try:
        wait.until(EC.url_contains("/rooms"))
        take_screenshot(driver, "login_success")
    except Exception as e:
        take_screenshot(driver, "login_success_failure")
        raise


def test_login_invalid_password(driver, base_url, create_test_user):
    """Negative test: wrong password should not redirect and should show alert (browser alert used in code)."""
    email = create_test_user["email"]
    driver.get(f"{base_url}/cuslogin")

    wait = WebDriverWait(driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.ID, "form3Example3")))
    email_input.clear()
    email_input.send_keys(email)

    pwd_input = driver.find_element(By.ID, "form3Example4")
    pwd_input.clear()
    pwd_input.send_keys("WrongPassword")

    btn = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    btn.click()

    # The app calls alert('unautherized user') on failure - handle possible alert
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        # take screenshot and accept
        take_screenshot(driver, "login_invalid_alert")
        alert.accept()
    except Exception:
        # If no alert, fallback: ensure URL did not change to /rooms
        assert "/rooms" not in driver.current_url
