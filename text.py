from config import MORSE_DICT


class Text:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"Text: {self.text}"

    def to_morse(self):
        """
        Transfer the text object to Morse.
        """
        self.text = [letter.upper() for letter in self.text]
        translated_morse = ""
        for letter in self.text:
            if letter == self.text[-1]:
                translated_morse += f"{MORSE_DICT[letter]}"
            translated_morse += f"{MORSE_DICT[letter]} "
        return translated_morse
