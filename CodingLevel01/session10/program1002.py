#Program to prompt and accept the name of employees and their salaries and store it in a file called employees.txt

n = int(input('How many employees are there? '))

fp = open('employees.txt', 'a')
for i in range(n):
    name = str(input(f'What is the name of employee {i + 1}? '))
    salary = float(input(f'What is the salary of employee {i + 1}? '))
    record = name + ', ' + str(salary)
    fp.write(record)
    fp.write('\n')

fp.close()


    
