def guess():
  import random

  secret_number = random.randint(1, 50)
  max_attempts = 5
  attempts = 0

  while attempts < max_attempts:
    print(f"{max_attempts - attempts} attempts left")

    user = int(input(f"Enter number 1-50: "))

    if not isinstance(user, int):
      print(f"Must be a number")

    if not 1 <= user <= 50:
      print(f"Enter number between 1-50")
      continue

    if user < secret_number:
      print(f"Too low")
    elif user > secret_number:
      print(f"Too high")
    else:
      print(f"You won")
      return

    attempts += 1

  if attempts == max_attempts:
      print(f"You have run out of attempts, You lose")

def menu():
  while True:
    print(f"Guessing Number Game")
    print('-'*20)
    print("1. Play")
    print("2. Exit")

    users = int(input("Enter Menu: "))

    if users == 1:
      guess()
    else:
      break

menu()