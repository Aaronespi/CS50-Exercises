#First, we ask for an expression
expression = input("Expression: ")
#Split the expression in 3 variables
x, y, z = expression.split(" ")
#Convert the variebles x and z into his numbers
x = int(x)
z = int(z)

#MAthcing the y and make a case for each statement
match y:
    case "+":
        result = x + z
        print(f"{result:.1f}") #With a print like this we make him show with 1 decimal
    case "-":
        result = x - z
        print(f"{result:.1f}")
    case "*":
        result = x * z
        print(f"{result:.1f}")
    case _:
        result = x / z
        print(f"{result:.1f}")
