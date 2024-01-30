def einstein(m):
    c = 300000000
    E = m * pow(c, 2)
    return E

def main():
    m = int(input("m: "))
    result = einstein(m)
    print("E: ", result)

main()
