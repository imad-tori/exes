# def fibonacci(n):
#     res = [1,1]
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1,1]
#     for i in range(n-2):
#         res.append(res[i]+res[i+1])
#     return res

def fibonacci(n):
    
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    f_list=fibonacci(n-1)
    return (f_list+[f_list[-1]+f_list[-2]])
    
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))