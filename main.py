from text import Text


def main():
    print("Welcome to the Morse Code Converter!")
    print("***")

    text_to_transfer = str(input("What text do you want to convert: "))
    text = Text(text_to_transfer)

    try:
        print("***")
        print(f"Morse code of '{text.text}' is '{text.to_morse()}'.")
        print("***")

    except Exception as e:
        print(f"Message: {e.__class__.__name__} {e}")
        print("Try again!")
        main()


if __name__ == "__main__":
    main()
