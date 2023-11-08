import pandas as pd
import matplotlib.pyplot as plt

# Create a list of lists containing the data
data = [
    ["Michael Phelps", "United States", "Swimming", 23],
    ["Larisa Latynina", "Soviet Union", "Gymnastics", 18],
    ["Nikolai Andrianov", "Soviet Union", "Gymnastics", 15],
    ["Bjørg Dæhlie", "Norway", "Cross-country skiing", 12],
    ["Paavo Nurmi", "Finland", "Athletics", 9],
    ["Carl Lewis", "United States", "Athletics", 9],
    ["Usain Bolt", "Jamaica", "Athletics", 9],
    ["Mark Spitz", "United States", "Swimming", 9],
    ["Jenny Thompson", "United States", "Swimming", 12],
    ["Ray Ewry", "United States", "Athletics", 8],
]

# Create a list of column names
column_names = ["Name", "Country", "Sport", "Gold Medals"]

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data, columns=column_names)

# Create a figure and plot Country data
fig = plt.figure(figsize=(10,6))
plt.pie(df['Country'].value_counts(), labels=df.Country.unique(), autopct='%1.0f%%')

# Add a title and legend
plt.title("Countries of Athletes with the Most Summer Olympic Gold Medals")
plt.legend()

# Show the plot
plt.show()