#BinarySearch Without Using Recursion
#TimeComplexity = O(log n)
#SpaceComplexity = O(1)
def BinarySearch(arr,x,l,r):
  while l<=r:
    mid = (l+r)//2
    if arr[mid] == x:
      l = r+1
      return mid
    elif arr[mid] < x:
      l = mid +1
    else:
      r = mid -1
  return -1

arr = [2,4,6,8,9,11,22,32,42,48]
x =42
l = 0
r = len(arr)-1
ans = BinarySearch(arr,x,l,r)
print("Searching Element is Found At: ",ans)