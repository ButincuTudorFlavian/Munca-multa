
word="anna has apples"
copy_word="a__a h_s a____s"
import random
class UI:
    def __init__(self,service):
        self.service = service

    def _run(self):
        hidden_phrase,phrase=self._random_sentence()
        #phrase="anna has apples"
        #hidden_phrase="a__a h_s a____s"
        computer="hangman"
        computer=list(computer)
        computer_range=1
        print("LUNGIME", len(computer))
        while True:

            print("your sentence is: ",hidden_phrase)
            guess = input("Guess a letter: ")
            hidden_phrase=self.service.guess_letter(guess,phrase,hidden_phrase)

            if hidden_phrase == phrase:
                print("YOU WON!, The sentence was:",phrase)
                break

            print("computer: ")
            for i in range(computer_range):
                print(computer[i])
                if i == len(computer)-1:
                    print("YOU LOST!")
                    break


            computer_range+=1



    def _random_sentence(self):
        list1=self.service.display_all_sentences()
        choice=random.choice(list1)

        words=choice.split(" ")
        hidden_phrase=[]
        for w in words:
            w=list(w)
            for i in range(1,len(w)-1):
                w[i]='_'

            hidden_phrase.append("".join(w))
            hidden_phrase.append(" ")
        return "".join(hidden_phrase),choice

