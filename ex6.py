# Exercise 6: Strings and Text

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who knows %s and those who %s." % (binary, do_not)

print(x)
print(y)

# To see the difference between %r and %s
print("I said: %r." % x)     # I said: 'There are 10 types of people.'.
print("I said: %s." % x)     # I said: There are 10 types of people..

print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left isde of ..."
e = "a string with a right side."

print(w + e)
