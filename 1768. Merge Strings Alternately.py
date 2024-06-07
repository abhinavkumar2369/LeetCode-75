class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        if len(word1)>len(word2):
            length = len(word2)
            word = word1[len(word2):]
        else:
            length = len(word1)
            word = word2[len(word1):]
            
        new_word = ''
        
        for i in range(length):
            new_word = new_word + word1[i]+ word2[i]
        new_word+=word
            
        return new_word