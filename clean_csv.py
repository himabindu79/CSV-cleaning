import pandas as pd
import os
import glob

def clean_csv(file_path):
    """Clean a single CSV file"""
    print(f"Cleaning {file_path}...")
    
    # Read CSV
    df = pd.read_csv(file_path)
    
    # Basic cleaning operations
    # 1. Remove duplicate rows
    df = df.drop_duplicates()
    
    # 2. Strip whitespace from column names
    df.columns = df.columns.str.strip()
    
    # 3. Remove rows where all values are null
    df = df.dropna(how='all')
    
    # 4. Strip whitespace from string columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip() if df[col].dtype == 'object' else df[col]
    
    return df

def main():
    # Create cleaned_data directory if it doesn't exist
    os.makedirs('cleaned_data', exist_ok=True)
    
    # Find all CSV files in data directory
    csv_files = glob.glob('data/*.csv')
    
    if not csv_files:
        print("No CSV files found in data/ directory")
        return
    
    # Clean each CSV file
    for csv_file in csv_files:
        try:
            cleaned_df = clean_csv(csv_file)
            
            # Save cleaned file
            filename = os.path.basename(csv_file)
            output_path = os.path.join('cleaned_data', filename)
            cleaned_df.to_csv(output_path, index=False)
            
            print(f"✓ Cleaned {filename} - Rows: {len(cleaned_df)}")
        except Exception as e:
            print(f"✗ Error cleaning {csv_file}: {str(e)}")
    
    print("\nCleaning completed!")

if __name__ == "__main__":
    main()