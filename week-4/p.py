def swap_first_last():
    list = [1, 2, 3, 4, 5] 

    list[0], list[-1] = list[-1], list[0]  
    return list  

result = swap_first_last()
print("List after swapping first and last elements:", result)