def linear_search(target, my_list):
    for i in my_list:
        if i == target:
            print (my_list.index(i))
            break
        if i != target:
            print ('not')
            break
            
# def linear_search(target, my_list):
#     i = target
#     while i != target in my_list:
        
#         if i == target:
#             break
#         print (my_list.index(i))
#         if i != target in my_list:
#             break
#         print ('not')

random_numbers = [6, 29, 18, 2, 72, 19, 18, 10, 37]

# linear_search(18, random_numbers)  # 2 (it returns the position of the number)
# linear_search(9, random_numbers)   # not found


def global_linear_search(target, my_list):
    for i in my_list:
        if i == target:
            print (my_list.index(i))
            
    

bananas_arr = list("bananas")   #  ["b", "a", "n", "a", "n", "a", "s"]
global_linear_search("a", bananas_arr)   # [1, 3, 5]