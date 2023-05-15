num = int(input("Enter the number\n"))
result= ""
while(num>0):
   temp = num%2
   result += str(temp)
   temp = 0
   if(num%2!=0):
     num=(num-1)//2
   else:
     num=num//2
result = result[::-1]
print(result)
     

   
  
  