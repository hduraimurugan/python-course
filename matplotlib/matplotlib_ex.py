import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV
df = pd.read_csv("data.csv")
print(type(df))

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Sales"], marker='o', color='royalblue', linewidth=2)

# Titles and labels
plt.title("Monthly Sales Overview", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales", fontsize=12)
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
