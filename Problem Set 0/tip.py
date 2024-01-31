def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
#This function takes de input of dollars, takes of $, convert it into a float and return the value
def dollars_to_float(d):
    d = d.removeprefix('$')
    d = float(d)
    return d
#This function takes de input of percent, takes of %, convert it into a float and return the value
def percent_to_float(p):
    p = p.removesuffix('%')
    p = float(p)
    p = p / 100
    return p

main()
