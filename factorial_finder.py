#FACTORIAL FINDER
number=int(input("enter the number ="))
result=1
count=0
for i in range(1,number+1):
    result=result*i
    count+=1
    print(count,result)
