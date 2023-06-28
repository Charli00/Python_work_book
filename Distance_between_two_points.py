'''The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t 1 , g 1 ) and (t 2 , g 2 ) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t 1 ) × sin(t 2 ) + cos(t 1 ) × cos(t 2 ) × cos(g 1 − g 2 ))
The value 6371.01 in the previous equation wasn’t selected at random. It is
the average radius of the Earth in kilometers.
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.'''

from math import radians,acos,sin,cos
user_input_01=radians(float(input("Enter the lattitue t1 : ")))
user_input_02=radians(float(input("Enter the longititude g1 : ")))
user_input_03=radians(float(input("Enter the lattitue t2 : ")))
user_input_04=radians(float(input("Enter the longitude g2 : ")))

latitude_Difference=user_input_03-user_input_01

longitude_difference=user_input_04-user_input_02


distance = 6371.01 * acos(sin(user_input_01) * sin(user_input_03) + cos(user_input_01) * cos(user_input_03) * cos(user_input_02 - user_input_04))

print(f"THE DISTANCE BETWEEN TWO POINTS : ",distance)
