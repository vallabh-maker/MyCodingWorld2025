#Function to find the sum of first 5 natural numbers

def find_sum_of_first_5_natural_numbers():
    summ = 0
    for i in range(1, 6):
        summ += i
    print(f'The sum of the first 5 natural numbers is {summ}')

find_sum_of_first_5_natural_numbers()

#Function to find the sum of even numbers from 1 to 10

def find_sum_of_even_numbers_from_1_to_10():
    summ = 0
    for i in range(1, 11):
        if i%2 == 0:
            summ += i
    print(f'The sum of the first 5 even numbers is {summ}')

find_sum_of_even_numbers_from_1_to_10()
