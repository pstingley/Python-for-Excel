import pandas as pd

# Optional: Load an Excel file (can be skipped if not needed)
# print(pd.read_excel("./python-for-excel-1st-edition/xl/course_participants.xlsx"))

# Step 1: Create the DataFrame with initial custom index
data = [
    ["Mark", 55, "Italy", 4.5, "Europe"],
    ["John", 33, "USA", 6.7, "America"],
    ["Tim", 41, "USA", 3.9, "America"],
    ["Jenny", 12, "Germany", 9.0, "Europe"]
]

df = pd.DataFrame(
    data=data,
    columns=["name", "age", "country", "score", "continent"],
    index=[1001, 1000, 1002, 1003]
)
df.index.name = "user_id"

print("\nOriginal DataFrame with named index:")
print(df)

# Step 2: Replace index values (must match the number of rows)
df.index = [999, 1004, 1001, 1000]
df.index.name = "user_id"  # Reassign index name after changing index

print("\nDataFrame with replaced index:")
print(df)

# Step 3: Sort by new index (optional)
df = df.sort_index()

print("\nSorted by index:")
print(df)

# Step 4: Reset the index so user_id becomes a column and appears on the same row as other headers
df = df.reset_index()

print("\nFinal DataFrame with all column headers in one row:")
print(df)

print("\n")
df = df.sort_values(["continent", "age"])
print(df)
