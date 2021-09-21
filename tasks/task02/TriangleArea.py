def printmenu():
    print("")
    print("Menu:")
    print("1. Calculate triangle area by base and height")
    print("2. Calculate triangle area by 2 sides and angle between them")
    print("3. Exit")


def calch():
    s = input("Enter base and height: ")
    parts = s.split(" ")
    base = float(parts[0])
    height = float(parts[1])
    areaFloat = 0.5*base*height
    print(f"Area is: {round(areaFloat)}")


def calca():
    import math
    s = input("Enter 2 sides and angle(degrees) between them: ")
    parts = s.split(" ")
    sideA = float(parts[0])
    sideB = float(parts[1])
    angle = int(parts[2])
    radians = math.radians(angle)
    sin = math.sin(radians)
    areafloat = float(0.5*sideA*sideB*sin)
    print(f"Area is: {round(areafloat)}")

print("Welcome to the triangle area calculation tool.")
i = 0
while i != 3:
    printmenu()
    i = int(input("Enter menu item number: "))
    if i == 1:
        calch()
    elif i == 2:
        calca()
print("Goodbye!")
