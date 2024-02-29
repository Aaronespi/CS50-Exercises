def main():
    #create a loop to reprompt if the input its not what we want
    while True:
        try:
            x, y = map(int, input("Factorial: ").split('/'))
            #here we handle if x is greater than y to start again the loop
            if x > y:
                continue
            #rounding to neares whole number and making it from 0 to 100
            z = round((x/y) * 100)
            if 0 <= z <= 1:
                print("E")
            elif 99 <= z <= 100:
                print("F")
            else:
                print(f"{z}%")
            #when it's done breaks the loop
            break
        #here we handle if the input its not a number
        except ValueError:
            pass
        #here we handle if we try to divide by 0
        except ZeroDivisionError:
            pass

main()