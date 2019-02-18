number = input("Please pick a number kind Sir!")
print(f"You have chosen {number} as your final choice.")

if int(number) % 15 == 0:
    print('FizzBuzz')
elif int(number) % 5 == 0:
    print('Buzz')
elif int(number) % 3== 0:
    print('Fizz')
else:
    print(number)

