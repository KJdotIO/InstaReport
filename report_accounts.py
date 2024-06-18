from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, WebDriverException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import time
import os
from multiprocessing import Process

# Function to close initial cookie popup
def close_cookie_popup(driver):
    try:
        print("Checking for initial cookie popup...")
        decline_cookies_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Decline optional cookies']"))
        )
        decline_cookies_button.click()
        print("Initial cookie popup closed.")
    except (NoSuchElementException, TimeoutException):
        print("No initial cookie popup found or it already closed.")

# Function to close post-login cookie popup
def close_post_login_cookie_popup(driver):
    try:
        print("Checking for post-login cookie popup...")
        decline_cookies_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='dialog']//button[@aria-label='Decline optional cookies']"))
        )
        decline_cookies_button.click()
        print("Post-login cookie popup closed.")
    except (NoSuchElementException, TimeoutException):
        print("No post-login cookie popup found or it already closed.")

def retry_click(element):
    retry_count = 0
    while retry_count < 3:
        try:
            element.click()
            return True
        except ElementClickInterceptedException:
            time.sleep(2)
            retry_count += 1
    print("Failed to click element after 3 tries.")
    return False

def report_user(driver, username):
    try:
        # Visit targets page
        print(f"Visiting profile: {username}")
        driver.get(f"https://www.instagram.com/{username}/")
        time.sleep(2)

        # Check if the account is public by looking for the "Similar accounts" button
        try:
            similar_accounts_button = driver.find_element(By.XPATH, "//svg[@aria-label='Similar accounts']")
            account_type = "Public"
            print("Account is public.")
        except NoSuchElementException:
            account_type = "Private"
            print("Account is private.")

        # Main reporting process
        try:
            options_button_div = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='button' and .//div[contains(@class, 'x6s0dn4 x78zum5 xdt5ytf xl56j7k')]]"))
            )
            # Using ActionChains to move to the element and click (the element is a div, not a button)
            actions = ActionChains(driver)
            actions.move_to_element(options_button_div).click().perform()
            print("Options button clicked successfully.")
            time.sleep(2) 

            print("Looking for the Report button...")
            report_button = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Report')]"))
            )
            report_button.click()
            print("Report button clicked successfully.")
            time.sleep(2)

            # Helper function to click button by index within div with class '_ac7r'
            def click_button_by_index(index):
                try:
                    report_modal_div = WebDriverWait(driver, 4).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "_ac7r"))
                    )
                    buttons = report_modal_div.find_elements(By.CLASS_NAME, "_abn2")
                    if len(buttons) > index:
                        buttons[index].click()
                        print(f"Button with index {index} clicked successfully.")
                        return True
                    else:
                        print(f"Button with index {index} not found.")
                        return False
                except (NoSuchElementException, TimeoutException, StaleElementReferenceException) as e:
                    print(f"Error finding or clicking button with index {index}: {e}")
                    return False

            # Click the buttons based on specified indices
            
            # Technically, you can change these values to whatever
            # indices you want, it'll change the report type
            # ive commented what each index does. Buttons are indexed by zero
            
            if click_button_by_index(1):  # Report Account
                time.sleep(1)
                if click_button_by_index(0):  # It's posting content that shouldn't be on Instagram (change to anything)
                    time.sleep(1)
                    if click_button_by_index(7):  # Bullying or harassment (change to anything)
                        time.sleep(1)
                        if click_button_by_index(2):  # Someone else (change to anything)
                            time.sleep(1)
                            
                            try:
                                print("Looking for the submit button within the div '_acgz'...")
                                submit_div = WebDriverWait(driver, 4).until(
                                    EC.presence_of_element_located((By.CLASS_NAME, "_acgz"))
                                )
                                inner_div = submit_div.find_element(By.XPATH, ".//div[contains(@class, 'x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xw7yly9 x1yztbdb x1pi30zi x1swvt13 x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1')]")
                                submit_button = inner_div.find_element(By.XPATH, ".//button[contains(@class, '_acan _acap _acas _aj1- _ap30')]")
                                retry_click(submit_button)
                                print("Submit button clicked successfully.")
                            except (NoSuchElementException, TimeoutException, StaleElementReferenceException) as e:
                                print(f"Error finding or clicking submit button: {e}")
                                return

                            print("Waiting for confirmation and closing the dialog...")
                            close_button = WebDriverWait(driver, 4).until(
                                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Close')]"))
                            )
                            close_button.click()
                            print("Dialog closed successfully.")
                            time.sleep(5)
                        else:
                            print("Failed to click 'Someone else' button.")
                    else:
                        print("Failed to click 'Bullying or harassment' button.")
                else:
                    print("Failed to click 'It's posting content that shouldn't be on Instagram' button.")
            else:
                print("Failed to click 'Report Account' button.")
        except (NoSuchElementException, TimeoutException) as e:
            print("An error occurred during the reporting process.")
            print(f"Message: {e}")

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error occurred while processing user {username}")
        print(f"Message: {e}")

def login(driver, account):
    try:
        print(f"Logging in with account: {account[0]}")
        driver.get("https://www.instagram.com/accounts/login/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

        close_cookie_popup(driver)

        driver.find_element("name", "username").send_keys(account[0])
        driver.find_element("name", "password").send_keys(account[1])

        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        retry_click(submit_button)
        print("Waiting for post-login elements to load...")
        time.sleep(2) 

        close_post_login_cookie_popup(driver)
    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error occurred during login for account {account[0]}")
        print(f"Message: {e}")

def report_for_account(username, account, options):
    try:
        driver = webdriver.Chrome(options=options)
        print(f"WebDriver initialized successfully for account: {account[0]}")

        login(driver, account)
        while True:
            report_user(driver, username)
            print("Refreshing the page...")
            driver.refresh()
            print("Page refreshed. Waiting to respect rate limits...")
            time.sleep(1) 
    except WebDriverException as e:
        print(f"Error: WebDriver initialization failed for account: {account[0]}")
        print(e)
    finally:
        driver.quit()
        print(f"Finished processing for account: {account[0]}")

def report_accounts(username, accounts_file):
    if not os.path.isfile(accounts_file):
        print(f"Error: The file {accounts_file} does not exist.")
        return

    options = Options()
    options.add_argument("--disable-notifications")

    print(f"Reading account credentials from {accounts_file}...")
    with open(accounts_file, "r") as file:
        accounts = [line.strip().split(":") for line in file]
    print(f"Found {len(accounts)} accounts.")

    processes = []
    for account in accounts:
        p = Process(target=report_for_account, args=(username, account, options))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

if __name__ == '__main__':
    report_accounts("", "acc.txt")
