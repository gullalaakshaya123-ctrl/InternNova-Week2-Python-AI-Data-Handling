
# Task 3: Data Cleaning using Pandas
# InternNova - Week 2

import pandas as pd

# 1. Load the uncleaned dataset
df = pd.read_csv("Datasets/uncleaned_student_data.csv")

print("BEFORE DATA CLEANING:")
print(df)

# 2. Display dataset information
print("\nDataset Information:")
print(df.info())

# 3. Identify missing values
print("\nMissing Values:")
print(df.isnull())

# 4. Count missing values
print("\nMissing Values Count:")
print(df.isnull().sum())

# 5. Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].mean()
)

# 6. Identify duplicate records
print("\nDuplicate Records:")
print(df[df.duplicated()])

# 7. Remove duplicate records
df = df.drop_duplicates()

# 8. Correct data types
df["Age"] = df["Age"].round().astype(int)
df["Marks"] = df["Marks"].round().astype(int)
df["Attendance"] = df["Attendance"].round().astype(int)

# 9. Display cleaned dataset
print("\nAFTER DATA CLEANING:")
print(df)

# 10. Verify missing and duplicate values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Records After Cleaning:")
print(df.duplicated().sum())

# 11. Save cleaned dataset
df.to_csv("Datasets/cleaned_student_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
