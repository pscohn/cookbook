

a = "abcde"
b = "cd"
c = "efg"



def perms(list_of_strings):
    if len(list_of_strings) == 0:
        return [""]

    result = []
    strings = perms(list_of_strings[1:])
    for c in list_of_strings[0]:
        for string in strings:
            result.append(c+string)
    return result
        
        


print(perms([a,b,c]))
