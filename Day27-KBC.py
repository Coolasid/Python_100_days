'''
Create a program capable of displaying questions to user like KBC.
User List data type to store the question and their correct answers.
Display the final amount the person is taking home after playing the game.
'''

questions = ["who is India's PM", "India's Capital", 'National bird', 'National animal']

options = [
  ['Godi', 'Modi', 'Codi', 'Lodi'],
  ['Delhi', 'Belhi', 'Kelhi', 'Jelhi'],
  ['Peacock', 'Parrot', 'Sparrow', 'Eagle'],
  ['Wolf', 'Elephant', 'Lion', 'Tiger'],
  ]

prize_money = [1000000, 2000000, 3000000, 4000000]

answers = ('Modi', 'Delhi', 'Peacock', 'Tiger')

# Do-while loop

index = 0
prize_won = 0

while True:
  print(f'{index+1} question: {questions[index]}')
  print(f'And Your Options are: {options[index]}')
  user_input = input('Answer: ')
  print(f"==>> user_input: {user_input}")

  if user_input != answers[index]:
    print('You Loose!!')
    break

  prize_won += prize_money[index]
  print(f"==>> prize_won: ₹{prize_won}")
  index += 1
  if index > 3:
    break

print(f'You will take home: ₹{prize_won}')

  



