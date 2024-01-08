# Constants
TRAIN_MASS = 22680
TRAIN_ACCELERATION = 10
TRAIN_DISTANCE = 100
BOMB_MASS = 1
SPEED_OF_LIGHT = 3*10**8

# Functions
def fahrenheit_to_celsius(f_temp):
    """Convert Fahrenheit to Celsius."""
    c_temp = (f_temp - 32) * 5/9
    return c_temp

def celsius_to_fahrenheit(c_temp):
    """Convert Celsius to Fahrenheit."""
    f_temp = c_temp * (9/5) + 32
    return f_temp

def get_force(mass, acceleration):
    """Calculate force."""
    return mass * acceleration

def get_energy(mass, c=SPEED_OF_LIGHT):
    """Calculate energy."""
    return mass * (c**2)

def get_work(mass, acceleration, distance):
    """Calculaet work"""
    work = get_force(mass, acceleration) * distance
    return work

# Use the function
train_force = get_force(TRAIN_MASS, TRAIN_ACCELERATION)
bomb_energy = get_energy(BOMB_MASS)
train_work = get_work(TRAIN_MASS, TRAIN_ACCELERATION, TRAIN_DISTANCE)

# Do the Work
print(f"The GE train supplies {train_force} Newtons of force")
print(f"A 1kg bomb supplies {bomb_energy} Joules")
print(f"The GE train does {train_work} Joules of work over {TRAIN_DISTANCE} meters")

