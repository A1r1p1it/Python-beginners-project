secret_word = "ghost"
your_guess = ""
total_guess = 3
attempt = 0
reuser = 3    # ← YOU used "reuser"
outOfGuess = False

while your_guess != secret_word and not outOfGuess:
  if attempt < total_guess:
    your_guess = input("What is your word: ")
    if your_guess == secret_word:
      break
      
    attempt += 1
    reuser -= 1
    print("\nWrong! \nYou have", reuser , "left attempt.\n")
      

  else: 
    outOfGuess = True

if outOfGuess:
  print("\nu lost")
else:
  print("\nu win")
