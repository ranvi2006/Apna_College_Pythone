# Take 3 number input form the user and find garetest number

a=int(input("Enter first number : "))
b=int(input("Enter secound number : "))
c=int(input("Enter third number : "))

if(a>=b):
    if(a>=c):
        print("Gratest number is : ",a)
    else:
        print("Gratest number is : ",c)
else:
    if(b>=c):
        print("Gratest number is : ",b)
    else:
        print("Gratest number is : ",c)