def bmi(w, h):
    return w/(2.54*h/100)**2

weight = float(input())
height = float(input())
print("%.2f" % bmi(weight, height))