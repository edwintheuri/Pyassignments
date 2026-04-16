import math, random 
### 
# This is a simple Calculator that  Does Basic Arithmetic
# Shows a random number 
# shows a finds squareroot
# ###
num1=input("num1, no decimals:\n")    
num1_init=int(num1) 
op = input("Add,Subtract,multiple,divide:\n") 
num2=input("num2, no decimals:\n") 
num2_init=int(num2) 
if op == "+" :  
    print(num1_init+num2_init)




#finding a square root of any input
print(math.sqrt(int(input("Enter a number for Square root : ")))) 

#finding a random number between,including 1 and 100, 1-100
print(random.randint(1,100))