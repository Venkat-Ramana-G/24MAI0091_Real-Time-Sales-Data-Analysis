import pandas as pd
import numpy as np

# Sample data to create the dataset
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Store ID': np.random.randint(1, 5, size=100),
    'Product ID': np.random.randint(1, 20, size=100),
    'Units Sold': np.random.randint(1, 100, size=100).astype(float),
    'Sales Amount': np.random.uniform(50, 500, size=100).astype(float),
    'Discount Applied': np.random.choice([5, 10, 15, np.nan], size=100, p=[0.3, 0.3, 0.3, 0.1]),
    'Customer Segment': np.random.choice(['Regular', 'Premium', 'Wholesale'], size=100)
}

# Convert some values to NaN for testing imputation
data['Units Sold'][np.random.choice(data['Units Sold'].shape[0], 10, replace=False)] = np.nan
data['Sales Amount'][np.random.choice(data['Sales Amount'].shape[0], 15, replace=False)] = np.nan

# Create DataFrame
sales_data = pd.DataFrame(data)

# Save dataset to a CSV file
sales_data.to_csv('sales_data_final.csv', index=False)
