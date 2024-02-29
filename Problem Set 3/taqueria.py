def main():
#we call the function to run
    x = get_order("Item: ")

def get_order(prompt):
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.00

    while True:
        try:
    #ask for the input and capitalize first character of every word
            x = input(prompt).title()
    #if the input its an empty space stops the loop
            if x == "":
                break
    #if the input its in the menu dict, pair the key value, sums to total and prints the amount and redoo the loop
            if x in menu:
                total += menu[x]
                print(f"Total: ${total:.2f}")
    #handling EOFError and KeyError
        except EOFError:
            break
        except KeyError:
            pass

main()
