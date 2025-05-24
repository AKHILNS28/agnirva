def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j];

lis=[1,5,7,5,3,8,0,3]
bubblesort(lis)
print(lis)