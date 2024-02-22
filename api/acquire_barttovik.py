# Import Packages
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Fetches the HTML content from the given URL
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
        return None

# Finds a table in the HTML content based on the specified table ID
def find_tables(html_content, table_id):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', {'id': table_id})
    return table

# Finds all tables on page, returns list 
def find_all_tables(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')
    return tables
    
# Extracts the contents of the given table and returns as a list of lists  
def extract_table_data(table):
    table_data = []
    if table:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['th', 'td'])
            row_data = [col.text.strip() for col in cols]
            table_data.append(row_data)
    return table_data

# Exports The Tables Present On The Page to .csv
def export_barttovic(url: str):
    html_content = get_html(url)
    if html_content:
        tables = find_all_tables(html_content)
        
        dfs = []
        for table in tables:
            table_data = extract_table_data(table)
            table_df = pd.DataFrame(table_data)
            dfs.append(table_df)
            
        df = pd.concat(dfs, ignore_index=True)
        return df
    else:
        print("Export of barttovic data did not yield table.")
    