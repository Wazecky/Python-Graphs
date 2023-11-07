import matplotlib.pyplot as plt

# set data
data = [1, 2, 3, 4, 5]
labels = ['A', 'B', 'C', 'D', 'E']

# create pie chart
plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()