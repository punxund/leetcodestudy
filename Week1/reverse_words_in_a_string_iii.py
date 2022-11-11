#https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ''
        #make word list with split
        word_list = list(s.split())
        
        for i in word_list:
            #word is character list
            word = list(i)
            reverse_word = ''
            #make reverse_word from the last character of word
            for j in range(len(word)) :
                reverse_word = reverse_word + word[len(word)-1-j]
            #make sentence with the reverse_words
            answer = answer + reverse_word + ' '
 
        return answer.rstrip()
