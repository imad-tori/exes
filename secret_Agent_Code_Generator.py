code1 = input("enter code1: ").lower()
code2 = input("enter code2: ").lower()
code3 = input("enter code3: ").lower()
numA = int(input("enter numA: "))
numB = int(input("enter numB: "))

if not code1.isalpha() or not code2.isalpha() or not code3.isalpha():
    print("Invalid codeword")
    
elif numA < 1 or numB < 1:
    print("Invalid numbers")

else:
    combined = code1 + "-" + code2 + "-" + code3
    secret_number = (numA * numB) + numA - numB
    swapped_A, swapped_B = numB, numA
    avg_value = (numA + numB)/2
    message_length = len(combined)

    cleaned_combined= combined.replace("-","")
    rev_combined=cleaned_combined[::-1]
    is_palindrome = False
    if rev_combined == cleaned_combined:
        is_palindrome = True

    print(f"Secret Code: {combined}") 
    print(f"Secret Number: {secret_number}") 
    print(f"Swapped Values: A={swapped_A}, B={swapped_B}") 
    print(f"Average of Originals: {avg_value}") 
    print(f"Combined Length: {message_length}") 
    print(f"Palindrome: {is_palindrome} ")