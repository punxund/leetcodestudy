# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba
# 2022-12-15 Hongsik Kim

from collections import defaultdict
# get input and split the case
test_case = int(input())
for case_count in range(test_case):
    case = input().split()
    D, N, K = int(case[0]), int(case[1]), int(case[2])
    daily_happiness_dict = defaultdict(list)
    for _ in range(N):
        attraction = input().split()
        h_i, s_i, e_i  = int(attraction[0]), int(attraction[1]), int(attraction[2])
        for day in range(s_i, e_i+1):
            daily_happiness_dict[day].append(h_i)

    print(daily_happiness_dict)
    
    max_daily_happiness = 0    
    for value in daily_happiness_dict.values():
        sum = 0
        bis = len(value)
        if K < len(value):
            bis = K
        for i in range(bis):
            x = max(value)
            sum += x
            value.remove(x)
        if sum > max_daily_happiness:
            max_daily_happiness = sum 

    print("Case #"+str(case_count+1)+": " +str(max_daily_happiness))
        

