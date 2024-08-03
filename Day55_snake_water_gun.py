import random 
i = 0
choose = ['s', 'w', 'g']
user_points = 0
computer_points = 0

while i < 3:
    user_input = input('choose [s, w, g]: ')
    
    computer_input = random.choice(choose)
    print(f"==>> computer_input: {computer_input}")

    if user_input == 's' and computer_input == 'w':
        user_points += 1
    elif user_input == 's' and computer_input == 'g':
        computer_points += 1
    elif user_input == 'w' and computer_input == 's':
        computer_points += 1
    elif user_input == 'w' and computer_input == 'g':
        computer_points += 1
    elif user_input == 'g' and computer_input == 's':
        user_points +=1
    elif user_input == 'g' and computer_input == 'w':
        user_points +=1 

    i += 1

print(f"==>> user_points: {user_points}")
print(f"==>> computer_points: {computer_points}")

if user_points > computer_points: 
    print('You Win!!')
elif user_points < computer_points:
    print("You Loose!!")
else:
    print("It's a tie!!" )