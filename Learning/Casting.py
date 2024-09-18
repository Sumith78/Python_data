##Casting: Converting one data type to another data type. We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.

# int to float
num_int = 10
print('num_int',num_int)                         
num_float = float(num_int)
print('num_float:', num_float)             

# float to int
gravity = 9.81
print(int(gravity))            

# int to str
num_int = 10
print(num_int)                
num_str = str(num_int)
print(num_str)                  

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      
print('num_float', float(num_str))  

# str to list
first_name = 'Asabeneh'
print(first_name)              
first_name_to_list = list(first_name)
print(first_name_to_list)            