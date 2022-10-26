# get the answer
import re
answer = "What's Up, Doc?"
answer = answer.upper()

answer_guessed = []

#pre-game setup.

for current_answer_character in answer:
  if re.search("^[A-Z]$", current_answer_character):
    answer_guessed.append(False)
  else:
      answer_guessed.append(True)
#game logic

num_incorrect_guesses = 5
current_incorrect_guesses = 0

letters_guessed = []

#let user play the game

while current_incorrect_guesses < num_incorrect_guesses and False in answer_guessed:
  #display game status.
  print (f"Number of incorrect guesses remaining: {num_incorrect_guesses - current_incorrect_guesses}")
  print("letter guessed: ", end= "")

  for current_letter_guessed in letters_guessed:
    print(current_letter_guessed, end= " ")

  print()

  #display puzzle board.
  for current_answer_index in range(len(answer)):
    if answer_guessed[current_answer_index]:
      print(answer[current_answer_index], end= "")
    else:
      print("_", end= "")
    
  print()
  #let the user guess letter
  letter = input("Enter a letter: ")
  letter = letter.upper()
  #check if user entered a valid latter.
  if re.search("^[A-Z]$",letter) and len(letter) == 1 and letter not in letters_guessed:
    #Insert Letter Guess(insertion sort)
    current_letter_index = 0

    for current_letter_guessed in letters_guessed:
      if letter < current_letter_guessed:
        break

      current_answer_index = 1
    letters_guessed.insert(current_letter_index, letter)

    #check if letter is in the puzzle. 
    if letter in answer:
      for current_answer_index in range(len(answer)):
        if letter == answer[current_answer_index]:
          answer_guessed[current_answer_index] =True
    else:
      current_incorrect_guesses +=1
    #post game
  if current_incorrect_guesses < num_incorrect_guesses:
    print("Congradulations, you won!")
  else:
    print(f"sorry, you lost. the was {answer}")



 

