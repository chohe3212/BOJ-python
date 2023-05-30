N, M = map(int,input().split())
ans = []

def back():
    if len(ans) == M:
      print(" ".join(map(str, ans)))
      return
    for i in range(1, 1+N):
       if len(ans) == 0:
          ans.append(i)
          back()
          ans.pop()
       elif i not in ans and i > ans[-1]:
          ans.append(i)
          back()
          ans.pop()

back()  