# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/
# 2022-11-25 Hongsik Kim

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # !!!!time limit exceeded!!!!
        string_list = list(s)
        bracket_list = []
        for i in range(len(string_list)): #O(n)           
            if string_list[i] == "(":
                a = i
            if string_list[i] == ")":                
                b = i
                bracket_list.append(s[a+1:b])
        print(bracket_list)

        value_list = [x[0] for x in knowledge] # O(n)
        key_list = [x[1] for x in knowledge] # O (n)       

        answer = s
        for i in bracket_list: # O(n^2)??
            if i in value_list:
                answer = answer.replace("("+i+")", key_list[value_list.index(i)]) # O(n)??             
            else:
                answer = answer.replace("("+i+")", "?")

        return answer 


        


