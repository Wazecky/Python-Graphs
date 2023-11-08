import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
df = pd.DataFrame({
    "Category": ["Rent", "Food", "Utilities", "Transportation", "Other"],
    "Amount": [1000, 500, 200, 300, 100]
})

# Create a pie chart
plt.pie(df["Amount"], labels=df["Category"], autopct="%1.1f%%")
plt.title("Budget Breakdown")
plt.show()