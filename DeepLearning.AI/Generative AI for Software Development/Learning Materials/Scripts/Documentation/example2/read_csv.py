# Wrong and bad documented code
import pandas as pd
import numpy as np

# load weather data
weather_df = pd.DataFrame('april2024_station_data.csv')

# Numpy is faster so convert
wind_speed = df['wind_speed'].to_numpy()
wind_direction = df['wind_direction'].to_numpy()

# Better built in function in np
wind_direction_rad = np.deg2rad(wind_direction)


# Correct and well documented code
import pandas as pd
import numpy as np

# Load the weather station data from the CSV file into a pandas DataFrame.
# Each row is expected to contain weather measurements such as wind speed
# and wind direction for April 2024.
weather_df = pd.read_csv("april2024_station_data.csv")

# Extract the wind speed column and convert it to a NumPy array.
# NumPy arrays are useful for fast numerical calculations.
wind_speed = weather_df["wind_speed"].to_numpy()

# Extract the wind direction column and convert it to a NumPy array.
# Wind direction is expected to be measured in degrees.
wind_direction_deg = weather_df["wind_direction"].to_numpy()

# Convert wind direction values from degrees to radians.
# Many NumPy trigonometric functions, such as sin() and cos(),
# expect angle values to be in radians rather than degrees.
wind_direction_rad = np.deg2rad(wind_direction_deg)

# Using docstring documentation
import pandas as pd
import numpy as np

"""
This script loads weather station data from a CSV file and prepares
wind-related values for numerical analysis.

The script:
1. Reads the weather dataset into a pandas DataFrame.
2. Extracts wind speed values as a NumPy array.
3. Extracts wind direction values in degrees.
4. Converts wind direction from degrees to radians for mathematical use.
"""

# Read weather station data from the CSV file.
weather_df = pd.read_csv("april2024_station_data.csv")

# Convert wind speed data from the DataFrame column into a NumPy array.
# This makes later numerical operations faster and easier.
wind_speed = weather_df["wind_speed"].to_numpy()

# Convert wind direction data from degrees into a NumPy array.
wind_direction_deg = weather_df["wind_direction"].to_numpy()

# Convert wind direction from degrees to radians.
# Radians are required when using NumPy trigonometric functions.
wind_direction_rad = np.deg2rad(wind_direction_deg)