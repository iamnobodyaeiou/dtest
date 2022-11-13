from time import time

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]   # n rows X W columns table or 2d array
  
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:  # first row and first column is always 0
                K[i][w] = 0

            elif wt[i-1] <= w:   
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])   # 2nd parameter in max ie K[i-1][w] means table mein apne upar vali value
                # 1st parameter in max means upar toh jaana hi hai aur weight se apna weight minus karna hai aur apni value add karni hai

            else:
                K[i][w] = K[i-1][w]   # upar ki 2 conditions fail huyi toh apne upar vale ki value copy karni hai
  
    return K[n][W]    # ye table ka last row aur last column ka element return karega
    # return K      # not required (just for understanding)

def test_time_complexity():
  val = [60, 100, 120]
  # weights must be written in ascending order   ***this is very important***
  wt = [10, 20, 30]
  W = 50
  n = len(val)
  print(knapSack(W, wt, val, n))

start = time()
test_time_complexity()
print("DP: ", (time()-start), "sec")
    
