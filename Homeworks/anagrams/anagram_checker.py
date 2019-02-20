class AnagramChecker:

    def __init__(self):

        # Read the lines of the file
        with open("engmix.txt", 'r') as f:
            lines = f.readlines()

        # Put everything in lowercase
        self.clearlist = []
        for line in lines:
            self.clearlist.append(line.lower())


    def is_valid_word(self, word):
        # word = word.lower()
        # for listword in self.clearlist:
        #     if word == listword:
        #         return True
        # return False
        return word.lower() in self.clearlist

    def get_anagram(self, word):
        word = word.lower()
        anagrams = []
        sorted_word = sorted(word)
        for w in self.clearlist:
            if sorted_word == sorted(w) and w != word:
                anagrams.append(w)

        return anagrams

