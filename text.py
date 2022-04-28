from config import MORSE_DICT


class Text:
    def __init__(self, text):
        self.text = text

    def text_to_morse(self):
        self.text = [letter.upper() for letter in self.text]
        translated_morse = ""
        for letter in self.text:
            if letter == self.text[-1]:
                translated_morse += f"{MORSE_DICT[letter]}"
            translated_morse += f"{MORSE_DICT[letter]} "
        return translated_morse


