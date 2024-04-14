import pandas as pd

# Load the dataset de /dataset/productos.csv
df = pd.read_csv('dataset/productos.csv')

# Display the first few rows of the dataframe to understand its structure and content
df_info = {
    'columns': df.columns.tolist(),
    'head': df.head().to_dict(orient='records'),
    'description': df.describe(include='all'),
    'shape': df.shape
}

print(df_info)
