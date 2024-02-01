n1=int(input("Enter first number :"))
n2=int(input("Enter second number :"))
op=input("Enter option 1.Addition 2.Subtraction 3.Multiplication 4.Division :")
if(op=='1'):
    res=int(n1+n2)
elif(op=='2'):
    res=int(n1-n2)
elif(op=='3'):
    res=int(n1*n2)
elif(op=='4'):
    res=int(n1/n2)
print("Result=",res)