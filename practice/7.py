def modify_list(my_list):
    my_list.append(4)
    my_list = [7, 8, 9]
    my_list.append(10)
    return my_list

original = [1, 2, 3]
modified = modify_list(original)
print(f"original is {original}")
print(f"modified is {modified}")