from math import sin, cos, tan, sqrt, pi
from vpython import sphere, color, vector, rate, scene, label, cone

# Hohmann Transfer Orbit Parameters
velocity_initial = 32706.45
transfer_time = 258.12
period = 519.89
transfer_semi_major_axis = 1.886e11
transfer_semi_minor_axis = 1.842e11

# Set up the VPython environment
scene.title = "Spacecraft Launch from Gateway to Mars"
scene.width = 800
scene.height = 600
scene.background = color.black

# Constants
AU = 1.496e11  # Astronomical Unit in meters (average distance from Earth to Sun)

# Create celestial bodies
sun = sphere(pos=vector(0, 0, 0), radius=1.5e10, color=color.yellow, emissive=True)
earth = sphere(make_trail=True, pos=vector(AU, 0, 0), color=color.blue)
mars = sphere(make_trail=True, pos=vector(1.52 * AU, 0, 0), color=color.red)

# Labels for celestial bodies
slabel = label(pos=sun.pos, text='Sun', xoffset=20, yoffset=20, color=color.yellow, box=False)
elabel = label(pos=earth.pos, text='Earth', xoffset=20, yoffset=20, color=color.blue, box=False)
mlabel = label(pos=mars.pos, text='Mars', xoffset=20, yoffset=20, color=color.red, box=False)

# Spacecraft (Rocket) visualization
rocket = cone(make_trail=True, pos=earth.pos, color=color.white)
rlabel = label(pos=rocket.pos, text='Spacecraft', xoffset=20, yoffset=20, color=color.white, box=False)

# Simulate the rocket's trajectory
dt = 3600  # Time step in seconds
simulation_time = 0
total_simulation_duration = transfer_time * 86400  # Total duration in seconds (converted from days)

while simulation_time < total_simulation_duration:
    rate(100)  # Control the speed of the simulation

    # Update the positions of the Earth and Mars (simple circular orbits)
    earth_angle = (simulation_time / (365.25 * 86400)) * 2 * pi
    mars_angle = (simulation_time / (687 * 86400)) * 2 * pi
    
    earth.pos = vector(AU * cos(earth_angle), AU * sin(earth_angle), 0)
    mars.pos = vector(1.52 * AU * cos(mars_angle), 1.52 * AU * sin(mars_angle), 0)

    theta = (simulation_time / (period * 86400)) * 2 * pi
    x = transfer_semi_major_axis * cos(theta)  # X-coordinate of the ellipse
    y = transfer_semi_minor_axis * sin(theta)  # Y-coordinate of the ellipse
    rocket.pos = vector(x, y, 0)
    simulation_time += dt

    elabel.pos = earth.pos
    mlabel.pos = mars.pos
    rlabel.pos = rocket.pos

    # Increment time
    simulation_time += dt

# Final position after the simulation
label(pos=rocket.pos, text='Spacecraft', xoffset=20, yoffset=20, color=color.white, box=False)

