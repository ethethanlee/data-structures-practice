data = ['male', 'female', 'male', 'male']

def hot_encode(data):
    counter = 0
    list_of_lists = []
    for item in data:
        again = []
        counter = counter + 1
        if item in data[:(counter - 1)]:
            pass
        else:
            for unit in data:
                if item == unit:
                    again.append(1)
                else:   
                    again.append(0)
            list_of_lists.append(again)
    return list_of_lists

print(hot_encode(data))
            