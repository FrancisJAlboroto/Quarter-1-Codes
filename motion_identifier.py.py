# Motion Type Identifier

# Function 1: Convert velocity to m/s
def convert_velocity(value, unit):
    if unit == "m/s":
        return value
    elif unit == "ft/s":
        return value * 0.3048       # 1 ft = 0.3048 m
    elif unit == "km/s":
        return value * 1000         # 1 km = 1000 m
    elif unit == "mi/s":
        return value * 1609.34      # 1 mile = 1609.34 m

# Function 2: Convert acceleration to m/s²
def convert_acceleration(value, unit):
    if unit == "m/s^2":
        return value
    elif unit == "ft/s^2":
        return value * 0.3048       # 1 ft/s² = 0.3048 m/s²
    elif unit == "km/s^2":
        return value * 1000         # 1 km/s² = 1000 m/s²
    elif unit == "mi/s^2":
        return value * 1609.34      # 1 mi/s² = 1609.34 m/s²

# Function 3: Determine motion type
def motion_type(v, a):
    if v > 0 and a == 0:
        return "Uniform Motion"
    elif v > 0 and a > 0:
        return "Accelerated Motion"
    elif v > 0 and a < 0:
        return "Decelerated Motion"
    elif v == 0:
        return "At Rest"

# --- Main Program ---

# Step 1: Input velocity
v_value = float(input("Enter velocity value: "))
v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")

# Step 2: Input acceleration
a_value = float(input("Enter acceleration value: "))
a_unit = input("Enter acceleration unit (m/s^2, ft/s^2, km/s^2, mi/s^2): ")

# Step 3: Convert to SI units
v_si = convert_velocity(v_value, v_unit)
a_si = convert_acceleration(a_value, a_unit)

# Step 4: Determine motion type
motion = motion_type(v_si, a_si)

# Step 5: Display results
print("\n--- Results ---")
print("Velocity = {:.3f} m/s".format(v_si))
print("Acceleration = {:.3f} m/s²".format(a_si))
print("Motion Type = {}".format(motion))