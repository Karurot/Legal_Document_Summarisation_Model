import os
import pandas as pd

# Define the folders containing text files
independent_folder = r'D:\dataset\IN-Abs\test-data\judgement'  # Change to the path of your independent variables folder
dependent_folder = r'D:\dataset\IN-Abs\test-data\summary'      # Change to the path of your dependent variables folder

# Initialize lists to store data
independent_data = []
dependent_data = []

# Function to read and process text files
def process_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return content

# Function to traverse folders and process text files
def process_folder(folder_path, data_list):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                content = process_text_file(file_path)
                data_list.append((file_name, content))

# Process the folders
process_folder(independent_folder, independent_data)
process_folder(dependent_folder, dependent_data)

# Create Pandas DataFrames
independent_df = pd.DataFrame(independent_data, columns=['File Name', 'Independent Variable'])
dependent_df = pd.DataFrame(dependent_data, columns=['File Name', 'Dependent Variable'])

# Merge DataFrames based on 'File Name'
merged_df = pd.merge(independent_df, dependent_df, on='File Name', how='inner')

# Save the merged DataFrame to an Excel file
output_excel_path = r'C:\Users\DELL\Desktop\dataset_test.xlsx'  # Change to your desired output file path
merged_df.to_excel(output_excel_path, index=False)

print(f'Dataset saved to {output_excel_path}')
