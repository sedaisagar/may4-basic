import pandas as pd

# df = pd.read_csv("./media/test.csv")
df = pd.read_excel("./media/demography.xlsx", sheet_name="Second")

# print(df.head(), "\n", df.tail())
# print("="*50)
# print(df.info())
# print("="*50)

# df = pd.DataFrame(
#     {
#         "Name": [
#             "Braund, Mr. Owen Harris",
#             "Allen, Mr. William Henry",
#             "Bonnell, Miss Elizabeth",
#         ],
#         "Age": [22, 35, 58],
#         "Sex": ["male", "male", "female"],
#     }
# )

# df.to_excel("./media/demography.xlsx", sheet_name="Second", index=False)
# df.to_csv("./media/demography.csv", index=False)


# print(df.describe())

# print(df[["Age", "Name"]])

above_20 = df[df["Age"] > 20]
below_20 = df[df["Age"] < 20]


# print(above_20)
# print(below_20)

df["Age Group"] = df["Age"].apply(lambda x: "Below 15" if x < 15 else "Below 20" if x < 20 else "Above 20")


# loc, iloc
# LOC -> label based indexing
# ILOC -> integer based indexing

# print(df.loc[0:4, ["Age"]])

print(df.iloc[0:4, 0:3])


# Create a dataframe with following student information:
# Name, Age, Marks

# Disply:
# Only the name column of student
# Student who scored more than 75 marks

# Add a new column "Grade" to the dataframe with following conditions:
# Marks >= 80 -> Excellent
# Marks >= 60 and < 80 -> Good
# Marks < 60 -> Needs Improvement