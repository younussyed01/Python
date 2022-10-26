import re

# get the answer

answer = "whats up doc?"

answer = answer.upper()

#per-game setup
answer_guessed = []

for current_answer_character in answer:
  if re.search("^[A-Z]$", current_answer_character):
    answer_guessed.append(False)
  else:
      answer_guessed.append(True)

      