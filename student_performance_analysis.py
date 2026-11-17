
# Task 5: Student Performance Data Analysis
# InternNova - Week 2

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("Datasets/uncleaned_student_data.csv")

print("STUDENT PERFORMANCE DATA ANALYSIS")

# 2. Display dataset information
print("\nOriginal Dataset:")
print(df)

print("\nDataset Information:")
df.info()

# 3. Identify important columns
print("\nImportant Columns:")
print(df[["Name", "Marks", "Attendance"]])

# 4. Data Cleaning
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing numerical values using column means
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].mean()
)

# Remove duplicate records
df = df.drop_duplicates()

print("\nCleaned Dataset:")
print(df)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())

# Save cleaned mini project dataset
df.to_csv(
    "Task5_Mini_Project/mini_project_cleaned_data.csv",
    index=False
)

# 5. Data Analysis
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

# Assuming 50 marks is the passing score
passed_students = (df["Marks"] >= 50).sum()
failed_students = (df["Marks"] < 50).sum()

print("\nSTUDENT PERFORMANCE ANALYSIS RESULTS")
print("Average Marks:", round(average_marks, 2))
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Number of Students Passed:", passed_students)
print("Number of Students Failed:", failed_students)

# 6. Visualization 1 - Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Performance - Bar Chart")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Task5_Mini_Project/student_marks.png")
plt.show()

# 7. Visualization 2 - Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Student Marks Distribution")
plt.tight_layout()
plt.savefig("Task5_Mini_Project/marks_distribution.png")
plt.show()

# 8. Visualization 3 - Pass and Fail Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(
    [passed_students, failed_students],
    labels=["Passed", "Failed"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Student Pass and Fail Analysis")
plt.savefig("Task5_Mini_Project/pass_fail_chart.png")
plt.show()

print("\nAll three charts created successfully!")
print("Mini project completed successfully!")
