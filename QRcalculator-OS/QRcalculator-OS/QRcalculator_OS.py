# QR Code Reader
# Author: Johnjimy Som
# Created: June 3, 2021
  
import math

# Initialising hex string
ini_string = "11109D6B2700A000200000E000000000" #sample
  
#ini_string = input('Please insert a hexcode: ')#import the hex here

  
# Printing initial string
# Step 1 Step1  QR code(16進数)を読み取る
print ("Initial string:", ini_string)
  
# Code to convert hex to binary
#Step2  読み取ったQR code(16進数)を2進数へ変換する
n = int(ini_string, 16) 
binaryStr = ''
while n > 0:
    binaryStr = str(n % 2) + binaryStr
    n = n >> 1    
result = binaryStr
  
# Print the resultant string
print ("\nResultant string [Binary]:", str(result))

#00010001000100001001110101101011001001110000000010100000000000000010000000000000000000001110000000000000000000000000000000000000
# Print binary characters start[9]-[34]length should be : 00010000100111010110101100
print ("\nResultant string [9-34] [Binary]:", str(result[1:]))

#Step3　2進数に変換した結果を、項目毎にデータを区切る
# import module
from tabulate import tabulate #unresolved import <'from tabulate'>

# assigned binaryStr data
mydata = [{"Encode Version", "x","x","y"}, 
          {"Print Area", "wololo","xxx","yyyu"}, 
          {"Item Code", "xx","yy","zz"}]
  
# create header
head = [" ", "City", "Binary", "Value(Decimal)"]
  
# display table
print(tabulate(mydata, headers=head, tablefmt="pretty"))