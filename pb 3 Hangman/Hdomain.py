
class Hangman:
    def __init__(self,sentence: str):
        self._sentence = sentence

    def get_sentence(self):
        return self._sentence

    def get_letter(self,word):
        return self._sentence[word]