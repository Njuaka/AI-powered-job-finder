import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver
driver = webdriver.Chrome()  # or use any other WebDriver like Firefox, Edge, etc.




# Function to read companies from the text file
def read_companies(file_path):
    companies = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) >= 2:  # Ensure both name and registration number are present
                company_name = parts[0]
                registration_number = parts[1]
                companies.append((company_name, registration_number))
    return companies


# Fetch official website using Clearbit API or Google Search
def fetch_official_website(company_name, registration_number):
    try:
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        query = f"{company_name} official site"
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        # Capture the first search result
        results = driver.find_elements(By.XPATH, '//a')[:1]  # Get the first result
        if results:
            return results[0].get_attribute('href')
        else:
            return "N/A"  # If no results, return N/A
    except Exception as e:
        print(f"Error fetching website for {company_name}: {e}")
        return "N/A"

# Search LinkedIn for data-related jobs
def search_linkedin_jobs(company_name):
    try:
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        query = f"{company_name} data scientist OR data engineer OR data analyst OR Research scientist jobs site:linkedin.com"
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        links = driver.find_elements(By.XPATH, '//a')[:5]
        return [(link.text, link.get_attribute('href')) for link in links]
    except Exception as e:
        print(f"Error fetching LinkedIn jobs for {company_name}: {e}")
        return []

# Scrape company website for job postings
def scrape_website_jobs(website_url):
    try:
        response = requests.get(website_url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("a", href=True, text=lambda x: "career" in x.lower() or "job" in x.lower())
        return [(job.text.strip(), job["href"]) for job in jobs]
    except Exception as e:
        print(f"Error scraping {website_url}: {e}")
        return []