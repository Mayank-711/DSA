#BinarySearch Using Recursion
#TimeComplexity = O(log n)
#SpaceComplexity = O(log n) Because of Recursive Stack
def BinarySearch(arr,x,l,r):
  mid = (l+r)//2
  if arr[mid] == x:
    l = r+1
    return mid
  elif arr[mid] < x:
    return BinarySearch(arr,x,mid+1,r)
  else:
    return BinarySearch(arr,x,l,mid-1)
  return -1

arr = [2,4,6,8,9,11,22,32,42,48]
x = 11
l = 0
r = len(arr)-1
ans = BinarySearch(arr,x,l,r)
print("Searching Element is Found At: ",ans)