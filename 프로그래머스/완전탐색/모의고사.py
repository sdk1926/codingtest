def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    answer = [0,0,0]
    real_answer = []
    for i in range(len(answers)):
        if answers[i] == a[i % 5]:
            answer[0] += 1
        if answers[i] == b[i % 8]:
            answer[1] += 1
        if answers[i] == c[i % 10]:
            answer[2] += 1
            
    for j, k in enumerate(answer):
        if k == max(answer):
            real_answer.append(j+1)
            
    return real_answer