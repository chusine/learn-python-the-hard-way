# Exercise 13: Parameters, Unpacking, Variables

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# To run the code in Terminal:
# > python ex13.py first, 2nd, 3rd -> type argument variables with it
# > python ex13.py stuff thing that
# > python ex13.py apple orange grapefruit

# Combine argument variable(argv) and input()
script, first = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", end = " ")
second = input()
print("Your third variable is:", end = " ")
third = input()
