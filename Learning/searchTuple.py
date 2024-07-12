
num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Search the number: "))
idx=0
for val in num:
  if(val==x):
    print("number found at index: ",idx)
    break
  idx +=1
 