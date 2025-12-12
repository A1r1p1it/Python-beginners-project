secret_word = "naruto"
guess = ""
guessNumber = 0
limitOfGuess = 3
outOfGuesses = False

while guess != secret_word and not outOfGuesses:
  if guessNumber < limitOfGuess:
    guess = input("Enter your name: ")
  else:
    outOfGuesses = True

if outOfGuesses:
  print("you lost")
else:
  print("win!")


