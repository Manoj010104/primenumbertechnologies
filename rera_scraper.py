import time
import pandas as pd
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

BASE_URL = "https://rera.odisha.gov.in"
PROJECT_LIST_URL = f"{BASE_URL}/projects/project-list"

def get_driver():
    options = uc.ChromeOptions()
    # Comment out the next line to see the browser for debugging
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = uc.Chrome(options=options)
    return driver

def get_first_six_detail_urls(driver):
    driver.get(PROJECT_LIST_URL)
    time.sleep(10)  # Wait for JS to load the table
    # Scroll to bottom to trigger lazy loading if any
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Wait more in case of lazy loading

    soup = BeautifulSoup(driver.page_source, "html.parser")
    detail_urls = []
    for a in soup.find_all("a", href=True):
        if "/projects/project-details/" in a["href"]:
            detail_url = BASE_URL + a["href"]
            if detail_url not in detail_urls:
                detail_urls.append(detail_url)
        if len(detail_urls) == 6:
            break
    print("Found detail URLs:", detail_urls)
    return detail_urls

def get_project_details(detail_url):
    print(f"Scraping: {detail_url}")
    resp = requests.get(detail_url)
    soup = BeautifulSoup(resp.content, "html.parser")
    data = {}
    left_table = soup.find("table", class_="table table-bordered")
    if left_table:
        for row in left_table.find_all("tr"):
            th = row.find("th")
            td = row.find("td")
            if not th or not td:
                continue
            key = th.text.strip()
            value = td.text.strip()
            if "RERA Registration Number" in key or "Rera Regd. No" in key:
                data["Rera Regd. No"] = value
            elif "Project Name" in key:
                data["Project Name"] = value
    promoter_table = None
    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            th = row.find("th")
            if th and ("Company Name" in th.text or "Registered Office Address" in th.text or "GST" in th.text):
                promoter_table = table
                break
        if promoter_table:
            break
    if promoter_table:
        for row in promoter_table.find_all("tr"):
            th = row.find("th")
            td = row.find("td")
            if not th or not td:
                continue
            key = th.text.strip()
            value = td.text.strip()
            if "Company Name" in key:
                data["Promoter Name (Company Name)"] = value
            elif "Registered Office Address" in key:
                data["Address of the Promoter"] = value
            elif "GST" in key:
                data["GST No"] = value
    for key in [
        "Rera Regd. No", "Project Name", "Promoter Name (Company Name)",
        "Address of the Promoter", "GST No"
    ]:
        if key not in data:
            data[key] = "Not found"
    return data

def main():
    import requests  # Only import here to avoid issues if not needed above
    driver = get_driver()
    try:
        detail_urls = get_first_six_detail_urls(driver)
        all_data = []
        for url in detail_urls:
            details = get_project_details(url)
            all_data.append(details)
            time.sleep(1)
        df = pd.DataFrame(all_data)
        print(df)
        df.to_csv("odisha_rera_projects.csv", index=False)
        print("✅ Data saved to odisha_rera_projects.csv")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
