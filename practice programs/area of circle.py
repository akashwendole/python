def area_of_circle(radius):
    area = radius * radius * 3.14
    return area


print("Press x to exit the program.")

while True:
    radius = str(input("Enter the radius of the circle:-"))
    if radius == 'x':
        break
    else:
        print("Area of the circle is:- " + str(area_of_circle(int(radius))))