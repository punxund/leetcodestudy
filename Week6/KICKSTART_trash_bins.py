# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887c32
# 2022-12-13 Hongsik Kim

# get input and split the case
test_case = int(input())
input = [input() for _ in range(test_case*2)]
N = input[0::2]
S = input[1::2]

for case in range(test_case):
    first, second = 0, 0
    counter = 0
    while True:
        # calculate the total distance of houses(each 0) to first trashbin(1)
        if first == 0:
            first = S[case].find('1')
            counter += int((first+1)*first/2)
        second = S[case].find('1', first+1)
        if second == -1:
            break
        # calculate the total distance of houses(each 0) between two trashbin(1)
        if second-first == 1:
            first = second
            continue        
        elif (second-first)%2 == 0:
            counter += ((second-first)/2)*((second-first)/2)
        else:
            counter += ((second-first-1)/2)*((second-first-1)/2)+(second-first-1)/2
        first = second
    # calculate the total distance of houses from(each 0) last trashbin(1)
    if first != int(N[case])-1:
        counter += (int(N[case])-1-first)*(int(N[case])-first)/2
          
    print("Case #"+str(case+1)+": " +str(int(counter)))
