def solution(n, lost, reserve):
    answer = int(n)-len(lost)
    reserve_list = reserve
    lost_list = lost
    for i in reserve_list:
        for l in lost_list:
            if l == i:
                lost_list.remove(l)
                reserve_list.remove(i)
            else:
                break

    for i in reserve_list:
        for l in lost_list: 
            if l == (i-1): 
                answer += 1 
                lost_list.remove(l)
                reserve_list.remove(i) 
                print(lost_list)
                print(reserve_list)

    for i in reserve_list:
        for l in lost_list:
            if l == (i+1):
                print('dwdw')
                answer += 1 
                lost_list.remove(l)
                reserve_list.remove(i) 

                
                              
    return answer


answer = solution(5, [2,4], [1,3,5])

print(answer)