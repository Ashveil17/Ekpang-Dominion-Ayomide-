# Five Basic Physics Formulas

G = 9.81  # standard gravity, m/s²


# 1. Speed = Distance / Time
def calculate_speed(distance, time):
    if time == 0:
        raise ValueError("Time cannot be zero")
    return distance / time


# 2. Acceleration = Change in Velocity / Time
def calculate_acceleration(v_final, v_initial, time):
    if time == 0:
        raise ValueError("Time cannot be zero")
    return (v_final - v_initial) / time


# 3. Force = Mass x Acceleration
def calculate_force(mass, acceleration):
    return mass * acceleration


# 4. Weight = Mass x Gravity
def calculate_weight(mass, gravity=G):
    return mass * gravity


# 5. Kinetic Energy = 1/2 x Mass x Velocity²
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2


# Displaying results
print(f"Speed: {calculate_speed(100, 20):.2f} m/s")
print(f"Acceleration: {calculate_acceleration(20, 10, 5):.2f} m/s²")
print(f"Force: {calculate_force(10, 5):.2f} N")
print(f"Weight: {calculate_weight(10):.2f} N")
print(f"Kinetic Energy: {calculate_kinetic_energy(10, 5):.2f} J")
