import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
df = pd.DataFrame({
    "body_area": ["Chest", "Back", "Triceps", "Biceps", "Shoulders", "Abs", "Legs", "Legs", "Calves", "Glutes"],
    "target_muscle": ["Pectoralis Major", "Latissimus Dorsi", "Triceps Brachii", "Biceps Brachii", "Deltoids", "Rectus Abdominis", "Quadriceps", "Hamstrings", "Gastrocnemius", "Gluteus Maximus"],
    "exercise": ["Bench Press", "Pull-Ups", "Triceps Pushdowns", "Bicep Curls", "Overhead Press", "Crunches", "Squats", "Deadlifts", "Calf Raises", "Hip Thrusts"],
    "workout_length": [30, 30, 30, 30, 30, 30, 30, 30, 30, 30],
    "reps": [10, 10, 10, 10, 10, 20, 10, 10, 20, 10]
})

# Plot the time series of workout lengths over time
plt.figure(figsize=(10, 6))
plt.plot(df["exercise"], df["workout_length"])
plt.title("Time Series of Workout Lengths")
plt.xlabel("Exercise")
plt.ylabel("Workout Length (minutes)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()