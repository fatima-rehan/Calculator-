#Fatima Rehan
#November 1st, 2022
#Python Calculator 
#This program will add, subrtact, multiply, and divide two numbers. 

print("Enter '+' to add, '-' to subtract, 'x' to multiply, and '/' to divide")
operation =input()
print("enter your number")
val1 = float(input())
print("enter your second number") 
val2 = float(input())

if operation == "+":                                           # "+" will be used to add
   added = val1 + val2                                         #numbers will be added
   print("you two numbers added equals", added)                
   added2 = round(added)                                       #sum rounded to decimal
   binary = bin(added2)                                        #sum will be converted to binary
   hexa = hex(added2)                                          #sum will be converted to hexadecimal
   print("the answer in binary is", binary)
   print("the answer in hexadecimal is", hexa)
         
elif operation == "-":                                         # "-" will be used to subtract 
   subtracted = val1 - val2                                    #numbers will be subtracted
   print("your two numbers subtracted equals", subtracted)
   subtracted2 = round(subtracted)                             #difference rounded to decimal
   binary = bin(subtracted2)                                   #difference will be converted to binary
   hexa = hex(subtracted2)                                     #difference will be converted to hexadecimal
   print("the answer in binary is", binary)
   print("the answer in hexadecimal is", hexa)   
    
elif operation == "x":                                         # "x" will be used to multiply
    multiplied = val1 * val2                                   #numbers will be multiplied
    print("your two numbers multiplied equals", multiplied)
    multiplied2 = round(multiplied)                            #product will be rounded to decimal
    binary = bin(multiplied2)                                  #product will be converted to binary
    hexa = hex(multiplied2)                                    #product will be converted to hexadecimal
    print("the answer in binary is", binary) 
    print("the answer in hexadecimal is", hexa)    
    
elif operation == "/":                                         # "/" will be used to divide
    divided = val1 / val2                                      #numbers will be divided
    print("your first number divided by your second number equals", divided, "in decimal") 
    divided2 = round(divided)                                  #quotient will be rounded to decimal
    binary = bin(divided2)                                     #quotient will be converted to binary
    hexa = hex(divided2)                                       #quotient will be converted to hexadecimal
    print("the answer in binary is", binary)
    print("the answer in hexadecimal is", hexa)    

else: 
    print("you put in the wrong key, error")                   #if wrong key is entered, errr statement will show" 
    