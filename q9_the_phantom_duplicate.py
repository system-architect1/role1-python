def singleNumber(nums):
    ones=0
    twos=0
    for num in nums:
        ones=(ones^num) & ~twos
        twos=(twos^num) & ~ones
    return ones
nums=list(map(int,input("Enter numbers:").split()))
print("Single number is:",singleNumber(nums))