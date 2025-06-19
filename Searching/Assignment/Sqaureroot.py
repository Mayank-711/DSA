#SquareRoot using Binary Search
def squareroot(n):
  if n ==1 or n ==0:
    return n
  start = 1
  end = n
  while start <= end:
    mid = (start + end)//2
    if mid*mid == n:
      return mid
    elif mid *mid < n:
      start = mid+1
    else:
      end = mid-1
  return end

n = [4,8,9,6,15,21]
for a in n: 
  ans = squareroot(a)
  print(ans)