import pandas as pd
import matplotlib.pyplot as plt

# Create a list of data
data = [
    {"sex": "male", "age_in_years": 1},
    {"sex": "female", "age_in_years": 2},
    {"sex": "male", "age_in_years": 3},
    {"sex": "female", "age_in_years": 4},
    {"sex": "male", "age_in_years": 5},
    {"sex": "female", "age_in_years": 6},
    {"sex": "male", "age_in_years": 7},
    {"sex": "female", "age_in_years": 8},
]

# Create a DataFrame
df = pd.DataFrame(data)

# Plot the distribution of the age
plt.hist(df["age_in_years"])
plt.xlabel("Age in years")
plt.ylabel("Number of abalones")
plt.title("Distribution of age in abalone dataset")
plt.show()