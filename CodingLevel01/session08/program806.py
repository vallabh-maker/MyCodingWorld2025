#Function to reverse a string and display both given string and reversed string.

def display_string_forwards_and_backwards(s):
    reverse = ""
    for i in range(len(s)):
        reverse = reverse + s[((len(s) - 1) - i)] 
    
    print(s)
    print(reverse)
    if s == reverse:
        print(s, 'is a palindrome')

display_string_forwards_and_backwards('madam')
