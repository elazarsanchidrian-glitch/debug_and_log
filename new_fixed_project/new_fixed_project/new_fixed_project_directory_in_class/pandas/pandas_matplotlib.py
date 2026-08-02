import pip
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/orders.csv")
df_first_5_rows = df.head(5)

print("first 5 rows:" , df_first_5_rows)

df_last_5_rows = df.tail(5)
print("last 5 rows:" , df_last_5_rows)

quantity = df["Quantity"]
print(quantity)
print()


print(f"Number of orders: {len(df)}")
print(f"Total products sold: {sum(quantity)}")
print(f"Total products sold: {quantity.sum()}")
print(f"Average quantity per order: {round(quantity.mean / len(quantity), 2)}")
print(f"largest order: ")

category_totals = df.groupby("Category")["Quantity"].sum()

plt.title("sales by category")
plt.xlabel("category")
plt.ylabel("quantity")

plt.tight_layout()


plt.savefig("sales_by_category.png")
category_totals.plot(
    kind="pie",
    title="sales by category",






