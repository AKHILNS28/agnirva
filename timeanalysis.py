import time


def bub(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

a1=[1,2,56,34,26,87,2,3,107,102]

start=time.time()
bub(a1.copy())
end=time.time()
print("Time taken by buublesort is ",end-start)

start=time.time()
a1.sort()
end=time.time()
print("Time taken by sort is ",end-start)
