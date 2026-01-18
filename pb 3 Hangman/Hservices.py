from Hrepo import TextFileRepo
#print("hidden: ", hidden_word[i+1], "   my guess: ", guess[i])
class Service:
    def __init__(self,repo):
        self._repo=repo

    def guess_letter(self,guess,word,hidden_word):
        index=list(self._repo.get_same_letters(guess,word))

        hidden_word=list(hidden_word)
        for i in index:
            hidden_word[i+1]=guess
        return "".join(hidden_word)

    def display_all_sentences(self):
        return list(self._repo.display_all())

