# trucks = [7,4,5,6]
# length = 2
# weight = 10

# i = 0
# j = 0
# 도로 = []
# a = trucks[0]

# while trucks or 도로: 

#     def 채워주기(도로):
#         global length
#         while len(도로)+1 <= length and sum(도로)+a <= weight:
#             도로.append(a)
#             print(도로)
#             trucks.pop(0)
#             print(trucks)

#         return 도로 
    
#     채워주기(도로)
#     도로.pop(0)
#     length += 1 

def solution(bridge_length, weight, truck_weights):
    a = [0] * bridge_length
    answer = 0
    trucks = truck_weights
    while a:
        a.pop(0)
        answer+=1
        if trucks:
            if sum(a) + trucks[0] <= weight:
                a.append(trucks.pop(0))
            else:
                a.append(0)
                
    return answer









