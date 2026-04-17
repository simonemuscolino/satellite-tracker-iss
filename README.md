# Satellite Tracker — ISS Visualization

This project focuses on the simulation and visualization of satellite motion using real orbital data.

The main goal is to model the trajectory of the International Space Station (ISS) as observed from a fixed location on Earth, and to provide intuitive visual representations of its motion in the sky.

---

## Project Description

Satellite tracking is a fundamental aspect of space engineering and mission analysis.  
In this project, real Two-Line Element (TLE) data from Celestrak is used to propagate the orbit of the ISS and compute its position relative to a ground observer.

Two different visualizations are generated:

- A **2D sky track**, showing how the satellite moves across the sky (Azimuth vs Elevation)
- A **polar plot**, representing a visible satellite pass from rise to set

This approach allows a clear understanding of when and where a satellite becomes visible from a specific location.

---

## Visual Outputs

### Sky Track (Azimuth vs Elevation)

This plot shows the apparent motion of the ISS in the sky over a short time window.

![Sky Track](images/sky_track_.png)

---

### Polar Pass Visualization

This representation highlights a full visible pass of the ISS, including time annotations along the trajectory.

![Polar Plot](images/polar_plot_.png)

---

## Engineering Concepts

This project applies several key aerospace concepts:

- Orbital propagation using TLE data
- Transformation to observer-based reference frames
- Azimuth and elevation coordinate systems
- Satellite visibility conditions (Altitude > 0°)
- Time-dependent trajectory analysis

---

## Observer Configuration

The observer is located in:

**Port Hedland, Australia**  
Latitude: 20.3123° S  
Longitude: 118.64498° E  

---

## Technologies Used

- Python
- Skyfield
- NumPy
- Matplotlib

---

## Future Improvements
Ground track visualization on Earth map
Real-time tracking
Multi-satellite support
GUI interface for interactive use

---

Author

Simone Muscolino
MSc Aerospace Engineering
