import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv("data.csv")

months = df["Month"]
sales = df["Sales"]

# 1. Line Chart
plt.figure(figsize=(6, 4))
plt.plot(months, sales, marker='o', color='blue')
plt.title("Line Chart: Sales Over Months")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Chart
plt.figure(figsize=(6, 4))
plt.bar(months, sales, color='green')
plt.title("Bar Chart: Sales Over Months")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# 3. Horizontal Bar Chart
plt.figure(figsize=(6, 4))
plt.barh(months, sales, color='orange')
plt.title("Horizontal Bar Chart: Sales Over Months")
plt.xlabel("Sales")
plt.ylabel("Month")
plt.tight_layout()
plt.show()

# 4. Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(sales, labels=months, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart: Sales Distribution")
plt.tight_layout()
plt.show()

# 5. Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(months, sales, color='purple', s=100)
plt.title("Scatter Plot: Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
