# Exercise 21: Functions Can Return Something

def add(a, b):
    print("Adding %d + %d" % (a, b))
    return a + b

def substract(a, b):
    print("Substracting %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("Multiplying %d * %d" % (a, b))
    return a * b

def devide(a, b):
    print("Deviding %d / %d" % (a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 1)
height = substract(200, 27)
weight = multiply(33, 2)
iq = devide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle")

what = add(age, substract(height, multiply(weight, devide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
