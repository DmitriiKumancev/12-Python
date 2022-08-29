# 1. MADLIBS
# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ___ "
youtuber = "BMTH" # some string variable

# a few ways to do this
print("subscibe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")  # !!! this is the most cleanest way to express srtring concatenation

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")


madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

 
