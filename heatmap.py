import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
df = pd.DataFrame({
    "fuel_economy": [33, 28, 31, 23, 24, 29, 30, 29, 32],
    "engine_size": [2.5, 2.5, 1.5, 5.0, 6.2, 2.5, 2.0, 2.0, 2.5],
    "engine_displacement": [1.5, 1.8, 1.4, 4.6, 6.2, 1.8, 1.8, 1.8, 1.8],
    "horsepower": [350, 203, 174, 460, 455, 188, 195, 201, 184],
    "weight": [1500, 3200, 2800, 3500, 3800, 3200, 3000, 3000, 3000],
    "acceleration": [4.4, 8.3, 9.2, 5.2, 4.8, 8.5, 8.8, 9.0, 8.7],
    "year": [2022, 2023, 2022, 2023, 2022, 2023, 2022, 2023, 2022],
})

# Create a heatmap of the correlation between different features
correlation_matrix = df.corr()

plt.matshow(correlation_matrix, cmap='coolwarm')
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)

# Add annotation text to the heatmap
for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        plt.text(i, j, f'{correlation_matrix.iat[i, j]:.2f}', ha='center', va='center', color='black')

plt.colorbar()
plt.show()
