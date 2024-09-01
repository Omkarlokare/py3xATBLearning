number = [1, 2, 3]

def do_something(my_list):
    my_list.append(100)
    my_list[0] = 7
    return my_list

a = do_something(number)
print(a)