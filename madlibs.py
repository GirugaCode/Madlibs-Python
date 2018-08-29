import string

# Ask the user for input
adjective1 = raw_input("Give me an adjective! ")
noun1 = raw_input("Give me a noun (plural)! ")
noun2 = raw_input("Give me another noun! ")
adjective2 = raw_input("Give me another adjective and brace yourself... ")

# Print the poem
print ("")
print string.capwords("A poem with " + noun1)
print ("")
print "Roses are " + adjective1
print noun1.capitalize() + " are blue"
print noun2.capitalize() + " is " + adjective2
print "And so are you!
