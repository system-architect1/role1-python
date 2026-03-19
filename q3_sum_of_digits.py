num=int(input("Enter the number: "))
num=abs(num)
digit_sum=0
while num>0:
    digit=num%10
    digit_sum+=digit
    num=num//10
if digit_sum%2==0:
    print("Even Sum")
else:
    print("Odd Sum")