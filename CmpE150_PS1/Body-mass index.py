# Write a function that returns the body-mass index(kg/m^2) by using the equation 1 in = 2.54 cm.
# Take the weight(kg) and height(in) values as inputs and define them as floats.
# Print the results with two digits after the decimal point.

def bmi(w, h):
    return w/(2.54*h/100)**2

weight = float(input())
height = float(input())
print("%.2f" % bmi(weight, height))