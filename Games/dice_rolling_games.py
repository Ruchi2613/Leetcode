import random
#
# while True:
#     choice_from_user = input('Roll the dice? (y/n):').lower()
#     if choice_from_user == 'y':
#         die1 = random.randint(1, 6)
#         die2 = random.randint(1, 6)
#         print(f'{die1},{die2}')
#     elif choice_from_user == 'n':
#         print('Thanks for playing!')
#         break
#     else:
#         print('Invalid choice!')


'''trying to implementing with score I used chatGPT but I understood:'''

total_score = 0
while True:
    print("\nOptions:")
    print("1. Roll one die")
    print("2. Roll two dice")
    print("3. View total score")
    print("4. Exit the game")

    choice = input('Enter your choice (1/2/3/4):').lower()

    if choice == '1':
        die1 = random.randint(1, 6)
        total_score+=die1
        print(f"You rolled: {die1}")
        print(f"Your current total score is: {total_score}")

    elif choice == '2':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total_score += (die1 +  die2)
        print(f"You rolled: {die1},{die2}")
        print(f"Your current total score is: {total_score}")

    elif choice == '3':
        print(f"Your total score so far is: {total_score}")

    elif choice == '4':
        print("Thanks for playing!")
        print(f"Your final score is: {total_score}")
        break
    else:
        print("Invalid choice! Please select a valid option.")