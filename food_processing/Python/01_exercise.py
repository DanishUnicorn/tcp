# EXERCISE 1: PUMP ASSIGNMENT

"""
A liquid food is pumped at 80°C at a volume rate of 2.8 m³/hour from a tank A to another tank B. 
The absolute pressure in both tanks is 101325 Pa. The food is pumped through stainless steel pipe (sanitary pipe) 
with a nominal diameter of 1.0 inch. Tank A is at the same height as the pump, while tank B is 4.4 meters above the height of the pump. 
There is 20m of pipe before the pump with one 90° (flanged) bend and 5m of pipe after the pump with a ‘globe’ valve, 
fully open but no bends. The liquid has a viscosity of 0.0012 Pa·s and a density of 1060 kg/m³. 
You can assume that the liquid levels do not change when pumping.
"""

import numpy as np  # For calculations

# Nested dictionary for pipe types and inner diameters (ID) in inches
pipe_IDs = {
    "steel": {
        0.5: 0.622, 0.75: 0.824, 1.0: 1.049, 1.5: 1.610,
        2.0: 2.067, 2.5: 2.469, 3.0: 3.068, 4.0: 4.026
    },
    "sanitary": {
        0.75: 0.902, 1.0: 0.902, 1.5: 1.402, 2.0: 1.870,
        2.5: 2.370, 3.0: 2.870, 4.0: 3.834
    }
}

def get_inner_diameter(D_inch, pipe_type="sanitary"):
    """
    Returns the inner diameter in meters for a given nominal pipe size (inches).
    pipe_type: "steel" or "sanitary".
    """
    try:
        return pipe_IDs[pipe_type][D_inch] * 0.0254  # Convert inches to meters
    except KeyError:
        raise ValueError(f"Nominal pipe size {D_inch} inch not found in {pipe_type} pipes.")

"""
# a) Determine the mean velocity and Reynolds number for the flow.
"""

def calculate_reynolds(V_m3_per_h, D, rho, mu):
    """
    Calculates the mean velocity and Reynolds number.
    Returns velocity (m/s), Reynolds number, and flow type.
    """
    # Convert flow rate from m³/h to m³/s
    V_dot = V_m3_per_h / 3600  

    # Compute cross-sectional area of the pipe
    A = np.pi * (D / 2) ** 2  

    # Mean velocity calculation
    V_mean = V_dot / A  

    # Reynolds number calculation
    Re = (rho * V_mean * D) / mu  

    # Determine flow type
    flow_type = (
        "Laminar flow" if Re < 2100 
        else "Transition flow" if 2100 <= Re <= 4000 
        else "Turbulent flow"
    )

    return V_mean, Re, flow_type

# Given data
V_m3_per_h = 2.8  # Volume flow rate in m³/h
D_inch = 1.0  # Nominal pipe size in inches (Change depending on the pipe size)
pipe_type = "sanitary"  # Change to "steel" for steel pipes
rho = 1060  # Density in kg/m³
mu = 0.0012  # Dynamic viscosity in Pa·s

# Fetch inner diameter before using it in functions
D = get_inner_diameter(D_inch, pipe_type)

# Compute results for velocity and Reynolds number
V_mean, Re, flow_type = calculate_reynolds(V_m3_per_h, D, rho, mu)

# Output results in a clear format
print(f"Mean velocity: {V_mean:.4f} m/s")
print(f"Reynolds number: {Re:.0f}")
print(f"Flow type: {flow_type}")

"""
# b) Determine all pressure drop contributions in the system and state the total pressure
drop both in units of J/kg and as head.
"""

def calculate_pressure_drop(P1, P2, u, z1, z2, rho):
    """
    Calculates:
    - Pressure difference per unit mass (ΔP)
    - Pressure drop head (ΔP_h)
    - Kinetic energy per unit mass (KE)
    - Kinetic energy head (KE_h)
    - Total head loss (dH)
    
    Returns all computed values.
    """
    g = 9.81  # Gravitational acceleration (m/s²)
    
    # Pressure difference per unit mass
    delta_P = (P2 - P1) / rho

    # Pressure head
    delta_P_h = delta_P / g

    # Kinetic energy per unit mass
    KE = 0.5 * u**2

    # Kinetic energy head
    KE_h = KE / g

    # Total head loss
    dH = g * (z2 - z1)

    return delta_P, delta_P_h, KE, KE_h, dH

# Given data
P1 = 101325  # Absolute pressure at tank A (Pa)
P2 = 101325  # Absolute pressure at tank B (Pa)
u = V_mean  # Flow velocity (m/s)
z1 = 0  # Reference height (tank A, pump level)
z2 = 4.4  # Height at tank B (m)
rho = 1060  # Density (kg/m³)

# Compute results
delta_P, delta_P_h, KE, KE_h, dH = calculate_pressure_drop(P1, P2, u, z1, z2, rho)

# Output results
print(f"Pressure difference per unit mass (ΔP): {delta_P:.2f} Pa/kg")
print(f"Pressure drop head (ΔP_h): {delta_P_h:.4f} m")
print(f"Kinetic energy per unit mass (KE): {KE:.4f} J/kg")
print(f"Kinetic energy head (KE_h): {KE_h:.4f} m")
print(f"Total head loss (dH): {dH:.4f} m")


"""
E minor loss factor
"""
def calculate_minor_losses(u):
    """
    Computes minor loss energy (Eminor) and minor loss head (Eminor_h).
    """
    g = 9.81  # Gravitational acceleration (m/s²)

    # Loss coefficients from professor's method
    K_bend = 0.3   # 90° flanged bend
    K_valve = 10   # Fully open globe valve
    K_entrance = 0.5  # Minor loss at entrance
    K_exit = 1.0  # Minor loss at exit

    # Sum of all minor loss coefficients
    K_total = (1 * K_bend) + K_valve + K_entrance + K_exit  

    # Compute minor loss energy
    Eminor = K_total * 0.5 * u**2  

    # Compute minor loss head
    Eminor_h = Eminor / g  

    return Eminor, Eminor_h

# Example data
u = V_mean  # Flow velocity (m/s), previously calculated

# Compute minor losses
Eminor, Eminor_h = calculate_minor_losses(u)

# Output results
print(f"Minor loss energy (Eminor): {Eminor:.4f} J/kg")
print(f"Minor loss head (Eminor_h): {Eminor_h:.4f} m")

