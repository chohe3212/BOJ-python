import sys

def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
        return search
    if len(data) == 1 and search != data[0]:
        return 
    if len(data) == 0:
        return 
    
    medium = len(data) // 2
    if search == data[medium]:
        return search
    else:
        if search > data[medium]:
            return binary_search(data[medium+1:], search)
        else:
            return binary_search(data[:medium], search)

while (1):
    sum_arr = 0
    arr1 = list(map(int,sys.stdin.readline().split()))
    if arr1 == [0]:
        break
    arr2 = list(map(int,sys.stdin.readline().split()))
    del arr1[0]
    del arr2[0]
    arr1.append(10001)
    arr2.append(10001)
    cnt2 = 0
    while(1):
        same_num = binary_search(arr2, arr1[cnt2])
        cnt2 += 1

        if same_num != None:
            if same_num == 10001:
                a=sum(arr1[:arr1.index(same_num)])
                b=sum(arr2[:arr2.index(same_num)])
                if a>b:
                    sum_arr += a
                else :
                    sum_arr +=b
                break

            a=sum(arr1[:arr1.index(same_num)+1])
            b=sum(arr2[:arr2.index(same_num)+1])
            if a>b:
                sum_arr += a
            else :
                sum_arr +=b
            del arr1[:arr1.index(same_num)+1]
            del arr2[:arr2.index(same_num)+1]
            cnt2 = 0

            

    print(sum_arr)


    

