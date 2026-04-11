#8.2

import pandas as pd
import numpy as np

# 1. Load the dataset
df = pd.read_csv(r"D:\New Compressed (zipped) Folder\Python practice\Sales Data.csv")

# 2. Calculate Total Revenue for each row
# Revenue = Quantity * Unit Price
df['Total_Revenue'] = df['quantity'] * df['unit_price']

print("\n--- Sales Data ---")
print(df)

# # 3. Basic Analysis using Pandas and Numpy
print("\n--- Sales Summary ---")

# Calculate overall total revenue
total_sales = np.sum(df['Total_Revenue'])
print(f"Total Revenue: ₹{total_sales:.2f}")

# # Find the product with the highest quantity sold
# groupby(): This is the most powerful tool for analysis. It gathers all rows belonging to a specific category (like 'East' or 'North') so you can sum or average them.
# The .idxmax() method in Pandas stands for "Index of Maximum." While the .max() function tells you what the highest value is, .idxmax() tells you the label (index) where that maximum value is located.

top_product = df.groupby('product_id')['quantity'].sum().idxmax()
print(f"Top Selling Product (by Quantity): {top_product}")

# # 4. Grouping Data by Region
region_analysis = df.groupby('region')['Total_Revenue'].sum()
print("\n--- Revenue by Region ---")
print(region_analysis)

# # 5. Average order value using Numpy
avg_order = np.mean(df['Total_Revenue'])
print(f"\nAverage Order Value: ₹{avg_order:.2f}")