##Prices Question
#T(n)=O(n)
def get_max(prices):
  min = float('inf')
  max = 0
  for i in range(len(prices)):
    if prices[i] < min:
      min = prices[i]
    elif prices[i] - min > max:
      max = prices[i]-min
  return max

prices = [7,1,5,3,6,4]
a=get_max(prices)
print(f"Maximum Profit is ",a)