# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba
# 2022-12-15 Hongsik Kim

from collections import defaultdict
# get input and split the case
test_case = int(input())
for case_count in range(test_case):
    case = input().split()
    D, N, K = int(case[0]), int(case[1]), int(case[2])
    daily_happiness = defaultdict(list)
    for _ in range(N):
        attraction = input().split()
        h_i, s_i, e_i  = int(attraction[0]), int(attraction[1]), int(attraction[2])
        for day in range(s_i, e_i+1):
            if len(daily_happiness[day]) < K:
                daily_happiness[day].append(h_i)
            elif min(daily_happiness[day]) < h_i:
                daily_happiness[day].remove(min(daily_happiness[day]))
                daily_happiness[day].append(h_i)                
    print(daily_happiness)
    
    daily_happiness_list = []    
    for value in  daily_happiness.values():
        daily_happiness_list.append(sum(value))    
    answer = max(daily_happiness_list)
    print("Case #"+str(case_count+1)+": " +str(answer))

     
    

        

