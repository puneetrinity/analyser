
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_linkedin_jobs(query="Data Scientist", location="India"):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    search_url = f"https://www.linkedin.com/jobs/search/?keywords={query}&location={location}"
    driver.get(search_url)
    time.sleep(5)

    job_data = []

    cards = driver.find_elements(By.CLASS_NAME, "base-card")
    for card in cards[:10]:
        try:
            title = card.find_element(By.CLASS_NAME, "base-search-card__title").text
            company = card.find_element(By.CLASS_NAME, "base-search-card__subtitle").text
            loc = card.find_element(By.CLASS_NAME, "job-search-card__location").text
            url = card.find_element(By.TAG_NAME, "a").get_attribute("href")

            job_data.append({
                "title": title,
                "company": company,
                "location": loc,
                "url": url
            })
        except:
            continue

    driver.quit()
    return job_data
