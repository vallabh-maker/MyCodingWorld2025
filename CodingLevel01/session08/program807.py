#Multiplication game
import random
def beginner():
    score = 0
    for i in range(1, 21):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        product = a*b
        answer = int(input(f'What is {a}x{b}? '))
        if product == answer:
            print('Correct!')
            score +=1
        else:
            print('Incorrect!')
    print(f'Your final score is {score}')
        
def intermediate():
    score = 0
    for i in range(1, 21):
        a = random.randint(10, 20)
        b = random.randint(10, 20)
        product = a*b
        answer = int(input(f'What is {a}x{b}? '))
        if product == answer:
            print('Correct!')
            score +=1
        else:
            print('Incorrect!')
    print(f'Your final score is {score}')
def advanced():
    score = 0
    for i in range(1, 21):
        a = random.randint(20, 30)
        b = random.randint(20, 30)
        product = a*b
        answer = int(input(f'What is {a}x{b}? '))
        if product == answer:
            print('Correct!')
            score +=1
        else:
            print('Incorrect!')
    print(f'Your final score is {score}')

def menu():
    print('------------------------------------------------------------------')
    print('                        Level Choice                              ')
    print('------------------------------------------------------------------')
    print('                        1. Beginner                               ')
    print('------------------------------------------------------------------')
    print('                       2. Intermediate                            ')
    print('------------------------------------------------------------------')
    print('                        3. Advanced                               ')
    print('------------------------------------------------------------------')

    choice = int(input('Select the difficulty level - '))
    if choice == 1:
        beginner()
    if choice == 2:
        intermediate()
    if choice == 3:
        advanced()
    else:
        print('Invalid choice')

menu()
        
