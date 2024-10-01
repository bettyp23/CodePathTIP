#1160. Find Words That Can Be Formed by Characters

#You are given an array of strings words and a string chars.
#A string is good if it can be formed by characters from chars (each character can only be used once).
#Return the sum of lengths of all good strings in words.

#Understand:
    #how does it work, what are the rules, what are the boundaries
    #Does a good string have to use ALL the characters in chars
    #can we use the same char in more than one word?

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        