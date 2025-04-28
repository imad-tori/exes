my_list = [3,4,1,2,6,3,8,3,5,2,4,8,7]
my_list.append(11)
my_list.remove(5)
my_list.insert(2,3)

print(f"the sum of the list is: {sum(my_list)}")

largest = my_list[0]
smallest = my_list[0]

for num in my_list:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(f"the largest number in the list is: {largest},\nthe smallest number in the list is: {smallest}")