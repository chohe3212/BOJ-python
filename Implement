score = []
for _ in range(20):
    score.append(input().split(" "))

total = 0
sum = 0
for i in score:
    if i[2] == "P":
        continue
    sum += float(i[1])
    if i[2] == "A+":
        total += float(i[1]) * 4.5
    elif i[2] == "A0":
        total += float(i[1]) * 4.0
    elif i[2] == "B+":
        total += float(i[1]) * 3.5
    elif i[2] == "B0":
        total += float(i[1]) * 3.0
    elif i[2] == "C+":
        total += float(i[1]) * 2.5
    elif i[2] == "C0":
        total += float(i[1]) * 2.0
    elif i[2] == "D+":
        total += float(i[1]) * 1.5
    elif i[2] == "D0":
        total += float(i[1]) * 1.0
    elif i[2] == "F":
        total += float(i[1]) * 0 
    

print(round(total / sum, 6))
