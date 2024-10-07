import pandas as pd

file_path = 'C:\\Users\\stayl\\Downloads\\online+retail\\Online Retail.xlsx'
data = pd.read_excel(file_path)

data_clean = data.dropna(subset=['CustomerID', 'Description'])
data_clean = data_clean[data_clean['Quantity'] > 0]
data_clean = data_clean[data_clean['UnitPrice'] > 0]

def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

data_clean = remove_outliers(data_clean, 'Quantity')
data_clean = remove_outliers(data_clean, 'UnitPrice')

output_file = 'cleaned_data.csv'
data_clean.to_csv(output_file, index=False)

print(data_clean)

print(f"Data has been saved to {output_file}")
