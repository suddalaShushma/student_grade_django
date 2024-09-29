import pandas as pd

# Specify the path to your CSV file
csv_file_path = r'C:\Users\sushma suddala\Desktop\mysite\students_record.csv'

# List of encodings to try
encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'windows-1252']

for encoding in encodings:
    try:
        # Attempt to read the CSV file with the specified encoding
        df = pd.read_csv(csv_file_path, encoding=encoding)
        print(f"Successfully read the file with encoding: {encoding}")
        print(df.head())  # Display the first few rows
        break  # Exit the loop if successful
    except Exception as e:
        print(f"Error reading with encoding {encoding}: {e}")
