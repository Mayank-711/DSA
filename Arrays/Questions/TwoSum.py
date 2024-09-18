#Two Sum -Find a+b = 210
#T(n) = O(n) - GreedyMethod
def search(arr,left,right,target):
  while left<=right:
    if arr[left]+arr[right]==target:
      return left,right
    elif arr[left]+arr[right]> target:
      right -= 1
    else:
      left +=1 
  return -1

arr = [20,40,60,80,90,120,240]
left = 0
right = len(arr)-1
target= 200
a,b = search(arr,left,right,target)
print(a,b)