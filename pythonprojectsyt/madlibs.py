# # string concatenaton (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____"
# youtuber = "Drew" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Input an Adjective: ")
verb1 = input("Input a first Verb: ")
verb2 = input("Input a second Verb: ")
famous_person = input("Input a famous person: ")

madlib = f"Computer programming ss so {adj}! It makes me so excited all the time because \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
    
print(madlib)