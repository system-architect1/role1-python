num=int(input("Enter a number: "))
if num%2==0:                #modulous(%) gives u the remainder
    print("Even")
else:
    print("Odd")







    #NOTES:
#float number? error int expected
#input 10^18? Python handles big ints
#no else? possible but 2 checks
#bitwise ? if num & 1==0: print("even") # faster and low level check
#to check multiple numbers? u need loop