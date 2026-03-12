#Calculator

import math

#Initial display
print("----------------------------------------")
print("|              Calculator              |")
print("----------------------------------------")
print("|         Mathematical Operations      |")
print("----------------------------------------")
print("|             1. Addition              |")
print("|             2. Subtraction           |")
print("|             3. Multiplication        |")
print("|             4. Division              |")
print("----------------------------------------")
print("|             Area Calculation         |")
print("----------------------------------------")
print("|       5. Area of a Square             ")
print("|       6. Area of a Rectangle          ")
print("|       7. Area of a Circle             ")
print("|       8. Area of a Triangle           ")
print("----------------------------------------")
print("|        Temperature Conversion        |")
print("----------------------------------------")
print("        9. Fahrenheit to Celsius       |")
print("       10. Celsius to Fahrenheit       |")
print("       11. Celsius to Kelvin           |")
print("       12. Kelvin to Celsius           |")
print("----------------------------------------")
print("        Interest Calculation           |")
print("----------------------------------------")
print("       13. Simple Interest             |")
print("       14. Compound Interest           |")
print("----------------------------------------")

#Choosing operation
choice = int(input("Enter your choice: "))

#Addition

match choice:
    case 1:
        a = float(input("Enter first number : "))
        b = float(input("Enter second number : "))
        total = a + b
        print(f"Sum of {a} and {b} is {total}")
    case 2:
        a = float(input("Enter first number : "))
        b = float(input("Enter second number : "))
        difference = a - b
        print(f"Difference between {a} and {b} is {difference}")
    case 3:
        a = float(input("Enter first number : "))
        b = float(input("Enter second number : "))
        product = a*b
        print(f"Product of {a} and {b} is {product}")

    case 4:
        a = float(input("Enter first number : "))
        b = float(input("Enter second number : "))
        quotient = a/b
        print(f"Quotient after dividing {a} by {b} is {quotient}")

    case _:
        print("Invalid choice")
'''
#Area of square
elif choice == 5:
    side = float(input("Enter side of the square : "))
    area = side*side
    print(f"The area of a sqaure of side {side} is {area}")
#Area of rectangle
elif choice == 6:
    length = float(input("Enter length of the rectangle : "))
    breadth = float(input("Enter breadth of the rectangle : "))
    area = length*breadth
    print(f"The area of a rectangle of length {length} and breadth {breadth} is {area}")
#Area of circle
elif choice == 7:
    radius = float(input("Enter radius of the circle : "))
    area = math.pi*radius*radius
    print(f"The arera of a circle of radius {radius} is {area}")
#Area of triangle
elif choice == 8:
    base = float(input("Enter the base of the triangle : "))
    height = float(input("Enter the height of the triangle : "))
    area = 1/2*base*height
    print(f"The are of a triangle of base {base} and height {height} is {area}")

#Fahrenheit to Celsius conversion
elif choice == 9:
    Fahrenheit = float(input("Enter the temperature in fahrenheit : "))
    Celsius = (Fahrenheit - 32)*5/9
    print(f"The temperature in celsius if the temperature in fahrenheit is {Fahrenheit} is {Celsius}")

#Celsius to Fahrenheit conversion
elif choice == 10:
    Celsius = float(input("Enter the temperature in celsius : "))
    Fahrenheit = (Celsius * 9/5) + 32
    print(f"The temperature in fahrenheit if the temperature in celsius is {Celsius} is {Fahrenheit}")

#Celsius to Kelvin conversion
elif choice == 11:
    Celsius = float(input("Enter the temperature in celsius : "))
    Kelvin = Celsius + 273
    print(f"The temperature in Kelvin if the temperature in celsius is {Celsius} is {Kelvin}")

#Kelvin to Celsius conversion
elif choice == 12:
    Kelvin = float(input("Enter the temperature in kelvin : "))
    Celsius = Kelvin - 273                  
    print(f"The temperature in Celsius if the temperature in Kelvin is {Kelvin} is {Celsius}")

#Simple interest calculation
elif choice == 13:
    principle = float(input("Enter the principle amount : "))
    rate = float(input("Enter the interest rate : "))
    time = float(input("Enter the time : "))
    SI = (principle*rate*time)/100
    print(f"The simple interest on a principle of ruppees {principle} at a rate of {rate}% over {time} years is {SI}")

#Compound interest calculation
elif choice == 14:
    principle = float(input("Enter the principle amount : "))
    rate = float(input("Enter the interest rate : "))
    time = float(input("Enter the time : "))
    Amount = principle*math.pow((1 + rate/100),time)
    CI = Amount - principle
    print(f"The compound interest on a principle of ruppees {principle} at a rate of {rate}% over {time} years is {CI}")

#Error     
else:
    print("Invalid choice")

'''
    
