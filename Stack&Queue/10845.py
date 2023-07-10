import sys
N = int(sys.stdin.readline())

data_queue = []

for i in range(N):
  str_input = sys.stdin.readline().split()
  if str_input[0] == "push":
    data_queue.append(str_input[1])
  elif str_input[0] == "pop":
    if len(data_queue) == 0:
      print(-1)
    else:
      print(data_queue.pop(0))
  elif str_input[0] == "size":
    print(len(data_queue))
  elif str_input[0] == "empty":
    print(1) if len(data_queue) == 0 else print(0)
  elif str_input[0] == "front":
    print(data_queue[0]) if len(data_queue) != 0 else print(-1)
  elif str_input[0] == "back":
    print(data_queue[-1]) if len(data_queue) != 0 else print(-1)