
# Task 4: Data Visualization using Matplotlib
# InternNova - Week 2

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("Datasets/cleaned_student_data.csv")

# 1. Bar Chart - Student Marks
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks - Bar Chart")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Task4_Visualization/bar_chart.png")
plt.show()

# 2. Line Chart - Student Attendance
plt.figure(figsize=(8, 5))
plt.plot(df["Name"], df["Attendance"], marker="o")
plt.xlabel("Student Name")
plt.ylabel("Attendance")
plt.title("Student Attendance - Line Chart")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Task4_Visualization/line_chart.png")
plt.show()

# 3. Histogram - Marks Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution - Histogram")
plt.tight_layout()
plt.savefig("Task4_Visualization/histogram.png")
plt.show()

# 4. Scatter Plot - Attendance vs Marks
plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance"], df["Marks"])
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.title("Attendance vs Marks - Scatter Plot")
plt.tight_layout()
plt.savefig("Task4_Visualization/scatter_plot.png")
plt.show()

print("All four visualizations created successfully!")
