#Find Element in An Matrix Sorted From LEft to right - Bruteforce Approach O(n^2)
def search(arr,target):
  for row in arr:
    for element in row:
      if element == target:
        return True
  return False


arr = [[2,3,4],[7,8,9],[14,15,16],[17,18,19]]
target =3
ans = search(arr,target)
print(ans)