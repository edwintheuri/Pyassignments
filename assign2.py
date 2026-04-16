
#This exercise handles printing user input ,
#Finding hourly rate ,
#Calculating and matching statements with their types , 
#lastly converts users temp





#Exercise 1

hello= input("Enter your name :")
print(f"Hello {hello}")

#Exercise 2

def Pay ():
    hours=float(input("Enter Hours worked :"))
    rate=float(input("Enter your rates :"))
    pay = hours * rate
    print(f"Pay :{pay}")
Pay()    

#Exercise 3


width = 17
height = 12.0

findingfloor=width//2
decimaldivison=width/2.0
intergerdiv=width/3
expression=1+2*5

print(f"Value : {findingfloor} Type : {type(findingfloor)}")
print(f"Value : {decimaldivison} Type : {type(decimaldivison)}")
print(f"Value : {intergerdiv} Type : {type(intergerdiv)}")
print(f"Value : {expression} Type : {type(expression)}")



#Exercise 4

temp=float((input("Enter Temp in degrees:")))

temp_farehn= temp*(9/5)+32 #formula to farenheit 
print(f"{temp_farehn}") 