"""Given a positive integer num, write a program that returns True if num is a perfect  /
square else return False. Do not use built-in functions like sqrt. Also, talk about the time
complexity of your code."""
def findcomplete_square(num):
  if num ==0 or num == 1:
    return True
  left = 1
  right = num
  while left<right:
    mid = (left + right)//2
    if mid * mid ==num:
      return True
    elif mid *mid> num:
      right = mid -1
    else:
      left = mid +1
  return False

num = 14
ans = findcomplete_square(num)
print(ans)