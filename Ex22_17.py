#1 postlab
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [21, 25, 30],
    "Marks": [88.5, 92.0, 76.5]
})

print("Data Types of Columns:")
print(df.dtypes)


#2 postlab
import pandas as pd

# Sample DataFrame with missing values
df = pd.DataFrame({
    "Age": [20, 25, None, 30, None]
})

# Calculate mean of the column
mean_value = df["Age"].mean()

# Fill missing values with mean
df["Age"] = df["Age"].fillna(mean_value)

print("Data after filling missing values:")
print(df)
