def reversed_list(array):
    reversed_array=[]
    for i in range(len(array)-1,-1,-1):
        reversed_array.append(array[i])
    return reversed_array
print(reversed_list([30,40,50,60,70,80]))