name = "John Doe"
age = 47
occupation = "Spy"

print(f"{name}, aged {age} is a {occupation}")

number = 5
number= number + 20
print (f"The number is {number}.")

number_of_oranges = 3333
number_of_people = 4
print(int(number_of_oranges/number_of_people))
print(int(number_of_oranges%number_of_people))

sentence = "This is a string"
print(sentence)
print(type(sentence))

age = 34
if age < 12:
    print('Deny Entry')
elif age < 18:
    print('Ask for parent\'s consent letter')
else:
    print('Let in')

age = 11
if age < 12:
    print('Deny Entry')
elif age < 18:
    print('Ask for parent\'s consent letter')
else:
    print('Let in')

age = 11
if age < 18:
    print('Deny Entry')
elif age < 12:
    print('Ask for parent\'s consent letter')
else:
    print('Let in')

age = 14
if age < 12:
    print('Deny Entry')
elif age < 18:
    print('Ask for parent\'s consent letter')
else:
    print('Let in')

age = 12
if age <= 12:
    print('Deny Entry')
elif age < 18:
    print('Ask for parent\'s consent letter')
else:
    print('Let in')

name = input("What is your name?")
print(f"Hello {name}")