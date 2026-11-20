
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset
# df = pd.read_csv("vegetables Dataset.csv")
# print(df.head())
# df.to_excel("Veggies.xlsx", index=False)
# print("Saved Successfully!")

df = pd.read_excel("Vegetables.xlsx")


# DATASET INFORMATION

# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.columns)
# print(df.isnull().sum())
# print(df.duplicated().sum())


# UNIQUE VALUES

print("Vegetable Name:")
print(df['Name'].unique())

print("Category:")
print(df['Category'].unique())

print("Season:")
print(df['Season'].unique())


# VALUE COUNTS

print("\nCategory Count:")
print(df["Category"].value_counts())

print("\nSeason Count:")
print(df["Season"].value_counts())


# PRICE DATA CLEANING

# Remove $ symbol from Price column
df["Price (per kg)"] = (
    df["Price (per kg)"]
    .astype(str)
    .str.replace("$", "", regex=False)
)

# Convert Price into numeric format
df["Price (per kg)"] = pd.to_numeric(
    df["Price (per kg)"], errors="coerce"
)

print("\nPrice Details:")
print("Minimum Price:", df["Price (per kg)"].min())
print("Maximum Price:", df["Price (per kg)"].max())
print("Average Price:", df["Price (per kg)"].mean())

print("\nMissing Price Values:")
print(df["Price (per kg)"].isnull().sum())

print("\nData Types:")
print(df.dtypes)


# CHARTS


# 1. Histogram - Price Distribution

plt.figure(figsize=(8, 5))
plt.hist(df["Price (per kg)"].dropna(), bins=10)
plt.title("Vegetable Price Distribution")
plt.xlabel("Price per kg")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("price_histogram.png", dpi=300)
plt.show()


# 2. Scatter Plot - Vegetable vs Price

plt.figure(figsize=(12, 7))

colors = plt.cm.tab20(np.linspace(0, 1, len(df)))

plt.scatter(
    df['Name'],
    df['Price (per kg)'],
    c=colors
)

plt.title("Vegetable vs Price")
plt.xlabel("Vegetable Name")
plt.ylabel("Price per kg")
plt.xticks(rotation=90, fontsize=8)
plt.tight_layout()
plt.savefig("veg_vs_price.png", dpi=500)
plt.show()


# 3. Line Chart - Vegetable vs Price

plt.figure(figsize=(12, 7))

plt.plot(
    df['Name'],
    df['Price (per kg)'],
    marker='o'
)

plt.title("Vegetable vs Price")
plt.xlabel("Vegetable Name")
plt.ylabel("Price per kg")
plt.xticks(rotation=90, fontsize=8)
plt.grid(True)
plt.tight_layout()
plt.savefig("veg_vs_price_linechart.png", dpi=500)
plt.show()


# 4. Top 10 Expensive Vegetables

top = df.sort_values(
    by="Price (per kg)",
    ascending=False
).head(10)

plt.figure(figsize=(10, 7))

colors = plt.cm.tab10(np.arange(len(top)))

plt.bar(
    top["Name"],
    top["Price (per kg)"],
    color=colors
)

plt.title("Top 10 Expensive Vegetables")
plt.xlabel("Vegetable Name")
plt.ylabel("Price per kg")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("veg_barchart.png", dpi=300)
plt.show()


# 5. Category-wise Average Price

category_price = df.groupby("Category")["Price (per kg)"].mean()

plt.figure(figsize=(10, 6))

colors = plt.cm.Set3(
    np.linspace(0, 1, len(category_price))
)

plt.bar(
    category_price.index,
    category_price.values,
    color=colors
)

plt.title("Category-wise Average Vegetable Price")
plt.xlabel("Category")
plt.ylabel("Average Price per kg")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Category_vs_Price.png", dpi=300)
plt.show()

season_count = df["Season"].value_counts()
plt.figure(figsize=(8,8))
plt.pie(
    season_count.values,
    labels=season_count.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Season-wise Veg Distribution")
plt.savefig("Season_wise_piechart.png", dpi=300)
plt.show()