def linear(arr,k):
    for i in range(len(arr)):
        if(arr[i]==k):
            print("Found at index ",i)

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

a1=[2,1,5,3,7,45,3,2]
a2=[12,45,67,100,140]

linear(a1,3)
bin(a2,67)
