# Write a program that involves functions and takes three integers:
# Volume in L, temperature in °C and amount of a perfect gas in mol.
# This program should give two outputs: The temperature in °F and the pressure of this perfect gas.
# Use the equations below and accept the value of R (ideal gas constant) as 0.08205 (atm*L)/(K*mol).

# Perfect (ideal) gas equation: P * V = n * R * T
# T(°F) = 1.8* T(°C) + 32
# T(K) = T(°C) + 273.15

def cel_to_fah(c):
    return 1.8*c + 32

def cel_to_kel(c):
    return c + 273.15

def pressure_of_perfect_gas(n, T, V):
    return n*R*T/V

R = 0.08205
volume = int(input())
celcius = int(input())
amount = int(input())
print(cel_to_fah(celcius), "°F")
print(pressure_of_perfect_gas(amount, cel_to_kel(celcius), volume))