def login_system():
  while True:
    username = input("What is your username?: ")
    password = int(input("What is your password?: "))
    if username == "David" and password == 123:
      print("Welcome David!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue


print("REPLIT LOGIN SYSTEM")
login_system()
