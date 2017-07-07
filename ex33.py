# Exercise 33: While Loops

i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)


def while_drill():
    print("What number do you want to go to? ")
    print("> ")
    input_number = int(input())
    i = 0
    numbers = []

    while i < input_number:
        print("At the top i is %d" % i)
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)
