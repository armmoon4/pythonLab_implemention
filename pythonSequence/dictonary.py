n = int(input())
student_dict = {}
for i in range(n):
    record = input().split()
    name = record[0]
    scores = list(map(float, record[1:]))
    student_dict[name] = scores
query_name = input()
scores = student_dict[query_name]
average_score = sum(scores) / len(scores)
print("{:.2f}".format(average_score))
