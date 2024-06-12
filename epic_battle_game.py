import random
from getpass import getpass as input

print("Welcome to the game of stone, paper, scissor")

Get_user_input = input("Enter your first player one move (R,P,S) :")

Get_user_input_01 = input("Enter your second player two move (R,P,S) :")
if (Get_user_input != "R" and Get_user_input != "P" and Get_user_input != "S"):
  print("Please enter the correct input")
  Get_user_input = input("Enter your first player one move (R,P,S) :")
  Get_user_input_01 = input("Enter your second player two move (R,P,S) :")

elif (Get_user_input == "R" and Get_user_input_01 == 'R'
    or Get_user_input == 'r' and Get_user_input_01 == 'r'):
  print("Both players have selected Rock, so it's a tie ")
elif (Get_user_input == 'R' and Get_user_input_01 == 'S'):
  print("""Player one has selected Rock and player two has selected Scissor, 
   so 
  player one wins""")

elif (Get_user_input == 'R' and Get_user_input_01 == 'P'):
  print("""Player one has selected Rock and player two has selected Paper,so 
 player two wins""")

#paper based code
elif (Get_user_input == 'P' and Get_user_input_01 == 'P'):
  print("Both players have selected Paper, so it's a tie")
elif (Get_user_input == 'P' and Get_user_input_01 == 'R'):
  print("""Player one has selected Paper and player two has selected Rock, so 
 player one wins""")
elif (Get_user_input == 'P' and Get_user_input_01 == 'S'):
  print("""Player one has selected paper and player two has selected Scissor, 
 so player two wins""")
#scissor based code
elif (Get_user_input == 'S' and Get_user_input_01 == 'S'):
  print("Both the players have selected Scissor, so it's a tie")
elif (Get_user_input == 'S' and Get_user_input_01 == 'P'):
  print(
      """Player one has selected Scissor and player two has selected Paper, so player one wins"""
  )
elif (Get_user_input == 'S' and Get_user_input_01 == 'R'):
  print(
      """Player one has selected Scissor and player two has selected Rock, so player two wins"""
  )
else:
  print("Please enter the correct input")
  Get_user_input = input("Enter your first player one move (R,P,S) :")

  Get_user_input_01 = input("Enter your second player two move (R,P,S) :")
