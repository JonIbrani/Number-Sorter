print("This program sorts out the numbers you give it.")

counter = 0
user_list = []
user_counter = int(input('Enter how many numbers you want us to sort out:\n'))

while counter < user_counter:
    user_numbers = int(input('Write down a number:\n'))
    user_list.append(user_numbers)
    counter += 1

sort_order = input("Enter 'A' for ascending order or 'D' for descending order: ")

if sort_order == 'A':
    user_list.sort()
elif sort_order == 'D':
    user_list.sort(reverse=True)
else:
    print("Invalid input for sorting order. Defaulting to ascending order.")

print(user_list)
