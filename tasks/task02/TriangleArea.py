import math


# Method for menu printing
def print_menu():
    print("")
    print("Menu:")
    print("1. Calculate triangle area by base and height")
    print("2. Calculate triangle area by 2 sides and angle between them")
    print("3. Exit")


# Method calculation of triangle area by provided base and height
def calc_by_height():
    s = input("Enter base and height: ")
    parts = s.split(" ")
    base = float(parts[0])
    height = float(parts[1])
    area_float = 0.5 * base * height
    print(f"Area is: {round(area_float)}")


# Method calculation of triangle area by provided 2 sides and angle(degrees) between them
def calc_by_angle():
    s = input("Enter 2 sides and angle(degrees) between them: ")
    parts = s.split(" ")
    side_a = float(parts[0])
    side_b = float(parts[1])
    angle = int(parts[2])
    radians = math.radians(angle)
    sin = math.sin(radians)
    area_float = float(0.5 * side_a * side_b * sin)
    print(f"Area is: {round(area_float)}")


# Main code
print("Welcome to the triangle area calculation tool.")
i = 0
while True:
    print_menu()
    i = int(input("Enter menu item number: "))
    if i == 1:
        calc_by_height()
    elif i == 2:
        calc_by_angle()
    elif i == 3:
        print("Goodbye!")
        exit()

