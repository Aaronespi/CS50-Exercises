def main():
   stringInput = input("Input: ")
   output = delete_vowels(stringInput)
   print("Output : {}".format(output))
#checks if a character is in the list, if match, removes it
def delete_vowels(stringInput):
    vowelList = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "I"]
    for char in vowelList:
        stringInput = stringInput.replace(char, "")
    return stringInput

main()
