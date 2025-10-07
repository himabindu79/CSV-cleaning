import pandas as pd
import os

input_dir = "data"
output_dir = "cleaned"

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if file.endswith(".csv"):
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, f"cleaned_{file}")

        df = pd.read_csv(input_path)

        # Basic cleaning
        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)
        df.columns = df.columns.str.strip()

        df.to_csv(output_path, index=False)
        print(f"Cleaned file saved to: {output_path}")
