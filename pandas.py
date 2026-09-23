
import pandas as pd

print(pd.__version__)

# ## 2. Series
#
# A **Series** is a one-dimensional labelled data structure.
#
# ### Example

marks = pd.Series([80, 75, 90, 65, 88])
print(marks)

# ### 🧪 Practice 1
# Create a Series called `ages` containing:
#
# `20, 21, 19, 22, 20`
#
# Then print the Series and print the value at index `2`.

# Write your code here
ages=pd.Series([20,21,19,22,20])
print(ages)
print(ages[2])



# ## 3. Create a DataFrame
#
# A **DataFrame** is a two-dimensional table with rows and columns.

data = {
    "Name": ["Arun", "Priya", "Rahul", "Divya", "Kiran"],
    "Department": ["AI", "DS", "AI", "CSE", "DS"],
    "Marks": [85, 92, 76, 88, 95],
    "Attendance": [90, 95, 75, 82, 98]
}

df = pd.DataFrame(data)
df

# ## 4. Inspect the DataFrame
#
# Try these commonly used commands.

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)

# ### 🧪 Practice 2
# 1. Display the first 3 rows.
# 2. Display the last 2 rows.
# 3. Find the number of rows and columns.
# 4. Display only the column names.

# Write your code here
print(df.head(3))
print(df.tail(2))
print(df.shape)
print(df.columns)


# ## 5. Selecting Columns
#
# ### One column

df["Name"]

# ### Multiple columns

df[["Name", "Marks"]]

# ### 🧪 Practice 3
# Display:
# 1. `Name` and `Department`
# 2. `Name`, `Marks`, and `Attendance`

# Write your code here.
df[["Name","Department"]]
df[["Name","Marks","Attendance"]]


# ## 6. Filtering Rows
#
# Find students who scored more than 80.

df[df["Marks"] > 80]


# ### 🧪 Practice 4
# Write code to find:
# 1. Students with marks greater than 85.
# 2. Students with attendance greater than 90.
# 3. Students from the `AI` department.
# 4. Students with marks less than 80.

# Write your code here
df[df["Marks"]>85]
df[df["Attendance"]>90]
df[df["Department"]=="AI"]

# ## 7. Multiple Conditions
#
# Use `&` for AND and `|` for OR.
#
# Example: marks greater than 80 AND attendance greater than 85.

df[(df["Marks"] > 80) & (df["Attendance"] > 85)]

# ### 🧪 Practice 5
# Find students who:
# 1. Have marks greater than 80 AND attendance greater than 90.
# 2. Are from AI OR DS department.

# Write your code here
df[(df["Marks"] > 80) & (df["Attendance"] > 90)]


# ## 8. Add and Update Columns
#
# Create a `Pass` column.

df["Pass"] = df["Marks"] >= 40
df


# ### 🧪 Practice 6
# 1. Create a `Bonus` column by adding 5 marks.
# 2. Create a `Final_Marks` column by adding `Marks + Bonus`.
# 3. Create a `High_Performer` column that is `True` when marks are 85 or above.

# Write your code here
df["Bonus"]=df["Marks"]+5
df["Final_Marks"]=df["Marks"]+df["Bonus"]
df["High_Performer"]=df["Marks"] >= 85
df

# ## 9. Missing Values
#
# Create a DataFrame containing a missing mark.

data_missing = {
    "Name": ["Arun", "Priya", "Rahul", "Divya"],
    "Marks": [85, None, 76, 90]
}

df_missing = pd.DataFrame(data_missing)
df_missing

# Useful methods:
#
# - `isnull()` → find missing values
# - `isnull().sum()` → count missing values
# - `fillna()` → replace missing values

print(df_missing.isnull())
print(df_missing.isnull().sum())

# ### 🧪 Practice 7
# Fill the missing mark using the **mean of the Marks column**.

# Write your code here
print(df_missing.fillna(df["Marks"].mean()))


# ## 10. Basic Statistics

print("Mean:", df["Marks"].mean())
print("Maximum:", df["Marks"].max())
print("Minimum:", df["Marks"].min())
print("Total:", df["Marks"].sum())
print(df["Marks"].describe())

# ### 🧪 Practice 8
# Find:
# 1. Average attendance
# 2. Highest attendance
# 3. Lowest attendance
# 4. Total marks

# Write your code here
print("Average attendance",df["Attendance"].mean())
print("Highest attendance",df["Attendance"].max())
print("Lowest attendance",df["Attendance"].min())
print("Total markse",df["Marks"].sum())


# ## 11. GroupBy
#
# Find the average marks for each department.

df.groupby("Department")["Marks"].mean()

# ### 🧪 Practice 9
# 1. Find the average attendance for each department.
# 2. Find the maximum marks for each department.
# 3. Count the number of students in each department.

# Write your code here
df.groupby("Department")["Attendance"].mean()
df.groupby("Department")["Marks"].max()
df.groupby("Department")["Name"].count()

# # 🚀 Mini Project: Student Performance Analyzer
#
# Use the following dataset.

project_data = {
    "Name": ["Arun", "Priya", "Rahul", "Divya", "Kiran", "Meena", "Vijay", "Anu"],
    "Department": ["AI", "DS", "AI", "CSE", "DS", "AI", "CSE", "DS"],
    "Marks": [85, 92, 67, 78, 95, 72, 88, 81],
    "Attendance": [90, 95, 75, 82, 98, 79, 91, 85]
}

students = pd.DataFrame(project_data)
students

# ## 🎯 Mini Project Tasks
#
# Solve these independently.
#
# 1. Display the first 5 students.
# 2. Display only `Name` and `Marks`.
# 3. Find students who scored more than 80.
# 4. Find students with attendance greater than 85.
# 5. Find students with marks > 80 AND attendance > 85.
# 6. Find the average marks.
# 7. Find the highest-scoring student.
# 8. Find average marks for each department.
# 9. Add a `Performance` column: `Excellent` if marks >= 90, otherwise `Good`.
# 10. Find the number of students in each department.

# 🚀 Write your mini-project solution here
students.head(5)
print(students["Name"])
print(students["Marks"])

print(students[students["Marks"]>80])

print(students[students["Attendance"]>85])

students[(students["Marks"]>80) & (students["Attendance"]>85)]

students["Marks"].mean()

students["highest-scoring"]=students["Marks"].max()
students[students["Marks"]==students["highest-scoring"]]

students.groupby("Department")["Marks"].mean()


students["Performance"]=(students["Marks"] >= 90).map({True: "Excellent", False: "Good"})
students

students.groupby("Department")["Name"].count()
