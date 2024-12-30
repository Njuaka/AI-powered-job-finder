from utils import *
from job_scraper import *


input_file = os.path.join(get_root_dir(), "data", "companies.txt")
output_file = os.path.join(get_root_dir(), "data", "job_search_results.csv")

def main():
    try:
        # Read companies and initialize results
        companies = read_companies(input_file)
        driver = webdriver.Chrome()  # Ensure ChromeDriver is installed
        driver.maximize_window()
        results = []

        # Process each company
        for company_name, registration_number in companies:
            # Fetch official website
            official_website = fetch_official_website(company_name, registration_number)
        
            # Search LinkedIn jobs
            linkedin_jobs = search_linkedin_jobs(company_name)
            for title, link in linkedin_jobs:
                results.append((company_name, registration_number, "LinkedIn", title, link))
        
            # Scrape official website
            if official_website != "N/A":
                website_jobs = scrape_website_jobs(official_website)
                for title, link in website_jobs:
                    results.append((company_name, registration_number, "Official Website", title, link))

        # Save all results to CSV
        save_to_csv(results, output_file)
        print(f"Data job search results saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()
    
    
if __name__ == "__main__":
    main()