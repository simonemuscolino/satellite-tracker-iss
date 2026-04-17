------------------------------------------------------------------------------------------
# ============================================================
# Satellite Tracker Project
# ============================================================
# Objective:
# This script generates two visualizations for satellite tracking:
# 1) A 2D sky-track plot (Azimuth vs Elevation)
# 2) A polar plot representing a visible satellite pass
#
# Data Source:
# TLE (Two-Line Element) data retrieved from Celestrak
#
# Libraries:
# - skyfield: orbital mechanics and satellite propagation
# - matplotlib: data visualization
# - numpy: numerical operations
# ============================================================


# ============================
# PART 1 — SKY TRACK (2D PLOT)
# ============================

import matplotlib.pyplot as plt
from skyfield.api import utc, load, Topos

# Load TLE data (satellite orbital elements)
station_data = load.tle('https://celestrak.com/NORAD/elements/stations.txt')
iss = station_data['ISS (ZARYA)']
print(iss)

# Define time range (2 hours, sampled every minute)
time_scale = load.timescale()
minutes = range(60 * 2)
time_range = time_scale.utc(2024, 3, 21, 2, minutes)

# Lists to store results
altitudes = []
azimuths = []

# Observer location (Port Hedland, Australia)
port_hedland = Topos(latitude='20.3123 S', longitude='118.64498 E')

# Compute satellite position over time
for t in time_range:
    orbit = (iss - port_hedland).at(t)
    altitude, azimuth, distance = orbit.altaz()

    # Store values in degrees
    altitudes.append(altitude.degrees)
    azimuths.append(azimuth.degrees)

# Plot sky track (Azimuth vs Elevation)
plt.figure(figsize=(10, 5))
plt.plot(azimuths, altitudes, linestyle='-', alpha=0.7)
plt.scatter(azimuths, altitudes)
plt.title("Satellite Path - ISS")
plt.xlabel("Azimuth (degrees)")
plt.ylabel("Altitude (degrees)")
plt.grid(True)
plt.show()
plt.savefig("sky_track.png", dpi=300)

# ============================
# PART 2 — POLAR PASS PLOT
# ============================

from skyfield import api
from pytz import timezone
import numpy as np

# Define observer time zone
time_zone = timezone('US/Pacific')

# Reload TLE data using Skyfield API
station_data = api.load.tle('https://celestrak.com/NORAD/elements/stations.txt')
iss = station_data['ISS (ZARYA)']
print(iss)

# Define extended time range (2 days)
minutes = range(60 * 24 * 2)
time_scale = api.load.timescale()
time_range = time_scale.utc(2024, 3, 21, 2, minutes)

# Observer location
port_hedland = api.Topos(latitude='20.3123 S', longitude='118.64498 E')

# Compute satellite position over entire time range
orbit = (iss - port_hedland).at(time_range)
altitude, azimuth, distance = orbit.altaz()

print(f"Altitudes: {altitude}")
print(f"Azimuth: {azimuth}")
print(f"Distance: {distance}")

# Identify when the satellite is visible (altitude > 0°)
visible_pass = altitude.degrees > 0

# Extract indices of visibility transitions
indicies, = visible_pass.nonzero()
boundaries, = np.diff(visible_pass).nonzero()

# Reshape into (rise, set) pairs
passes = boundaries.reshape(len(boundaries) // 2, 2)
print(passes)

# Select a specific pass to visualize
pass_to_observe = 0
specific_pass = passes[pass_to_observe]
rise, set_time = specific_pass

# Print rise and set times
print(f'ISS Rises at {time_range[rise].astimezone(time_zone)}')
print(f'ISS Sets at {time_range[set_time].astimezone(time_zone)}')

# Create polar plot
plt.figure(figsize=(8, 8))  # NUOVA FIGURA
ax = plt.subplot(111, projection='polar')
plt.title("ISS Pass Polar Chart")
plt.savefig("polar_plot.png", dpi=300)

# Configure polar axes
ax.set_rlim([0, 100])  # radial limit (elevation)
ax.set_theta_zero_location('N')  # North at top
ax.set_theta_direction(-1)  # clockwise direction

# Convert coordinates
theta = azimuth.radians
r = 90 - altitude.degrees  # convert elevation to polar radius

# Plot selected pass
ax.plot(theta[rise:set_time], r[rise:set_time], 'bo--')

# Annotate time along the pass
for k in range(rise, set_time):
    text = time_range[k].astimezone(time_zone).strftime('%H:%M')
    ax.text(theta[k], r[k], text, ha='right', va='bottom')
