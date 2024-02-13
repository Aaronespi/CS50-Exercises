def main():
    amountDue = 50
    change = 0
    "Amount Due: {}".format(amountDue)
    #created a loop for amountDue greater than 0
    while amountDue > 0:
        insertedCoin = int(input("Insert Coin: "))
        #checks the input, only accepts 5, 10, 25
        if insertedCoin == 5 or insertedCoin == 10 or insertedCoin == 25:
            amountDue -= insertedCoin
            print("Amount Due: {}".format(amountDue))
        else:
            print("Amount Due: {}".format(amountDue))
    #checks if amountDue it's 0 or negative to return or not change coins
    if amountDue == 0:
        print("Change Owed: {}".format(change))
    else:
        change = abs(amountDue)
        print("Change Owed: {}".format(change))

main()