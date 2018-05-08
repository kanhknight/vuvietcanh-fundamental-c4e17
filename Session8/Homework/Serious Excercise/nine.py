def get_envent_list(l):
    l_new = []
    for i in l:
        if i%2==0:
            l_new.append(i)
    return(l_new)
a = get_envent_list([1,2,3,4,5,5,6,6,7,78,6,99,10])
print(a)