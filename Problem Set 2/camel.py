def main():
    #ask for the input
    camel_case_var = input("camelCase: ")
    #call the function on a variable
    snake_case_var = convert_to_snake(camel_case_var)
    print("snake_case: ", snake_case_var)

def convert_to_snake(camel_var):
    #we need a variable to put the characters
    snake_var = ""
    for char in camel_var:
        #checks if it's capitalized: if true puts a _ and make it lower and push it to the var before
        if char.isupper():
            snake_var += "_" + char.lower()
            #if false, push the character to the var before
        else:
            snake_var += char
    #returns the var created on udercase all characters
    return snake_var.lstrip()

main()