# Odisha RERA Projects Scraper

## Objective

Extract the following fields from the first six project detail pages under the “Projects Registered” section on [Odisha RERA](https://rera.odisha.gov.in/projects/project-list):

- **RERA Registration Number**
- **Project Name**
- **Promoter Name** (Company Name under the Promoter Details tab)
- **Promoter Address** (Registered Office Address under the Promoter Details tab)
- **GST Number**

## Technical Overview

- The Odisha RERA portal is a Single Page Application (SPA) built with Angular; content loads dynamically through JavaScript.
- The scraper uses **Selenium** with **undetected-chromedriver** for full page load and bot bypass.
- The data is saved to `odisha_rera_projects.csv`.

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python rera_scraper.py
```

## Output

The file `odisha_rera_projects.csv` will be created in the same directory.

## Notes

- If the CSV is empty or incomplete, disable headless mode by setting `headless=False` in the script for debugging.
- The script includes robust waits and parsing for reliability.
