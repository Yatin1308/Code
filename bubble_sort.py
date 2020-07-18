def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print("Sorted array is : ")
for i in range(len(arr)):
    # print(arr[i])
    print("%d" % arr[i])

    # 2nd way to bubble sort


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1, 0, -1):
        for i in range(passnum):
            if nlist[i] > nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp


nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
bubbleSort(nlist)
for list in nlist:
    print(list)
