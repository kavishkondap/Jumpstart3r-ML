import pandas as pd

def delete_rows_with_empty_cells(input_file, output_file):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(input_file)
    
    # Drop rows with any empty cell
    df.dropna(axis=0, how='any', inplace=True)
    
    # Save the modified DataFrame to a new Excel file
    df.to_excel(output_file, index=False)

# Example usage
input_file = 'machineLearningData13.xlsx'  # Path to the input Excel file
output_file = 'machineLearningData14.xlsx'  # Path to save the modified Excel file

delete_rows_with_empty_cells(input_file, output_file)
