#Function to display the multiplication table of 7
def display_multiplication_table(n):
    for i in range(1,11):
        product = i*n
        print(f'{n}x{i} = {product}')

for i in range(1, 21):
    display_multiplication_table(i)
    print('-------------------------------------------')
