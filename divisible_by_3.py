start = int(input("enter the start number: "))
end = int(input("enter the end number: "))
divisor = int(input("enter the divisor: "))

count = 0
num = start

while num <= end:
    if num % divisor == 0:
        print(num)
        count+=1
    num+=1
    
print(f"the total count of numbers divisible by {divisor} in the range is: {count}")