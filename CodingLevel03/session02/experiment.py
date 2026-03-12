


list_of_fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']


tuple_of_quantities = (1, 2, 3, 4, 5)


dict_of_words = {
    "Jackfruit" :  "Its a fruit",
    "Tomato" : "Its a vegetable",
    "Phone" : "It's a device"

}

print(list_of_fruits)
print(tuple_of_quantities)
print(dict_of_words)


text = ""
for key in dict_of_words:
    text += key + "," + dict_of_words[key] + "\n"

print(text)