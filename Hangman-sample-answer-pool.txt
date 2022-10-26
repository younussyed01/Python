import re

#getting the answer.

pool_file = open("hangman-sample-answer-pool.txt")

pool_answers = []

pool_answers_line = pool_file.readline()

while pool_answers_line:
  pool_answers.append(pool_answers_line)

  pool_answers_line = pool_file.readline()


answer = "What's Up, Doc?"
answer = answer.upper()
#game setup.

num_of_incorrect_guesses = 5

answer_guessed = []