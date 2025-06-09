import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV
df = pd.read_csv("data.csv")

# Step 2: View data
print("\n--- Head ---")
print(df.head())

# Step 3: Filter data (e.g., IT department only)
it_dept = df[df['Department'] == 'IT']
print("\n--- IT Department ---")
print(it_dept)

# Step 4: Group by department and average salary
grouped = df.groupby('Department')['Salary'].mean().reset_index()
print("\n--- Average Salary by Department ---")
print(grouped)

# Step 5: Plotting - Bar Chart
# plt.figure(figsize=(8, 5))
# plt.bar(grouped['Department'], grouped['Salary'], color='skyblue')
# plt.title("Average Salary by Department")
# plt.xlabel("Department")
# plt.ylabel("Average Salary")
# plt.tight_layout()
# plt.savefig("bar_chart.png")  # Save the chart
# plt.show()
