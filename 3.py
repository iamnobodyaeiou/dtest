from time import time

class item:
  def __init__(self, value, weight):
    self.value = value
    self.weight = weight

def knapsack(W, arr):
  arr.sort(key = lambda x: x.value/x.weight, reverse = True)

  profit = 0
  for item in arr:

    # If adding Item won't overflow, add it completely
    if item.weight <= W:
      profit += item.value
      W -= item.weight
    
    # If we can't add current Item, add fractional part of it
    else:
      profit = profit + (W * item.value)/ (item.weight)
      break
  
  return profit

def test_time_complexity():
  W = 50
  arr = [item(120, 30), item(60, 10), item(100, 20)]
  print("Maximum Profit:",knapsack(W, arr))

start = time()
test_time_complexity()
print("Fractional knapsack using greedy method: ", (time()-start), "sec")
