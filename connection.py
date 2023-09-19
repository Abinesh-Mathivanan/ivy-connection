import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import os
import ssl

class LinkedinBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, driver):
        driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        uname_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]')))
        uname_field.send_keys(self.username)
        password_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        password_field.send_keys(self.password)
        login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')))
        login_button.click()
        time.sleep(5)

    def get_id_list(self, file_name='university_females.csv'):
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        with open(file_path, newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            id_links = []
            for row in data:
                university = row[0]
                gender = row[1]
                id_link = row[2]

                if gender.lower() == 'female' and any(keyword in university.lower() for keyword in ['harvard', 'cambridge', 'oxford', 'mit', 'your_other_university_keywords']):
                    if 'linkedin' in id_link:
                        if 'https:' not in id_link:
                            id_link = 'https:' + id_link
                        id_links.append(id_link)
            return id_links

    def connect(self, id_links, driver):
        for id_link in id_links:
            driver.get(id_link)

            try:
                connect_button = driver.find_element(By.XPATH, '//button[@aria-label="Connect with this person"]')
                connect_button.click()
                time.sleep(3)
            except NoSuchElementException:
                print("Connect button not found for:", id_link)
            except Exception as e:
                print(e)
                pass

        print(f"Sent {len(id_links)} connection requests to eligible profiles.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LinkedIn Automation Bot for University Females')
    parser.add_argument('--username', help='LinkedIn_UserId', required=True)
    parser.add_argument('--password', help='LinkedIn_Password', required=True)
    args = parser.parse_args()
    username = args.username
    password = args.password

    bot = LinkedinBot(username, password)
    ssl._create_default_https_context = ssl._create_unverified_context
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)
    
    bot.login(driver)
    id_links = bot.get_id_list()
    print(f"Found {len(id_links)} eligible profiles.")
    bot.connect(id_links, driver)
    driver.quit()
    print('Done')
