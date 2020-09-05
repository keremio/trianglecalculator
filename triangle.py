import matplotlib.pyplot as plt 
import math
pi = 3.1415
xy1 = input("Type the coordinates of the first corner of the triangle\n").split()
x1 = float(xy1[0])
y1 = float(xy1[1])
xy2 = input("Type the coordinates of the second corner of the triangle\n").split()
x2 = float(xy2[0])
y2 = float(xy2[1])
xy3 = input("Type the coordinates of the third corner of the triangle\n").split()
x3 = float(xy3[0])
y3 = float(xy3[1])

side1 = math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
side2 = math.sqrt( (x3-x1)**2 + (y3-y1)**2 )
side3 = math.sqrt( (x3-x2)**2 + (y3-y2)**2 )

if (side1 + side2 < side3 or side3 + side2 < side1 or side1 + side3 < side2):
        print("This triangle cannot be drawn since the length of one of the sides is bigger than the sum of remaining ones.")
elif (abs(side1 - side2) > side3 or abs(side3 - side2) > side1 or abs(side1 - side3) > side2):
        print("This triangle cannot be drawn since the length of one of the sides is smaller than the difference between remaining ones.")
else:
        alpha1 = math.acos((pow(side2,2) + pow(side3,2) - pow(side1,2)) / (2*side2*side3)) * 180.0/pi;
        alpha2 = math.acos((pow(side1,2) + pow(side3,2) - pow(side2,2)) / (2*side1*side3)) * 180.0/pi;
        alpha3 = math.acos((pow(side2,2) + pow(side1,2) - pow(side3,2)) / (2*side2*side1)) * 180.0/pi;
        if (side1 == side2 or side1 == side3 or side2 == side3):
            print("This triangle is isosceles\n")
            if (side1 == side2 == side3):
                print("This triangle is equilateral\n")
            else:
                print(" ")
        if (int(alpha1) == 90 or int(alpha2) == 90 or int(alpha3) == 90):
            if (side1 == side2 or side1 == side3 or side2 == side3):
                print("This triangle is the right isosceles triangle\n")
            else:
                print("This triangle is a right triangle\n")
        print("Length of side1 is: ")
        print(side1)
        print("\nLength of side2 is: ")
        print(side2)
        print("\nLength of side3 is: ")
        print(side3)
        print("\nValue of angle1 is: ")
        print(alpha1)
        print("\nValue of angle2 is: ")
        print(alpha2)
        print("\nValue of angle3 is: ")
        print(alpha3)

coord = [[x1,y1], [x2,y2], [x3,y3]]
coord.append(coord[0])
xs, ys = zip(*coord)
plt.figure()
plt.plot(xs,ys)
plt.show()

