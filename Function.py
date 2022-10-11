from unittest import result


def printfunc():
    print("Hello ! This my first python function")

def power_func(num,exp):
    result= num**exp
    return result

n=3
e=4

print(power_func(n,e))

def math_ops(num1,num2):
    add=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1/num2
    return add,sub,mul,div

n1,n2=7,3

add,sub,mul,div=math_ops(n1,n2)

print("addition of", n1," + ",n2,"=",add)
print("subtraction of", n1," - ",n2,"=",sub)
print("multiplication of", n1," * ",n2,"=",mul)
print("division of", n1," / ",n2,"=",div)


