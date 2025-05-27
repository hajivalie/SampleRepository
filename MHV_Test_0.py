# Level Test - Python Script

# Q1
prime = 103
mod_result = prime % 2
print(f"{prime} mod 2 =", mod_result)
print("Is it correct? ", mod_result == 1)

# Q2
first = input("Enter your first name: ")
last = input("Enter your last name: ")
print("Type of inputs:", type(first), type(last))
full_name = first + " " + last
print("Full name:", full_name)

# Q3
my_list = ["a", "b", "c", "d", "e"]
my_list[2] = "Iran"
print(my_list)

# Q4
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(my_dict.items())

# Q5
with open('test.txt', 'w') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Last line of file")

with open('test.txt', 'r') as file:
    lines = file.readlines()
    print("Last line:", lines[-1])

# Q6
print(255 > 188 and 255 < 189)

# Q7
friends = ["Hossein", "Ali", "Hasan", "Reza", "Mahdi"]
person = "Ali"
if person in friends:
    print("HOORA")

# Q8
numbers = list(range(1, 11))
for num in numbers:
    if num % 2 == 0:
        print(num)

# Q9
x = 12
if 10 < x < 15:
    print("good")

# Q10
import random
nums = list(range(0, 10000, 100))
random.shuffle(nums)
print("Index 10:", nums[10])

# Q11
def count_evens(lst):
    return len([x for x in lst if x % 2 == 0])

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print("Even count:", count_evens(numbers))

# Q12
def check_capital(s):
    capitalized = s.capitalize()
    return capitalized, capitalized[0].isupper()

result, is_capital = check_capital("hello")
print("Capitalized:", result)
print("First letter capital?", is_capital)

input("\nPress Enter to exit...")