
# Task 2: Pandas and Dataset Handling
# InternNova - Week 2

import pandas as pd

# 1. Create a DataFrame
data = {
    "Name": ["Anu", "Balu", "Chandu"],
    "Marks": [85, 78, 92]
}

df = pd.DataFrame(data)

print("Created DataFrame:")
print(df)

# 2. Load CSV dataset
df = pd.read_csv("Datasets/student_performance.csv")

print("\nComplete Dataset:")
print(df)

# 3. Display first five rows
print("\nFirst Five Rows:")
print(df.head())

# 4. Display last five rows
print("\nLast Five Rows:")
print(df.tail())

# 5. Check rows and columns
print("\nDataset Shape:")
print(df.shape)

# 6. Check data types
print("\nData Types:")
print(df.dtypes)

# 7. Basic statistical information
print("\nStatistical Information:")
print(df.describe())

# 8. Select specific columns
print("\nStudent Names and Marks:")
print(df[["Name", "Marks"]])

# 9. Filter rows based on a condition
print("\nStudents Scoring More Than 80:")
print(df[df["Marks"] > 80])
