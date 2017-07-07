# # Exercise 5: More Variables and Printing
#
# my_name = 'Kyoyoung Chu'
# my_age = 31
# my_height = 173 # cm
# my_weight = 68  # kg
# my_eyes = 'Brown'
# my_teeth = 'White'
# my_hair = 'Black'
#
# print("Let's talk about %s" % my_name)
# print("He's %d cm tall" % my_height)
# print("He's %d kg heavy" % my_weight)
# print("Actually that's not too heavy")
# print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
# print("His teeth are usually %s depending on the coffee." % my_teeth)
#
# # This line is tricky, try to get it exactly right
# print("If I add %d, %d, and %d, I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))


# Study Drill
# Drill 1: Change all the variables so there is no my_ in front of each one.
name = 'Kyoyoung Chu'
age = 31
height = 173 # cm
weight = 68  # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

weight_in_pounds = weight * 2.20462
height_in_inches = height * 0.393701

print("Let's talk about %s" % name)
print("He's %d cm tall" % height)
print("He's %d incehs tall" % height_in_inches)
print("He's %d kg heavy" % weight)
print("He's %d pounds heavy" % weight_in_pounds)
print("Actually that's not too heavy")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# This line is tricky, try to get it exactly right
print("If I add %d, %d, and %d, I get %d." % (age, height_in_inches, weight_in_pounds, age + height_in_inches + weight_in_pounds))
