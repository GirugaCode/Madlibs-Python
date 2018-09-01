# Story

'''
This is a story about (Enter name1:) and (Enter name2:). These two were madly in love.
Everyday they would (Enter verb:) eachother without thinking twice. However, one day
the two lovers went inside a (Enter noun:) and was never to be seen agian.

'''



# Create Variables

Name1 = input("Enter a name: ")
Name2 = input("Enter another name: ")
verb = input("Enter a verb: ")
noun = input("Enter a noun: ")

print("""This is a story about %s and %s. These two were madly in love.
Everyday they would start %s eachother without thinking twice.
However, one day the two lovers went
inside a %s and was never to be seen agian.""" % (Name1, Name2, verb, noun))

# Prompt the user to enter the madlibs (noun, adj, verb)


# Print the Story


# The world's simplest madlibs
# def zeus():
#     verb = input("Enter a verb: ")
#     noun = input("Enter a noun: ")
#     anothernoun = input("Enter another noun: ")
#     print("Zeus %sed  %s but %s was unaffected by it." % (verb, noun, anothernoun))
#
#
# def about():
#     adjective = input("Enter an adjective: ")
#     adj = input("Enter another adjective: ")
#     print("You're %s and %s" % (adjective, adj))
#
# story = input("Which story would you like to play Possible options thelightgod, aboutYourEnemy:  ")
# if story == "thelightgod":
#     zeus()
# elif story == "aboutYourEnemy":
#     about()
# else:
    # print("Doesn't Exist.")
