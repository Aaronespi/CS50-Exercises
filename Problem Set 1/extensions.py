file = input("File name: ") #first we get the input

file = file.lower().strip() #make him case-insensitive and strip the spaces on both sides

#With .endswith() we can check how our input ends and will print one thing or another
if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg") or file.endswith(".jpeg"):
     print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")