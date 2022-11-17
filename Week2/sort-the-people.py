#https://leetcode.com/problems/sort-the-people/description/
#2022-11-17 Hongsik Kim

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #make dictionary with names and heights - O(n)
        people = {}
        for i in range(len(names)):
            people[heights[i]] = names[i]
        
        #descending order by heights - O(nlogn)
        heights.sort(reverse=True)
        
        #return names sorted in order by heights O(n)
        answer = []
        for j in heights:
            answer.append(people[j])

        #O(nlogn)
        return answer