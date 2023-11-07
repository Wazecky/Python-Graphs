import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read CSV file
df = pd.read_csv("GOOG.csv").copy()

# Filter dates between 2020 and 2021
df = df[(df["Date"] >= "2020-01-01") & (df["Date"] <= "2021-01-01")]

# Convert date strings to datetime objects
df["Date"] = pd.to_datetime(df["Date"])

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 5))

# Create the candlestick chart
ax.bar(
    df["Date"],
    df["High"] - df["Low"],
    bottom=df["Low"],
    color="black",
    width=0.6,
    zorder=1,
)
ax.bar(
    df["Date"],
    df["Close"] - df["Open"],
    bottom=df["Open"],
    color=df["Close"].gt(df["Open"]).map({True: "g", False: "r"}),
    width=0.6,
    zorder=2,
)

# Format the x-axis
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.grid(True, which="both", linestyle="--", linewidth=0.5, zorder=0)

# Set the title and labels
plt.title("Alphabet Stock Price (2020-2021)")
plt.ylabel("Price")
plt.show()