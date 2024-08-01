'''

from random import randint

LOW, HIGH = 1, 10

clue = ''

random_number = randint(LOW, HIGH)
print(f"==>> random_number: {random_number}")

while True:
  number = input(f'Guess the number bt {LOW} and {HIGH}  {clue}:' )
  guess = int(number)

  if guess > random_number:
    clue = f'(choose a smaller number then {guess})'
  elif guess < random_number:
    clue = f'(choose a lager number then {guess})'
  else:
    break

print('You won the game!!! ')
'''

print('=============')

i = 0
while True:
  print(i)
  i += 1
  if( i %100 == 0):
    break
  