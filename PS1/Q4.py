def slope(x1,x2,y1,y2):
    return (y2-y1)/(x2-x1)

def distance(x1,x2,y1,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

xa, ya = input().split(",")
xb, yb = input().split(",")
xa, ya, xb, yb = int(xa), int(ya), int(xb), int(yb)
print(slope(xa,xb,ya,yb))
print(distance(xa,xb,ya,yb))