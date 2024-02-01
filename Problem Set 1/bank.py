greeting = input("Greeting: ")

greeting = greeting.lower().strip()
#We made the input case-insensitive and get ride of spaces on both sides
if greeting[0] != "h": #if not estart's with h
    print("$100")
elif greeting[0] == "h" and greeting.startswith("hello") != True: #if starts with h but not hello
    print("$20")
else: #if starts with hello
    print("$0")