#include <iostream>
#include <math.h>
using namespace std;


int main()
{
    const float PI = 4.0 * atan(1.0);
    float x1,x2,x3,y1,y2,y3;
    cout << "Type the coordinates of the first corner of the triangle\n";
    cin >> x1 >> y1;
    cout << "Type the coordinates of the second corner of the triangle\n";
    cin >> x2 >> y2;
    cout << "Type the coordinates of the third corner of the triangle\n";
    cin >> x3 >> y3;
    float side1 = sqrt(pow((x2 - x1),2) + pow((y2 - y1),2));
    float side2 = sqrt(pow((x3 - x1),2) + pow((y3 - y1),2));
    float side3 = sqrt(pow((x3 - x2),2) + pow((y3 - y2),2));
    if (side1 + side2 < side3 || side3 + side2 < side1 || side1 + side3 < side2)
    {
        cout << "This triangle cannot be drawn since the length of one of the sides is bigger than the sum of remaining ones.";
    }
    else if (abs(side1 - side2) > side3 || abs(side3 - side2) > side1 || abs(side1 - side3) > side2)
    {
        cout << "This triangle cannot be drawn since the length of one of the sides is smaller than the difference between remaining ones.";
    }
    else{
        float alpha1 = acos((pow(side2,2) + pow(side3,2) - pow(side1,2)) / (2*side2*side3)) * 180.0/PI;
        float alpha2 = acos((pow(side1,2) + pow(side3,2) - pow(side2,2)) / (2*side1*side3)) * 180.0/PI;
        float alpha3 = acos((pow(side2,2) + pow(side1,2) - pow(side3,2)) / (2*side2*side1)) * 180.0/PI;
        if (side1 == side2 || side1 == side3 || side2 == side3)
        {
            cout << "This triangle is isosceles\n";
            if (side1 == side2 == side3)
            {
                cout << "This triangle is equilateral\n";
            }
            else
            {

            }
        }
        if (ceil(alpha1) == 90 || ceil(alpha2) == 90 || ceil(alpha3) == 90)
        {
            if (side1 == side2 || side1 == side3 || side2 == side3)
            {
                cout << "This triangle is the right isosceles triangle\n";
            }
            else
            {
                cout << "This triangle is a right triangle\n";
            }
        }
        cout << "Length of side1 is: " << side1;
        cout << "\nLength of side2 is: " << side2;
        cout << "\nLength of side3 is: " << side3;
        cout << "\nValue of angle1 is: " << alpha1;
        cout << "\nValue of angle2 is: " << alpha2;
        cout << "\nValue of angle3 is: " << alpha3;

    }
    return 0;
}
