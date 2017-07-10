# Exercise 38: Doing Things to Lists

# class Thing(object):
#     def test(message):
#         print(message)
#
# a = Thing()
# a.test("hello")
#

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There are {} items now.".format(len(stuff)))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])    # whoa! fancy, returns the last item in the list
print(stuff.pop())  # get rid of the first item in the list and returns
print(' '.join(stuff))    # what? cool! make a string with a list joining with a whitespace in between the words
print('#'.join(stuff[3:5]))    # super stellar!
