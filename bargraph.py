import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
df = pd.DataFrame({
    "Country": ["China", "India", "United States", "Indonesia", "Pakistan", "Nigeria", "Brazil", "Bangladesh", "Russia", "Mexico"],
    "Population": [1.444e9, 1.412e9, 332.4e6, 279.1e6, 238.2e6, 218.5e6, 212.6e6, 169.6e6, 146.1e6, 128.9e6]
})

# Sort the DataFrame by population
df = df.sort_values(by=["Population"], ascending=False)

# Create a bar plot
plt.bar(df["Country"], df["Population"])

# Set the title and axis labels
plt.title("Population of the Top 10 Most Populous Countries in 2023")
plt.xlabel("Country")
plt.ylabel("Population (in billions)")

# Rotate the x-axis labels to prevent overlapping
plt.xticks(rotation=45)

# Show the plot
plt.show()