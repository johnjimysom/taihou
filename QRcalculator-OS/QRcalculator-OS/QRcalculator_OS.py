# Python code to demonstrate 
# conversion of hex string
# to binary string
  
import math

# Initialising hex string
#ini_string = "11109D6B2700A000200000E000000000" #sample
  
ini_string = input('Please insert a hexcode: ')

  
# Printing initial string
print ("Initial string:", ini_string)
  
# Code to convert hex to binary
n = int(ini_string, 16) 
bStr = ''
while n > 0:
    bStr = str(n % 2) + bStr
    n = n >> 1    
result = bStr
  
# Print the resultant string
print ("\nResultant string [Binary]:", str(result))