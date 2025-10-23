import pandas as pd
import sqlite3
import os

def create_mock_data():
    """Creates a mock sales_data.csv file in the current directory."""
    print("Creating mock sales_data.csv...")
    
    # Define the raw data
    data = """Order_ID,Order_Date,Category,Product_Name,Sales,Profit
1001,2025-07-05,Technology,Laptop,1200,180
1002,2025-07-08,Office,Binders,20,5
1003,2025-07-15,Technology,Monitor,350,60
1004,2025-08-02,Technology,Mouse,40,15
1005,2025-08-10,Furniture,Chair,150,25
1006,2025-08-12,Technology,Laptop,1200,180
1007,2025-08-20,Office,Pens,10,3
1008,2025-09-01,Technology,Keyboard,80,22
1009,2025-09-05,Technology,Monitor,350,60
1010,2025-09-10,Furniture,Table,400, -50
1011,2025-09-18,Technology,Headphones,120,30
"""
    # Write the data to a file
    with open("sales_data.csv", "w") as f:
        f.write(data)
    print("File created successfully.")

def run_analysis():
    """
    Main analysis pipeline:
    1. Loads CSV into Pandas.
    2. Loads Pandas data into an SQL database (SQLite).
    3. Runs an SQL query to extract *only* Technology products.
    4. Cleans and transforms the extracted data using Pandas.
    5. Saves the final, clean data to a new CSV for Excel.
    """
    
    # --- Part 1: Load Data & Create Database ---
    try:
        df = pd.read_csv("sales_data.csv")
    except FileNotFoundError:
        print("Error: sales_data.csv not found.")
        return

    # Create a connection to an in-memory SQL database
    # 'sales_db.db' will be created in your folder
    db_conn = sqlite3.connect("sales_db.db")
    
    # Use pandas .to_sql() to create a table named 'sales'
    # if_exists='replace' means it will overwrite the table every time
    df.to_sql('sales', db_conn, if_exists='replace', index=False)
    print("Data loaded into SQL database 'sales_db.db'.")

    # --- Part 2: SQL (Data Extraction) ---
    # This is the BA part: "I only want to see 'Technology' products."
    sql_query = """
    SELECT 
        Order_Date,
        Product_Name,
        Sales,
        Profit
    FROM 
        sales
    WHERE 
        Category = 'Technology'
    """
    
    print("Running SQL query to extract 'Technology' sales...")
    # Use pandas to read the result of the SQL query directly into a new DataFrame
    tech_df = pd.read_sql_query(sql_query, db_conn)
    
    # Close the database connection
    db_conn.close()

    # --- Part 3: Python (Data Cleaning & Transformation) ---
    print("Cleaning and transforming data using Python (Pandas)...")
    
    # Check for missing values (a good BA always checks)
    # print(tech_df.isnull().sum()) 
    
    # Feature Engineering: Create the 'Profit_Margin' column (Manager's request)
    # This is an "advanced" fresher step!
    tech_df['Profit_Margin'] = (tech_df['Profit'] / tech_df['Sales']) * 100
    
    # Format the margin to 2 decimal places for easier reading
    tech_df['Profit_Margin'] = tech_df['Profit_Margin'].round(2)
    
    # Handle dates: Convert 'Order_Date' string to a real datetime object
    tech_df['Order_Date'] = pd.to_datetime(tech_df['Order_Date'])
    
    # Feature Engineering: Extract 'Order_Month' for trend analysis
    tech_df['Order_Month'] = tech_df['Order_Date'].dt.strftime('%Y-%m (Month)') # Formats as '2025-07 (Month)'

    # --- Part 4: Export for Excel ---
    output_filename = "final_report_data.csv"
    tech_df.to_csv(output_filename, index=False)
    
    print(f"\n✅ Success! Analysis complete.")
    print(f"Final clean data has been exported to: {output_filename}")
    print("Next step: Open this file in Excel!")

# --- Main execution ---
if __name__ == "__main__":
    # First, create the mock data file
    create_mock_data()
    
    # Second, run the full analysis pipeline
    run_analysis()