Odisha RERA Projects Scraper
This Python-based automation script extracts details of the first six “Projects Registered” on the Odisha RERA project list page. It is designed to handle dynamic content rendered via JavaScript and collect critical information from each project’s detail page.

🎯 Objective
Extract the following fields from the first six project detail pages under the “Projects Registered” section on Odisha RERA:

RERA Registration Number

Project Name

Promoter Name (Company Name under the Promoter Details tab)

Promoter Address (Registered Office Address under the Promoter Details tab)

GST Number

⚙️ Technical Overview
The Odisha RERA portal is a Single Page Application (SPA) developed with Angular. All content loads dynamically through JavaScript.

To handle dynamic rendering, the scraper uses Selenium with undetected-chromedriver, effectively bypassing basic bot detection and ensuring full page load.

After extracting the target data, results are stored in a structured CSV file: odisha_rera_projects.csv.

📦 Requirements
Install dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt

Copy
Edit
undetected-chromedriver
selenium
beautifulsoup4
pandas
requests
🚀 Usage
Clone the repository and navigate to the project folder.

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the scraper:

bash
Copy
Edit
python rera_scraper.py
Output:
The file odisha_rera_projects.csv will be created in the same directory, containing all required project details.

📝 Notes
If the CSV file is empty or partially filled, try disabling headless mode by removing or commenting out the --headless option in the script. This allows better visibility and may help bypass loading delays or detection mechanisms.

The script includes modular functions, meaningful comments, and clear error handling to ensure maintainability and extendability.

All extracted fields have been validated against the source pages to ensure accuracy and completeness.

