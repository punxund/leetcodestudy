class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        lower_list = []
        for word in wordlist: # O(n), n is the length of wordlist.
            lower_list.append(word.lower())

        # chnage the vowel to 'a'
        def vowel_change(word): # O(l), m is the length of word.
            changed_word = ""
            lower_word = word.lower()
            for alphabet in list(lower_word):
                if alphabet in ['a', 'e', 'i', 'o', 'u']:
                    changed_word += 'a'
                else:
                    changed_word += alphabet
            return changed_word

        vowel_changed_words = []
        for word in wordlist: # O(n)
            vowel_changed_words.append(vowel_change(word))

        output_list = []
        for query in queries: # O(n*m*l), l is the length of queries
            lower_word = query.lower()
            # When query exactly matches a word in the wordlist, return same word back.    
            if query in wordlist: # O(n)
                output_list.append(query)
            # When query matches a word up to capitlization, return first match in wordlist.
            elif lower_word in lower_list: # O(n)                                
                output_list.append(wordlist[lower_list.index(lower_word)])
            # When query matches a word up to vowel errors, return the first match in wordlist.
            elif vowel_change(query) in vowel_changed_words: # O(n*m)                
                output_list.append(wordlist[vowel_changed_words.index(vowel_change(query))])
            # If query has no matches in the wordlist, return the empty string.
            else:
                output_list.append("")

        return output_list # o(n*m*l)