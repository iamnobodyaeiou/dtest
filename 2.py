import heapq
from time import time

class node:
  def __init__(self, freq, symbol, left = None, right = None):
    self.freq = freq
    self.symbol = symbol
    self.left = left
    self.right = right
    self.huff = ''

  def __lt__(self, nxt):
    return self.freq<nxt.freq

def printNodes(node, val = ''):
  newVal = val + str(node.huff)

  # checking left and right and printing them
  if(node.left):
    printNodes(node.left, newVal)
  if(node.right):
    printNodes(node.right, newVal)

  # if both left right are null then print newVal
  if(not node.left and not node.right):
    print(f"{node.symbol}--->{newVal}")

def test_time_complexity():
    chars = ['a','b','c','d','e','f']
    freq = [5, 9, 12, 13, 16, 45]

    nodes = []   # this list is used for heap
    for i in range(len(chars)):
        heapq.heappush(nodes, node(freq[i], chars[i]))   # adding all node to the nodes heap priority queue

    while len(nodes)>1:
      left = heapq.heappop(nodes)   # popping two smallest elements from the min heap
      right = heapq.heappop(nodes)

      left.huff = 0   # setting left and right huff values to 0 and 1
      right.huff = 1

      newNode = node(left.freq+right.freq, left.symbol + right.symbol, left, right)   # creating a new node by adding 2 minimum nodes
      heapq.heappush(nodes, newNode)      # pushing the new node in the heap

    printNodes(nodes[0]) 

RUNS = 1

start = time()
test_time_complexity()
print("Huffman Encoding Time:", time()-start, "sec")

