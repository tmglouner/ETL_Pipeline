import pandas as pd

# Step 1: Load the CSV file into a DataFrame
input_file_path = '/Users/thomasglouner/Downloads/data.csv'  # Replace with your actual input file path

try:
    df = pd.read_csv(input_file_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(input_file_path, encoding='ISO-8859-1')

# Step 2: Filter rows where 'Country' is 'USA'
usa_df = df[df['Country'] == 'Hong Kong']

# Step 3: Save the filtered DataFrame to a new CSV file
output_file_path = '/Users/thomasglouner/Documents/data/hk_data.csv'
usa_df.to_csv(output_file_path, index=False)

print(f"Filtered data has been saved to {output_file_path}")