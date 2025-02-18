from sympy import symbols, Eq, solve, log

"""
# A liquid food (specific heat = 4.0 kJ/[kg °C]) flows in the inner pipe of a double-pipe heat exchanger. The liquid food enters the heat exchanger at 20°C and exits at 60°C (Fig. E4.16). The flow rate of the liquid food is 0.5 kg/s. In the annular section, hot water at 90°C enters the heat exchanger and flows countercurrently at a flow rate of 1 kg/s. The average specific heat of water is 4.18 kJ/(kg °C). Assume steady-state conditions.
"""

# Given data

T_food_exit = 60  # Exit temperature of liquid food in °C
T_food_inlet = 20  # Entrance temperature of liquid food in °C
c_p_food = 4.0  # Specific heat of liquid food in kJ/(kg °C)
m_dot_food = 0.5  # Flow rate of liquid food in kg/s

T_water_inlet = 90  # Entrance temperature of hot water in °C
c_p_water = 4.18  # Specific heat of water in kJ/(kg °C)
m_dot_water = 1  # Flow rate of hot

d_inner = 0.05  # Inner diameter of the pipe in meters
# flow = countercurrent # Flow type

# Define symbolic variables
T_water_exit = symbols("T_water_exit")


# 1) Calculate the exit temperature of water.
# To do this, we will use the following equation: q = m_dot * c_p * (T_food_inlet - T_food_exit) = m_dot * c_p * (T_water_exit - T_water_inlet)

# Where:
# q = heat transfer rate (kW)
# m_dot = mass flow rate (kg/s)
# c_p = specific heat (kJ/(kg °C))
# T_food_inlet = entrance temperature of liquid food (°C)
# T_food_exit = exit temperature of liquid food (°C)
# T_water_inlet = entrance temperature of hot water (°C)
# T_water_exit = exit temperature of hot water (°C)

# Calculating q:
q = (m_dot_food * c_p_food * ( T_food_exit - T_food_inlet))

print(f"Heat transfer rate: {q:.2f} kW")

# Solving for T_water_exit:
eq_01 = Eq(m_dot_food * c_p_food * (T_food_exit - T_food_inlet), m_dot_water * c_p_water * (T_water_inlet - T_water_exit))

solution = solve(eq_01, T_water_exit)
print(f"T_water_exit =", solution[0], "°C")

# 2) Calculate log-mean temperature difference.
# The log-mean temperature difference (LMTD) is calculated using the formula:
# LMTD = (Delta_T1 - Delta_T2) / ln(Delta_T1 / Delta_T2)

# Where:
T_water_exit = solution[0]
Delta_T1 = T_water_exit - T_food_inlet
Delta_T2 = T_water_inlet - T_food_exit

LM_Delta_T = (Delta_T1 - Delta_T2) / (log(Delta_T1 / Delta_T2))

print(f"Log-mean temperature difference: {LM_Delta_T:.2f} °C")

# 3) If the average overall heat transfer coefficient is 2000 W/(m² °C) and the diameter of the inner pipe is 5 cm, calculate the length of the heat exchanger.


# 4) Repeat these calculations for parallel-flow configuration.
#Du bytter om på Delta T1 og Delta T2