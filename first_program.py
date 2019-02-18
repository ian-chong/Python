print ("Hello World")

# practicing how to wrote coding comments 
# in multiple lines
# check this out


# Examples of a Python Dictionary

person = {
  'name': 'John',
  'age': 23,
  'occupation': 'Apprentice'
}

print(person['name'])
print(person['age'])
print(person['occupation'])

# Examples of Python Dictionary in a List
person_one = {
  'name': 'John',
  'age': 23,
  'occupation': 'Apprentice'
}

person_two = {
  'name': 'Sally',
  'age': 18,
  'occupation': 'Student'
}

person_three = {
  'name': 'Meng',
  'age': 29,
  'occupation': 'Engineer'
}

people = []
people.append(person_one)
people.append(person_two)
people.append(person_three)

print(people)

print(people[0]['name'])
print(people[1]['age'])
print(people[2]['occupation'])

# A list within a list
test = [
  ["a", "b", "c"],
  ["d", "e", "f"],
  ["g", "h", "i"]
]

print(test[1])     # ["d", "e", "f"]
print(test[1][1])  # "e"

# A Dictionary within a list
test2 = [
  {"bitcoin": 1000, "zcash":100},
  {"bitcoin": 2000, "zcash":200}
]

print(test2[0])           # {:bitcoin=>1000, :zcash=>100}
print(test2[0]["zcash"])   # 100

# A Dictionary within a Dictionary
test3 = {
    "day_1": {"bitcoin": 100, "eth":1000},
    "day_2": {"bitcoin": 200, "eth":2000}
}

print(test3["day_1"])         # {:bitcoin=>100, :eth=>1000}
print(test3["day_1"]["eth"])   # 1000

# A List within a Dictionary
test4 = {
    "my_coins": ["btc", "eth", "xmr"],
    "other_coins": ["ada", "xrp", "xvg"]
}

print(test4["other_coins"])      # ["ada", "xrp", "xvg"]
print(test4["other_coins"][1])   # "xrp"

# fruits = ["Apple", "Banana", "Durian"]
# for fruit in fruits:
#     print(fruit)

# count = 1

# while count < 5:
#     print(count)
#     count += 1

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break

for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# loopy = range(0,100)
# for i in loopy:
#     if i != 57:
#         print(i)

# Challenge Longest Name
names = ['Sheng', 'Kevin', 'Audrey', 'KJ', 'Delilah', 'Josh', 'Mack', 'Rey']
length = 0
longest_name = ""
for i in names:
    if len(i) > length:
        length = len(i)
        longest_name = i

print(longest_name)
        
info = [
    ["name", "age", "pet"],
    ["Amy", "20", "bird"],
    ["John", "21", "cat"],
    ["Ash", "24", "dog"],
]

print (info[0]+info[1])

def long_words(lst):
    words = []
    for word in lst:
        if len(word) > 5:
           words.append(word)
    return words

