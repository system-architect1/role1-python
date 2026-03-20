num=int(input("Enter a number: "))
if num>0:
    if num%2==0:
        print("Positive even")
    else:
        print("Positive odd")
elif num<0:
    if num%2==0:
        print("Negative even")
    else:
        print("Negative odd")
else:
    print("Zero")