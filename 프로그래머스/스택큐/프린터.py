from collections import deque
priorities = [2,2,2,2,2,2]
location = 3
#c = [i for i in range(len(priorities))]
def solution(priorities, location):
    max_num = max(priorities)
    b = [i for i in enumerate(priorities)]
    index = 0
    i = 0
    while b:
        popnum = b.pop(0)
        if popnum and popnum[1] < max_num:
            b.append(popnum)
        elif popnum and popnum[1] >= max_num:
            max_num = max(b)
            if popnum[0] == location:
                return index + 1
            index += 1       
        
print(solution(priorities,location))

# for i in range(len(priorities)):
#     if b[i][0] == location:
#         answer = i + 1
#         print(answer)

# print(b)

