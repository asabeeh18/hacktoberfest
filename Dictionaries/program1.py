number = input("Enter any number : ")
number_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five"
}
output = ""
for item in number:
    output += number_mapping.get(item, "!")
print(output)
