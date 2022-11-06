# Take the coordinates (x, y) of two points (A and B), which are located on a
# two-dimensional plane, as inputs and define them as integers.
# Write two separate functions which return the slope from A to B, and the distance between A and B.
# Print the results of these calculations.

def slope(x1,x2,y1,y2):
    return (y2-y1)/(x2-x1)

def distance(x1,x2,y1,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

xa, ya = input().split(",")
xb, yb = input().split(",")
xa, ya, xb, yb = int(xa), int(ya), int(xb), int(yb)
print(slope(xa,xb,ya,yb))
print(distance(xa,xb,ya,yb))