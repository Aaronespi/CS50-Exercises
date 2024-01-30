def convert(text):
    #first we convert the text we want to emoji
    text_with_emoji = text.replace(":)", "🙂").replace(":(", "🙁")
    return text_with_emoji
#Define the main code
def main():
    user_input = input()
    result = convert(user_input)
    print(result)

main()