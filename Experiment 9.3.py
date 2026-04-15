#9.3

# Import the Spark session and math functions
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

# Start a Spark Session (The main engine)
spark = SparkSession.builder.appName("CanteenReport").getOrCreate()

# Load the csv file we just created
# header=True: Uses the first row as column names
# inferSchema=True: Automatically identifies numbers (integers)
df = spark.read.csv(r"D:\New Compressed (zipped) Folder\Python practice\sales.csv", header=True, inferSchema=True)

# Add a new column 'total' by multiplying quantity and price
df = df.withColumn("total", col("quantity") * col("price"))

# --- 1. Calculate Total Sales Per Day ---
print("--- Total Sales Per Day ---")
# Group data by date and sum the 'total' column
df.groupBy("date").agg(_sum("total").alias("Daily_Revenue")).show()

# # --- 2. Find the Most Sold Item (by Quantity) ---
print("--- Most Sold Item ---")
# Group by item, sum quantities, sort descending (highest first), take the top 1
df.groupBy("item").agg(_sum("quantity").alias("Total_Qty")) \
  .orderBy(col("Total_Qty").desc()).limit(1).show()

# # --- 3. Calculate Total Overall Revenue ---
# # Select the sum of the 'total' column and get the first result
total_revenue = df.select(_sum("total")).collect()[0][0]
print(f"TOTAL OVERALL REVENUE: {total_revenue}")

# Stop the Spark session to free up memory
spark.stop()

