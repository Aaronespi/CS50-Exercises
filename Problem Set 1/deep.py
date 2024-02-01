Answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
Answer = Answer.casefold().strip()
#We made the input case-insensitive and get ride of spaces on both sides

if Answer == "42" or Answer =="forty-two" or Answer =="forty two":
    print("Yes") #if one of the conditiosn it's true prints Yes
else:
    print("No") #if none of them are true, prints No