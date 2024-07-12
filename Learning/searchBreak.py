nums=[1,4,9,16,25,36,49,64,81,100]

x=int(input("Search Number: "))
i=0
while i<len(nums):
  if(nums[i]==x):
    print("The number is at idx: ",i)
    break
  else:
     print("number not found in list")
  i +=1