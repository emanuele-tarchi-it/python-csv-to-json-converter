__version__ = "1.0.0"
__author__ = "Emanuele Tarchi"

import pandas as pd
import json
import os

def csv_to_json(input_file, output_file="output.json", indent=4, columns=None):
    """
    Converts a CSV file to a formatted JSON file with custom column selection.
    """
    # 1. Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' was not found.")
        return

    try:
        print(f"--- Starting Conversion ---")
        print(f"Loading: {input_file}...")
        
        # 2. Load the data
        df = pd.read_csv(input_file)

        # 3. Filter specific columns if the user requested them
        if columns:
            # Check if columns actually exist in the CSV to avoid crashes
            existing_cols = [c for c in columns if c in df.columns]
            print(f"Filtering specific columns: {existing_cols}")
            df = df[existing_cols]

        # 4. Convert dataframe to a list of dictionaries
        data = df.to_dict(orient="records")

        # 5. Save to JSON with UTF-8 support for international characters
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)

        print(f"Success! {len(data)} records converted.")
        print(f"Output saved as: {output_file}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    # Rename 'sample.csv' to your actual file
    csv_to_json(
        input_file="sample.csv", 
        output_file="data_export.json", 
        indent=2,
        columns=None  # Or list columns: ["Name", "City"]
    )
