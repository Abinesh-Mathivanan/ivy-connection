import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os
import ssl

class LinkedinBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # ... Other methods (login, connect) ...

    def parse_and_store_ivy_league_students(self, csv_filename):
        # Perform a LinkedIn search for Ivy League students
        search_query = "Ivy League student"
        search_url = f"https://www.linkedin.com/search/results/people/?keywords={search_query}"

        # Navigate to the search results page
        self.driver.get(search_url)

        # Create or open the CSV file for writing
        with open(csv_filename, mode='w', newline='') as csvfile:
            fieldnames = ['Name', 'Gender', 'University', 'Profile URL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the CSV header row
            writer.writeheader()

            while True:
                # Extract profile information from the current page
                profiles = self.driver.find_elements(By.CLASS_NAME, 'search-result__info')

                for profile in profiles:
                    try:
                        name = profile.find_element(By.TAG_NAME, 'span').text.strip()
                        profile_url = profile.find_element(By.TAG_NAME, 'a').get_attribute('href')

                        # Visit the profile page to extract more details (gender and university)
                        self.driver.get(profile_url)
                        time.sleep(2)  # Add a short delay for the page to load

                        # Extract gender (if available)
                        gender_element = self.driver.find_element(By.CLASS_NAME, 'pv-text-details__left-panel')
                        gender = gender_element.text.strip() if gender_element else "Not specified"

                        # Extract university (assuming it's mentioned in the "Education" section)
                        education_section = self.driver.find_element(By.ID, 'education-section')
                        university_element = education_section.find_element(By.TAG_NAME, 'h3')
                        university = university_element.text.strip() if university_element else "University not specified"

                        # Write profile information to the CSV file
                        writer.writerow({'Name': name, 'Gender': gender, 'University': university, 'Profile URL': profile_url})

                    except Exception as e:
                        print(f"Error parsing profile: {str(e)}")

                # Check for the presence of a "Next" button for pagination
                next_button = self.driver.find_element(By.XPATH, '//button[@aria-label="Next"]')
                if not next_button.is_enabled():
                    break  # No more pages to navigate

                # Click the "Next" button to go to the next page
                next_button.click()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LinkedIn Automation Bot for Ivy League Students')
    parser.add_argument('--username', help='LinkedIn_UserId', required=True)
    parser.add_argument('--password', help='LinkedIn_Password', required=True)
    args = parser.parse_args()
    username = args.username
    password = args.password

    bot = LinkedinBot(username, password)
    ssl._create_default_https_context = ssl._create_unverified_context
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    bot.driver = webdriver.Chrome(options=chrome_options)
    
    bot.login(bot.driver)
    csv_filename = "females.csv"  # Specify the CSV filename

    bot.parse_and_store_ivy_league_students(csv_filename)
    bot.driver.quit()
    print(f"Ivy League student profiles parsed and stored in '{csv_filename}'.")
