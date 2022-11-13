from time import time

def fibonacci(n): #(Iterative) Non recursive fibonacci function
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    return fib_list[n]

def fibonacci_recursive(n):    #Recursive fibonacci function
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_recur_list[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return fib_recur_list[n]

N = 20
RUNS = 1000
print(f"Given N = {N}\n{RUNS} runs")
fib_list = [0] * (N + 1)
fib_list[0] = 0
fib_list[1] = 1

# non recursive
start = time()
for i in range(RUNS):
  fibonacci(N)
duration = time()-start

print("Fibonacci non-recursive:", fibonacci(N), "\tTime:", duration, "sec")

# recursive
fib_recur_list = [0] * (N + 1)
# fib_recur_list[0] = 0     # not required as its a recursive function
# fib_recur_list[1] = 1

start = time()
for i in range(RUNS):
  fibonacci_recursive(N)
duration = time()-start

print("Fibonacci Recursive:\t",fibonacci_recursive(N),"\tTime:", duration, "sec")
