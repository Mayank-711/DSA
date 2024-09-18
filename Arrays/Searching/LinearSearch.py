#LinearSearch
#timecomplexity = O(n)
#spacecomplexity = O(1)
def linearsearch(arr,x):
  n = len(arr)
  for i in range(n-1):
    if arr[i]==x:
      return i
  return -1

arr = [26,24,32,29,11,6,89,92]
x = 11
ans = linearsearch(arr,x)
print("Searching element is found at index: " ,ans)