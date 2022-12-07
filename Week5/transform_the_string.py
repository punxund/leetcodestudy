#https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008da461
#2022-12-07 Hongsik Kim

# get input and save in the string_list and target_list.
case_number = int(input())
input_ = list(input() for _ in range(case_number*2))
string_list = []
target_list = []
for i in range(len(input_)):
    if input % 2 == 0:
         string_list.append(input_[i])
    else:
        target_list.append(input_[i])

# function that changing target string to target number list. 
def target_to_number(Target):
    target_number = []
    for char in Target:
        number = ord(char) # using ord function get the number of character
        target_number.append(number)
        target_number.append(number-26) # becauese it is cyclic 
        target_number.append(number+26) 
        #print(target_number)
    return target_number

# function that finding nearest alphabet with target number list.
def to_nearest_alphabet(char, number_list):
    char_number = ord(char)
    to_nearest = float('inf')
    for number in number_list: # update nearest alphabet
        if abs(char_number-number) < to_nearest: 
            to_nearest = abs(char_number-number)
    #print(to_nearest)
    return to_nearest

# case by case add the count of each character to neareat target alphabet. 
for case in range(case_number): # O(lmn), n cases --> lmn is length of input.
    count = 0     
    target_number_list = target_to_number(target_list[case]) # O(m), m is length of target
    for char in string_list[case]: # O(lm), l is length of string
        if char not in set(target_list[case]):
            count += to_nearest_alphabet(char, target_number_list) # O(m)  

    print('Case #'+str(case + 1)+': '+str(count))