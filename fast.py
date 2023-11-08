import matplotlib.pyplot as plt

# Animal names and their speeds
animals = ["Peregrine falcon", "Golden eagle", "White-throated needletail swift", "Eurasian hobby", "Frigatebird", "Spur-winged goose", "Cheetah", "Sailfish", "Pronghorn antelope", "Marlin"]
speeds = [389, 240, 169, 160, 153, 142, 120, 112, 88.5, 80.5]  # Speeds in km/h

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(animals, speeds, color='skyblue')

# Set the chart title and labels
plt.title("Fastest Animals in the World (Speed in km/h)")
plt.xlabel("Animals")
plt.ylabel("Speed (km/h)")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()