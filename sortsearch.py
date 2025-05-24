def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j];

def bin(arr,k):
    n=len(arr)
    l=0
    r=n-1
    while(r>=l):
        mid=(l+r)//2
        if(k>arr[mid]):
            l=mid+1
        elif(k<arr[mid]):
            r=mid-1
        else:
            print("found at ",mid)
            break

a1=[23,45,26,10,32,56,39]
bubblesort(a1)
print(a1)
bin(a1,23)