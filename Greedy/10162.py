T = int(input())

A = T//300
B = (T%300)//60
C = (T%60)//10



if T%10 !=0:
    print(-1)
else:
    print(A,B,C)