rows=5

for i in range(1 , rows+1):
  print(' '*(rows-i) * 2, end='')
  
  for j in range(i):
    print("*" , end='  ')
  print()