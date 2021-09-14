# import sys
# dic = {"muzi":{1,2,3,4,5,4}}
# print(dic)
# i = "muzi prodo"
# i = i.split()
# dic[i[0]].add(i[1])
# print(dic)
# id_list = ["neo","prodo", "peach","neo","prodo", "peach","neo","prodo", "peach"]
# dic = {i : {} for i in id_list}
# print(dic)
# from collections import Counter
# counter=Counter(id_list)
# print(counter)
# ans = []
# for k,v in counter.items():
#     if v >= 3:
#         print(k)

from collections import Counter
def solution(id_list, report, k):
    answer = []
    dic = {i : set() for i in id_list}
    report_user = []
    report_user1 = []
    for i in report:
        i = i.split()
        dic[i[0]].add(i[1])        
    for j in dic.values():
        j = list(j)
        for u in j:
            report_user.append(u)
    counter = Counter(report_user)
    for l,m in counter.items():
        if int(m) >= k:
            report_user1.append(l)      
    for p in dic.values():
        p = list(p)
        y = 0
        for z in report_user1:
            q = p.count(z)
            y += q
        answer.append(y)
    print(answer)
solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)