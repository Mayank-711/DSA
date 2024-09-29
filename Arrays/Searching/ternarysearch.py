##ternary search using recursion Time complexity ,T(n) = O(log n base 3 )

def ternary(arr,i,j,key):
    mid1 = (i+j)//3
    mid2= j-(j-i)//3
    while i<=j:
        if arr[mid1]==key:
            return mid1
        if arr[mid2]==key:
            return mid2
        ##First Part of ternary search
        elif arr[mid1] > key:
            return ternary(arr,i,mid1-1,key)
        #third part of ternary search
        elif arr[mid2] < key:
            return ternary(arr,mid2+1,j,key)
        #second part of ternary search
        else:
            return ternary(arr,mid1+1,mid2-1,key)
    return -1

arr = [2,4,5,7,8,18,20,29,41]
i = 0
j = len(arr)-1
key = 29
ans = ternary(arr,i,j,key)
print(ans)