string=input("Enter a string:")
if len (string)>1:
    result=string[-1]+string[1:-1]+string[0]
else:
    result=string
print("Result:", result)    
