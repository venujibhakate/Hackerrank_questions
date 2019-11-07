def socksMarchant(list1):
    i = 0
    count = 0
    while i < len(list1):
        j = i + 1
        while j < len(list1):
            if list1[i] == list1[j]:
                count = count + 1
                del (list1[i])
                break
            j = j + 1
        i = i + 1
    return(count)
print(socksMarchant([1,2,3,3,1,1,1,3,4,6,6]))

#  socks = {}
#     res = 0
    
#     for el in ar:
#         if el not in socks.keys():
#             socks[el] = 1
#         else:
#             socks[el] += 1
    
#     for key in socks.keys():
#         res += socks[key]//2
    
#     return res