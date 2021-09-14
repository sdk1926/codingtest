# from datetime import datetime
# time_1 = datetime.strptime('05:00',"%H:%M")
# time_2 = datetime.strptime('07:55',"%H:%M")
# time = time_2 - time_1
# print(time)
# print(int(time.seconds)//60)

# dic = {}
# i = ["fefef", "wefwef", "wefwef"]
# dic[i[1]] = i

from datetime import datetime
import math
def solution(fees, records):
    dic = {}
    for i in records:
        i = i.split()
        dic[i[1]] = []
    for j in records:
        j = j.split()
        dic[j[1]].append([j[0],j[2]])
    for k, m in dic.items():
        min = 0 
        if len(m) % 2 == 0:
            while m:
                A = m.pop()
                B = m.pop()
                time_1 = datetime.strptime(A[0],"%H:%M")
                time_2 = datetime.strptime(B[0],"%H:%M")
                time = time_1 -time_2
                minute = int(time.seconds)//60
                min += minute
        else:
            while m:
                A = m.pop(0)
                if m:
                    B = m.pop(0)
                    time_1 = datetime.strptime(A[0],"%H:%M")
                    time_2 = datetime.strptime(B[0],"%H:%M")
                    time = time_2 - time_1
                    minute = int(time.seconds)//60
                    min += minute
                else:
                    time_1 = datetime.strptime(A[0],"%H:%M")
                    time_2 = datetime.strptime("23:59","%H:%M")
                    time = time_2 - time_1
                    minute = int(time.seconds)//60
                    min += minute
        dic[k] = min
        
    dic = sorted(dic.items())
    answer = []
    for o in dic:
        if o[1] <= fees[0]:
            answer.append(fees[1])
        else:
            z = fees[1] + (math.ceil((o[1]-fees[0])/fees[2]) * fees[3])
            answer.append(z)
    return answer

solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
solution([1, 461, 1, 10],["00:00 1234 IN"])