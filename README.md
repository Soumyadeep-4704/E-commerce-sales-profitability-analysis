# E-commerce Sales & Profitability Analysis

This repository contains a simple Business Analyst project that analyzes e-commerce sales data. The goal is to extract data using SQL, transform it with Python, and visualize insights in an Excel dashboard.

### **Project Goal**

To analyze the 'Technology' product category from a sample sales dataset to answer key business questions:

1.  What is the profit margin for each product?
2.  Which products are the most and least profitable?
3.  How do sales trend month-over-month?

-----

## 🚀 Tech Stacks Used

  * **Python (Pandas):** For data cleaning, transformation, and feature engineering.
  * **SQL (SQLite):** For data storage and targeted data extraction.
  * **MS Excel:** For data visualization using Pivot Tables and Pivot Charts.

-----

## 🏃 How to Run This Project

1.  **Clone the repository:**

    ```bash
    git clone [your-repo-url]
    cd [your-repo-name]
    ```

2.  **Install dependencies:**
    *(Ensure you have Python 3 and pip installed)*

    ```bash
    pip3 install -r requirements.txt
    ```

    *(Note: Create a `requirements.txt` file and add `pandas` and `sqlalchemy` to it)*

3.  **Run the analysis script:**
    This single command will:

      * Create the mock `sales_data.csv`.
      * Load it into a `sales_db.db` SQLite database.
      * Run the SQL query and Python analysis.
      * Export the clean data.

    <!-- end list -->

    ```bash
    python3 analyze.py
    ```

4.  **View the Report:**

      * A new file named `final_report_data.csv` will be generated.
      * Open this file in **Microsoft Excel** to view the raw data for the dashboard.
      * *(Optional: You can include a screenshot of your Excel dashboard here)*

-----

## 📂 File Structure

```
.
├── analyze.py            # Main Python script to run the full ETL pipeline
├── requirements.txt      # Required Python libraries
├── sales_data.csv        # (Generated) Raw mock data
├── sales_db.db           # (Generated) SQLite database
├── final_report_data.csv # (Generated) The final, clean data for Excel
└── README.md             # This file
```

## 📊 Sample Dashboard Output
<img width="1470" height="809" alt="Screenshot 2025-10-23 at 8 22 30 PM" src="https://github.com/user-attachments/assets/a422b31c-3ce6-486a-9598-16f617d92f7c" />


