import math

# Constants
g0 = 9.81  # Standard gravity in m/s^2
seconds_per_day = 86400  # Number of seconds in a day
mu_sun = 1.327e20  # Gravitational parameter for the Sun in m^3/s^2

# Function to calculate effective exhaust velocity
def effective_exhaust_velocity(Isp):
    return Isp * g0

# Function to calculate mass flow rate
def mass_flow_rate(F, Isp):
    ve = effective_exhaust_velocity(Isp)
    if ve <= 0:
        raise ValueError("Effective exhaust velocity must be greater than zero.")
    return F / ve

# Function to calculate time of flight in seconds
def time_of_flight(delta_v, Isp, initial_mass, thrust):
    ve = effective_exhaust_velocity(Isp)
    m_dot = mass_flow_rate(thrust, Isp)
    
    final_mass = initial_mass / (10 ** (delta_v / ve))
    
    if m_dot <= 0:
        raise ValueError("Mass flow rate must be greater than zero.")
    
    flight_time_seconds = (initial_mass - final_mass) / m_dot
    
    return flight_time_seconds

# Function to calculate fuel mass needed
def fuel_mass_needed(initial_mass, final_mass):
    return initial_mass - final_mass

# Function to optimize the orbital parameters
def optimal_orbital_parameters(r1, r2):
    """
    Calculate the semi-major axis and transfer velocities for a Hohmann transfer orbit
    based on the specific optimal placements.
    
    Parameters:
    r1 (float): Radius of the initial orbit (m)
    r2 (float): Radius of the final orbit (m)
    
    Returns:
    tuple: Semi-major axis of the transfer orbit (a), velocity at r1 (v1), velocity at r2 (v2)
    """
    a = (r1 + r2) / 2
    v1 = math.sqrt(mu_sun * (2 / r1 - 1 / a))
    v2 = math.sqrt(mu_sun * (2 / r2 - 1 / a))
    return a, v1, v2

# Function to optimize the transfer time
def optimal_transfer_time(r1, r2):
    """
    Calculate the transfer time for a Hohmann transfer orbit with optimal placement.
    
    Parameters:
    r1 (float): Radius of the initial orbit (m)
    r2 (float): Radius of the final orbit (m)
    
    Returns:
    float: Transfer time in seconds
    """
    a, _, _ = optimal_orbital_parameters(r1, r2)
    T = 2 * math.pi * math.sqrt(a**3 / mu_sun)
    return T / 2

# Function to calculate orbital parameters for Hohmann transfer
def orbital_parameters(r1, r2):
    """
    Calculate the semi-major axis and transfer velocities for a Hohmann transfer orbit.
    
    Parameters:
    r1 (float): Radius of the initial orbit (m)
    r2 (float): Radius of the final orbit (m)
    
    Returns:
    tuple: Semi-major axis of the transfer orbit (a), velocity at r1 (v1), velocity at r2 (v2)
    """
    a = (r1 + r2) / 2
    v1 = math.sqrt(mu_sun * (2 / r1 - 1 / a))
    v2 = math.sqrt(mu_sun * (2 / r2 - 1 / a))
    return a, v1, v2

# Function to calculate transfer time for Hohmann orbit
def transfer_time(r1, r2):
    """
    Calculate the transfer time for a Hohmann transfer orbit.
    
    Parameters:
    r1 (float): Radius of the initial orbit (m)
    r2 (float): Radius of the final orbit (m)
    
    Returns:
    float: Transfer time in seconds
    """
    a, _, _ = orbital_parameters(r1, r2)
    T = 2 * math.pi * math.sqrt(a**3 / mu_sun)
    return T / 2

# Main function
def main():
    # Spacecraft performance parameters
    delta_v = 9000  # Total delta-v in m/s
    specific_impulse = 10000  # Specific impulse in seconds
    initial_mass = 90000 # Initial mass of the spacecraft in kg
    thrust_per_thruster = 15  # Thrust per thruster in Newtons
    num_thrusters = 8 # Number of thrusters
    thrust = thrust_per_thruster * num_thrusters  # Total thrust in Newtons
    
    # Calculate effective exhaust velocity
    ve = effective_exhaust_velocity(specific_impulse)
    
    # Calculate mass flow rate
    m_dot = mass_flow_rate(thrust, specific_impulse)
    
    # Calculate final mass
    final_mass = initial_mass / (10 ** (delta_v / ve))
    
    # Calculate time of flight
    flight_time_seconds = time_of_flight(delta_v, specific_impulse, initial_mass, thrust)
    flight_time_days = flight_time_seconds / seconds_per_day
    
    # Calculate Hohmann transfer orbit parameters
    r1 = 1.496e11  # Radius of Moon's orbit around the Sun in meters
    r2 = 2.272e11  # Average radius of Mars orbit around the Sun in meters
    
    a, v1, v2 = orbital_parameters(r1, r2)
    transfer_time_seconds = transfer_time(r1, r2)
    transfer_time_days = transfer_time_seconds / seconds_per_day  # Convert to days
    
    # Calculate fuel needed
    fuel_needed = fuel_mass_needed(initial_mass, final_mass)
    
    # Output results
    print(f"Spacecraft Performance:")
    print(f"Effective Exhaust Velocity: {ve:.2f} m/s")
    print(f"Time of Flight: {flight_time_days:.2f} days")
    print(f"Mass of Fuel Needed: {fuel_needed:.2f} kg")
    print(f"Mass Flow Rate: {m_dot:.4f} kg/s")
    print()
    print(f"Hohmann Transfer Orbit:")
    print(f"Semi-major axis of the transfer orbit: {a:.2e} m")
    print(f"Velocity at initial orbit (r1): {v1:.2f} m/s")
    print(f"Velocity at final orbit (r2): {v2:.2f} m/s")
    print(f"Transfer time: {transfer_time_days:.2f} days")

if __name__ == "__main__":
    main()


