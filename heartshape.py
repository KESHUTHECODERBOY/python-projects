row = int(input("enter the number of rows: "))
col = int(input("enter the number of col: "))
for r in range(row):
  for c in range(col):
    if (r == 0 and c%3!=0) or (r==1 and c%3==0) or (r-c==2) or (r+c==8):
     print("*",end =" ")
    else:
        print(end=" ")
  print()
  
