arr_tuple = (1,2,5,7,9,25,50,100)     # changes are not appliacble in tuple
#arr_tuple.append(6)
print(arr_tuple)
for ele in arr_tuple:
    print(ele)
for  ind in range(0,len(arr_tuple)):
    print("Element at",ind,"value is",arr_tuple[ind])

arr_list = list(arr_tuple)
arr_list.append(99)
print(arr_list)
print(arr_tuple)