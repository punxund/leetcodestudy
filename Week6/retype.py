# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043adc7
# 2022-12-09 Hongsik Kim

test_case = int(input())
cases = [input().split() for _ in range(test_case)]
count = 0
print(cases)
for case in cases:
    N = int(case[0])
    K = int(case[1])
    S = int(case[2])

    from_first = (K-1)+1+N
    backwards = (K-1)+(K-S)+(N-S+1)
    print(from_first)
    print(backwards)
    answer = min(from_first, backwards)
    count += 1
    print("Case #"+str(count)+": " +str(answer))