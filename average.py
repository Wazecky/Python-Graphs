# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load data in a pandas dataframe
data = {
    'Carrier': ['Verizon', 'AT&T', 'T-Mobile', 'UScellular', 'Mint Mobile', 'Visible'],
    'Coverage area': ['99% of the US population', '98% of the US population', '98% of the US population', '95% of the US population', "99% of the US population (uses T-Mobile's network)", "99% of the US population (uses Verizon's network)"],
    'Price': ["$50-$180", "$40-$165", "$30-$135", "$30-$120", "$15-$40", "$40"],
    'Network type': ['CDMA and LTE', 'GSM and LTE', 'GSM and LTE', 'GSM and LTE', 'GSM and LTE', 'CDMA and LTE'],
    'Data speeds': ['Up to 1 Gbps', 'Up to 1 Gbps', 'Up to 1 Gbps', 'Up to 1 Gbps', 'Up to 1 Gbps', 'Up to 1 Gbps'],
    'Customer service': [4.5, 4.0, 3.5, 4.0, 4.0, 3.5],
    'Features': ['HD calling, Wi-Fi calling, international roaming, hotspot tethering', 'HD calling, Wi-Fi calling, international roaming, hotspot tethering', 'HD calling, Wi-Fi calling, international roaming, hotspot tethering', 'HD calling, Wi-Fi calling, international roaming, hotspot tethering', 'HD calling, Wi-Fi calling, international roaming, hotspot tethering', 'HD calling, Wi-Fi calling, international roaming, hotspot tethering'],
    'Contract options': ['Month-to-month, 1-year, and 2-year contracts', 'Month-to-month, 1-year, and 2-year contracts', 'Month-to-month, 1-year, and 2-year contracts', 'Month-to-month, 1-year, and 2-year contracts', 'Month-to-month only', 'Party pay only'],
    'Family plans': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
    'Device discounts': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
    'Promotions': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

# Extract numerical values from the price range and calculate the average
average_prices = []
for price_range in df['Price']:
    price_values = [int(price.strip('$')) for price in price_range.split('-')]
    average_price = sum(price_values) / len(price_values)
    average_prices.append(average_price)

# Calculate the overall average price
overall_average_price = sum(average_prices) / len(average_prices)

print(f"The overall average price across all carriers is ${overall_average_price:.2f}.")