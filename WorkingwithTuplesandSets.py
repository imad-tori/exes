my_set = {4,2,9,7,1}
my_tuple = (16,4,81,49,1)
my_list = list(my_set)

des_my_list= sorted(my_list, reverse = True)
print(f"set to a list in descending order: {des_my_list}")

intersection_set_tuple = []
for num in my_tuple:
    if num in my_set:
        intersection_set_tuple.append(num)
print(f"intersection-set-tuple: {intersection_set_tuple}")

print(f"length of the tuple: {len(my_tuple)}, length of the set: {len(my_set)}")

# we can not add items after the tuple has been created.
