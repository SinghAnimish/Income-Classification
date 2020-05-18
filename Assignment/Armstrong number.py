#Program to find a given number is Armstrong number or not.

num=int(input("Enter a number:- "))
sum=0
temp=num
length= len(str(num))
while(temp>0):
    digit=temp%10
    sum=sum+(digit**length)
    temp=temp//10

if(sum==num):
    print("Armstrong number")
else:
    print("Not a armstrong number")
    
