import math
import PI
user_input_01=(float(input("Enter the lattitue t1 : ")))
user_input_02=(float(input("Enter the longititude g1 : ")))
user_input_03=(float(input("Enter the lattitue t2 : ")))
user_input_04=float(input("Enter the longitude g2 : "))

radians_conversion_t1=(PI.PI/180)*user_input_01
radians_conversion_g1=(PI.PI/180)*user_input_02
radians_conversion_t2=(PI.PI/180)*user_input_03
radians_conversion_g2=(PI.PI/180)*user_input_04


DISTANCE=math.sqrt((radians_conversion_t2)**2 )-((radians_conversion_t1)**2 )+ ( ((radians_conversion_g2) **2) - ( (radians_conversion_g1)**2 ) )

print(DISTANCE)