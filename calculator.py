num1 = int(input("Enter the number 1 : "))
operator = str(input("Enter the operator +,-,*,**,/,%,// : "))
num2 = int(input("Enter the number 2 : "))
if operator == "+":
    print("The addition of two number is" , num1+num2)
elif operator == "-":
  print("The subtraction of two number is" , num1-num2)
elif operator == "*":
  print("The multiplication of two number is" , num1*num2)
elif operator == "**":
  print("The exponent of two number is" , num1**num2)
elif operator == "/":
  print("The division of two number is" , num1/num2)
elif operator == "%":
  print("The modulus of two number is" , num1%num2)
elif operator == "//":
  print("The floor division of two number is" , num1//num2)
else:
  print("please enter the correct operator ")

