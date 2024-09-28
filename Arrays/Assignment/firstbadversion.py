#FirstBadVersion
def firstone(arr):
  left = 0
  right = len(arr) - 1
  index_of_one = 0
  while left<= right:
    mid = (left+right)//2
    if arr[mid] == 1:
      index_of_one = mid
      right = mid -1
      print("right in if ",right)
    elif arr[mid] ==0 :
      left = mid +1
      print("left in elif ",left)
    else:
      return None
  return index_of_one


arr = [0,0,0,1,1,1,1]
ans = firstone(arr)
print(ans)