import matplotlib.pyplot as plt
import pandas as pd

# Create a list of data
data = [
    [2000, 1.00],
    [2001, 1.00],
    [2002, 3.06],
    [2003, 2.90],
    [2004, 2.92],
    [2005, 2.90],
    [2006, 3.05],
    [2007, 3.09],
    [2008, 3.14],
    [2009, 3.71],
    [2010, 3.89],
    [2011, 4.11],
    [2012, 4.54],
    [2013, 5.46],
    [2014, 8.08],
    [2015, 9.23],
    [2016, 14.76],
    [2017, 16.56],
    [2018, 28.09],
    [2019, 48.15],
    [2020, 70.54],
]

# Create a DataFrame from the list of data
df = pd.DataFrame(data, columns=["Year", "ARS/USD"])

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df["Year"], df["ARS/USD"])

# Add labels and title
plt.xlabel("Year")
plt.ylabel("ARS/USD")
plt.title("Exchange Rate Between the Argentinian Peso and the US Dollar")

# Show the plot
plt.show()