#import random
from Hdomain import Hangman
class MemoryRepo:
    def __init__(self):
        self.data=[]

    def add_sentence(self,sentence):
        self.data.append(sentence)


    def display_all(self):
        return list(self.data)

    def get_same_letters(self,letter,word):
        list_letters=[]

        for i in range(len(word)):
            if word[i] == letter:
                list_letters.append(i-1)

        return list(list_letters)


class TextFileRepo(MemoryRepo):
    def __init__(self,filename):
        super().__init__()
        self._filename=filename
        self.load()

    def display_all(self):
        return list(self.data)

    def add_sentence(self,sentence):
        super().add_sentence(sentence)
        self.save()

    def get_same_letters(self,letter,word:str):
        return super().get_same_letters(letter,word)

    def load(self):
        try:
            with open(self._filename,'r') as file:
                for line in file:
                    line=line.strip()
                    self.data.append(line)
        except:
            self.data=[]

    def save(self):
        with open(self._filename,'w') as file:
            for s in self.data:
                file.write(s)
