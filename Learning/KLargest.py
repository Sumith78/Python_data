import heapq
def find_kth_largest(arr,k):
  return heapq.nlargest(k,arr)[-1]

arr=[3,3,1,5,6,4]
k=2
print(find_kth_largest(arr,k))

#two highest elements are checked in decending order and then -1 is used to take the last element [6,5] , -1= 5

