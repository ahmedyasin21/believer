import random
num1 = 3
    
def token():
    """
    generate and return a new value for num1, and 
    save the previous value in num2
    """
    global num1, num2 
    num2 = num1 
    num1 = random.randint(40,90)
    return num1

def vcode():
    """
    return the existing value of num2 (which token() 
    saved as the previous value of num1)
    """
    return num2

print(token(), vcode()) 
print(token(), vcode()) 
print(token(), vcode())