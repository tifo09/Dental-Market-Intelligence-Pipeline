# Dental Market Intelligence Dashboard 🦷📊

## Project Overview
I am a dentist and I wanted to analyze the dental supplies market (specifically the "Toothpick" e-commerce website). This end-to-end project covers web scraping the raw data, cleaning it, and building an interactive dashboard to track prices and instruments.

## Tech Stack
* **Web Scraping:** Python (`Scrapy`) to extract data from the website.
* **Data Cleansing:** Python (`Pandas` & `NumPy`) to clean and filter the data.
* **BI Visualization:** `Power BI` & `Power Query` to transform data and design the interactive dashboard.

## Data Pipeline Steps (What I Did)
* **Web Scraping:** I used `Scrapy` to scrape product URLs and names from the Toothpick online store, exporting the raw data into a file named `toothpick.csv`.
* **Data Cleaning:** I used `Pandas` to clean the dataset and programmatic rules to solve the "merged text" bug where categories were fused together (e.g., text clumping). Saved the output as `cleaned_toothpick.csv`.
* **Power Query Transformation:** Imported the clean data into `Power BI` and used Power Query to split the fused categories into separate, clean rows without damaging compound words.
* **Dashboard Design:** Designed a well-organized medical-themed dashboard displaying the total number of products and mapping the relationship between categories, brands, and prices.

## Dashboard Preview
Below is the final interactive dashboard showcasing tools, items, and average pricing by dental specialty:
<img width="1048" height="592" alt="Screenshot 2026-06-17 000456" src="https://github.com/user-attachments/assets/d3451254-a9c4-49de-9726-bb2def4c179f" />


## Key Insights Described
* **Specialty Pricing:** Analyzes and highlights the pricing differences for brands according to their specific categories (e.g., high-precision *Burs* vs. large equipment).
* **Brand Comparison:** Compares different pricing strategies for competitive brands within the exact same medical category.
