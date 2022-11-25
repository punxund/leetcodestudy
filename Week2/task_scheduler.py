# https://leetcode.com/problems/task-scheduler/submissions/846384760/
# 2022-11-19 Hongsik Kim

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time_list =[]
        set_list = set(tasks)
        # make dictionary of counting alphabet
        dictionary = {}
        for i in set_list: # O(n)
            dictionary[i] = tasks.count(i) # O(n)
        
        count_list = list(dictionary.values())
        count_max_alpha = count_list.count(max(dictionary.values())) # O(n^2)?

        # if n is 0, output is just length of tasks
        if n == 0:
            time_list.append(len(tasks))
        # if n is 1, 
        if n == 1:
            for i in dictionary.values(): # O(n)
                # output is just length
                if (i-1)*n <= sum(dictionary.values())-i:
                    time_list.append(len(tasks))
                # or the largest number of alphabet*2-1, because "AXAXAXA"
                else:
                    time_list.append(2*i-1)
        # if n is more than 2,
        if n >= 2:
            for i in dictionary.values(): # O(n)
                # output is just length
                if (i-1)*n <= sum(dictionary.values())-i and count_max_alpha != n:
                    time_list.append(len(tasks))
                # or 
                else:
                    if count_max_alpha >= 2:
                        time_list.append(((i-1)*(n+1)+1)+(count_max_alpha-1)) # "AAABBB"    
                    else:
                        time_list.append((i-1)*(n+1)+1) # "AXYAXYA" XY is idle or other alphabets

        return max(time_list) # O(n^2)


