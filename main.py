from text import Text


def main():
    print("Welcome to the Morse Code Converter!")

    text_to_transfer = str(input("What text do you want to convert?"))
    text = Text(text_to_transfer)
    print(text.text_to_morse())


if __name__ == "__main__":
    main()
