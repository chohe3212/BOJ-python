N,M = map(int,input().split())
ans =[]

def back():
  if len(ans) == M:
    print(" ".join(map(str, ans)))
    return
  for i in range(1,1+N):
    ans.append(i)
    back()
    ans.pop()

back()