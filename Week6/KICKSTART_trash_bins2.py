# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887c32
# 2022-12-13 Hongsik Kim


from bisect import bisect_left, bisect_right
# get input and split the case
test_case = int(input())
input = [input() for _ in range(test_case*2)]
N = input[0::2]
S = input[1::2]

for case in range(test_case):

    trashbin = []
    for house in range(int(N[case])):     
        if S[case][house] == '1':
            trashbin.append(house)

    counter = 0
    for house in range(int(N[case])):
        if S[case][house] == '0':
            L = bisect_left(trashbin, house)-1            
            R = bisect_right(trashbin, house)
            if house < trashbin[0]:
                counter += abs(house-trashbin[R])
            elif house > trashbin[-1]:
                counter += abs(house-trashbin[L])
            else :
                counter += min(abs(house-trashbin[L]), abs(house-trashbin[R]))                      
            #print(counter)
            
    print("Case #"+str(case+1)+": " +str(counter))

# for case in range(test_case):

#     trashbin = []
#     for house in range(int(N[case])):     
#         if S[case][house] == '1':
#             trashbin.append(house)

#     counter = 0
#     for house in range(int(N[case])):
#         if S[case][house] == '0':
#             to_neighbor = float('inf')
#             for who in trashbin:
#                 if abs(house-who) < to_neighbor:
#                     to_neighbor = abs(house-who)
#             counter += to_neighbor

#     print("Case #"+str(case+1)+": " +str(counter))
