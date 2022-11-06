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