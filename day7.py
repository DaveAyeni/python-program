import random
word_list =  ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard egg mole monkey moose mouse mule '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''] 
random_word = random.choice(word_list)
print(random_word)
lists = []
attempt_letters = []
for _ in range(len(random_word)):
  lists += "_"
print(lists)
print()
attempt = 0
max_attempt = 6
hang_index = 0
while attempt < max_attempt:
  found = False
  ask = input("Enter a letter: ")
  print()
  for index, letter in enumerate(random_word):
    if ask == letter:
      lists[index] = ask
      found = True
  if found:
    print(lists)
    print()
  else:
    print(HANGMANPICS[hang_index])
    for _ in ask:
      attempt_letters += ask
    print("ATTEMPTED LETTER(S)", attempt_letters)
    print()
    print(lists)
    print()
    attempt += 1
    hang_index += 1
  if not "_" in lists:
    print("YOU WON!!!")
    break
  if attempt == max_attempt:
    print("GAME OVER YOU FUCKING LOST... THE WORD WAS" , random_word)
    break
