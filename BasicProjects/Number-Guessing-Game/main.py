print("Welcome to the number guessing game")
number = int(input("The numbers should be between 1 to 100: \n"))
difficulty = input("Choose a difficult. Type 'easy' or 'hard': ")
if difficulty == "easy":
  chance = 10
  print("You have 10 attempts remaining to guess the number")
  while chance > 0:
    guess = int(input("Make a guess: "))
    if guess < number:
      chance -= 1
      if chance == 0:
        print("You have run out of guesses. You lose")
      else:
        print(f'Too low\nGuess again.\nYou have {chance} attempts remaining to guess the number')
    elif guess > number:
      chance -= 1
      if chance == 0:
        print("You have run out of guesses. You lose")
      else:
        print(f'Too high\nGuess again.\nYou have {chance} attempts remaining to guess the number')
    else:
      print(f'You got it. The answer was {number}')
      break
else:
  chance = 5
  print("You have 5 attempts remaining to guess the number")
  while chance > 0:
    guess = int(input("Make a guess: "))
    if guess < number:
      chance -= 1
      if chance == 0:
        print("You have run out of guesses. You lose")
      else:
        print(f'Too low\nGuess again.\nYou have {chance} attempts remaining to guess the number')
    elif guess > number:
      chance -= 1
      if chance == 0:
        print("You have run out of guesses. You lose")
      else:
        print(f'Too high\nGuess again.\nYou have {chance} attempts remaining to guess the number')
    else:
      print(f'You got it. The answer was {number}')
      break
