
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a DataFrame
df = pd.DataFrame({
'data_availability': ['Good', 'Good', 'Good', 'Bad', 'Bad', 'Good', 'Good', 'Bad', 'Bad', 'Good', 'Good'],
'affordable_housing': ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No'],
'educational_quality': ['High', 'Medium', 'Low', 'High', 'Low', 'Medium', 'High', 'Low', 'Low', 'Medium', 'High'],
'trust_in_police': ['High', 'Medium', 'Low', 'Low', 'High', 'Good', 'Medium', 'Low', 'High', 'Good', 'Medium'],
'roads_and_sidewalks': ['Good', 'Good', 'Fair', 'Bad', 'Bad', 'Good', 'Good', 'Fair', 'Bad', 'Good', 'Good'],
'local_gatherings': ['Frequent', 'Occasional', 'Rare', 'Rare', 'Frequent', 'Frequent', 'Occasional', 'Rare', 'Rare', 'Frequent', 'Occasional'],
'mental_health': ['Good', 'Good', 'Fair', 'Poor', 'Poor', 'Good', 'Good', 'Fair', 'Poor', 'Good', 'Good']
})

# Create a bar chart of the number of people with each level of data availability, grouped by mental health
df.groupby(['data_availability', 'mental_health']).size().unstack().plot(kind='bar')

# Set the chart title and labels
plt.title("Number of People with Each Level of Data Availability, Grouped by Mental Health")
plt.xlabel("Data Availability")
plt.ylabel("Number of People")

# Show the chart
plt.show()