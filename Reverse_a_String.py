def reverse_string(text):
    res=""
    i = len(text)-1
    while i >= 0:
        res+=text[i]
        i-=1
    return res
print(reverse_string("hello"))
print(reverse_string("green"))
print(reverse_string("orange"))
