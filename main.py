import random
import matplotlib.pyplot as plt
import math

# tracks number of steps
# roughly equal to the time complexity of the algorithm
class stepCounter:
  numSteps = 0

  def step(self):
    self.numSteps = self.numSteps + 1

  def reset(self):
    self.numSteps = 0

  def getSteps(self):
    return self.numSteps

steps = stepCounter()

# 2 parts: heaping and sorting
# sorting in place
# to avoid using extra memory 
def heapsort(arr):
  heapify(arr)
  end = len(arr) - 1

  # O(n)
  while end > 0:
    steps.step()

    arr[end], arr[0] = arr[0], arr[end]
    end = end - 1
    siftdown(arr,0,end)

  return arr

# builds max heap
# where each value in the parent node is greater than its children
def heapify(arr):
  
  count = len(arr)
  start = getParent(count - 1)

  # O(n)
  while start >= 0:
    siftdown(arr,start,count-1)
    start = start -1
    steps.step()

def getParent(index):
  return (index-1)//2 

def leftchild(i):
  return 2*i + 1

# O(logn) used in sorting and heaping parts
# sifts values so that the parent value is greater than its children
# operation used on heap
def siftdown(arr,start,end):
  root = start
  while leftchild(root) <= end:
    steps.step()

    child = leftchild(root)
    swap = root
    
    if arr[swap] < arr[child]:
      swap = child
    if child+1 <= end and arr[swap] < arr[child+1]:
      swap = child + 1
    if swap == root:
      return
    else:
      arr[root], arr[swap] = arr[swap], arr[root]
      root = swap 


# size of list sorted are a tenth of N
# comparison with O(n), O(nlogn) and O(n^2)
def printSort(N):

  stepArr = []
  tenth = N//10
  n = [tenth, 2*tenth, 3*tenth , 4*tenth, 5*tenth, 6*tenth, 7*tenth, 8*tenth, 9*tenth, N ]

  n2 = [i*i for i in n]

  for i in n:
    steps.reset()

    arr1 = list(range(i))
    random.shuffle(arr1)
    sortedList = heapsort(arr1)
    numSteps = steps.getSteps()

    stepArr.append(numSteps)


  fig = plt.figure()
  fig,ax = plt.subplots()

  ax.plot(n,stepArr, label='Heap Sort')
  ax.plot(n,n, label='Linear')
  ax.plot(n, n2, label='n Squared')
  
  ax.set(xlabel='List Size', ylabel='Number of Steps', title='Complexities')
  ax.grid()
  ax.legend()

  plt.savefig('algorithms.png')

printSort(100)