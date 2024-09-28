#Find Element in An Matrix Sorted From LEft to right - O(log (m*n))
def search(arr,target):
  m = len(arr)
  if m == 0:
    return False
  n = len(arr[0])
  left,right = 0,m*n-1
  while left <= right:
    mid = (left + right)//2
    mid_element = arr[mid//n][mid%n]
    if mid_element == target:
      return True
    elif mid_element < target:
      left = mid + 1
    else:
      right = mid - 1
  return False
arr = [[2,3,4],[7,8,9],[14,15,16],[17,18,19]]
target =3
ans = search(arr,target)
print(ans)