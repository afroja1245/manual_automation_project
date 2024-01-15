from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker()

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    print("Launching Browser")


    yield driver
    driver.quit()

test_data = [
    ("anthonygrimes@example.org", "GT_VVjpv^9", "Account Login"),
    ("Demo@123",  "GT_VVjpv^9",  "Account Login"),   #invalid, valid
    ("anthonygrimes@example.org", "VVjpv^9", "Account Login"), #valid, invalid
    ("virtual_user", "Mu_:>yt65", "Account Login"),  #invalid, invalid
    ("123467",  "GT_VVjpv^9",  "Account Login"),   #invalid, valid
    ("123467",  "123456^9",  "Account Login"),   #invalid, invalid
    (" ",  " ", "Account Login")                     #empty field, empty field

]



@pytest.mark.parametrize("username, password, expected_title",test_data)
def test_login(driver, username, password, expected_title):
    # open url
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

    # Verify Home page open successfully
    actual_title = driver.title
    assert expected_title == actual_title

    # find email
    username_email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))
    # username_email = driver.find_element(By.NAME, "email")
    username_email.send_keys(username)
    # Actual email  anthonygrimes@example.org

    # find password
    username_password = driver.find_element(By.NAME, "password")
    username_password.send_keys(password)  # Actual password  GT_VVjpv^9
    time.sleep(5)

    # Submit login button
    login_button = driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[value='Login']")
    # click Submit button
    login_button.click()
    time.sleep(3)

    # verify Login using url
    expected_url = "https://tutorialsninja.com/demo/index.php?route=account/account"
    actual_url = driver.current_url

    if actual_url == expected_url:
        print(f"Login successfully.")
    else:
    # if Error Occurred

        verify_error = driver.find_element(By.CSS_SELECTOR, "div#account-login > .alert.alert-danger.alert-dismissible").is_displayed()
        assert verify_error
        print("error occurred")




