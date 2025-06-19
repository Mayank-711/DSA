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
    else:
      left = mid +1
  return index_of_one


arr = [0,0,0,1,1,1,1]
ans = firstone(arr)
print(ans)