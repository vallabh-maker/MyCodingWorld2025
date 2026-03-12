#Function to display characters in reverse order along with its index in different lines

def print_characters_with_index_in_reverse(s):
    for i in range(len(s) - 1,-1 , -1):
        print(f'The character at index {i} is', s[i])

print_characters_with_index_in_reverse('computer')
