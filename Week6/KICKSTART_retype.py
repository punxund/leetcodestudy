# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043adc7
# 2022-12-13 Hongsik Kim

# get input and split the case
test_case = int(input())
cases = [input().split() for _ in range(test_case)]

# each case get the time to finish the game
case_count = 0
for case in cases:
    case_count += 1
    N = int(case[0])
    K = int(case[1])
    S = int(case[2])
    # calculate the time from first and backward(to S) and find the least time
    from_first = (K-1)+1+N
    backwards = (K-1)+(K-S)+(N-S+1)
    answer = min(from_first, backwards)
    # print the output    
    print("Case #"+str(case_count)+": " +str(answer))