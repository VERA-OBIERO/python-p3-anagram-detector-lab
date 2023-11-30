# your code goes here!
class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, anagram_list):
        new_anagrams = []
        for i in anagram_list:
            if sorted(i.lower()) == sorted(self.word) and i.lower() != self.word:
                new_anagrams.append(i)
        return new_anagrams
        
