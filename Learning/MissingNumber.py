def find_number(arr):
  n= len(arr)+1
  total_sum = n*(n+1)//2
  arr_sum=sum(arr)
  return total_sum-arr_sum

arr=[1,2,3,5,6]
print(f"The missing Number is : {find_number(arr)}")