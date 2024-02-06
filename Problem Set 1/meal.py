def main():
    time = input("What time is it? ")
    converted_time = convert(time)#Here we call our function to convert the input to a number

    if converted_time >= 7 and converted_time <= 8:
        print("breakfast time")
    elif converted_time >= 12 and converted_time <= 13:
        print("lunch time")
    elif converted_time >= 18 and converted_time <= 19:
        print("dinner time")
    else:
        print("")
#Our function takes the input and split it
def convert(time):
    hours, minutes = time.split(":")
    #Convert both ina  float number
    hours = float(hours)
    minutes = float(minutes)
    #to get the minutes just divide by 60 and you will get the number with 2 decimals, sum all and return
    converted_time = hours + (minutes / 60)
    return converted_time



if __name__ == "__main__":
    main()