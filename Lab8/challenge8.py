def unboxing(lst):
    ''' fungsi untuk membuka bungkusan game'''
    
    if type(lst) == int:
        return str(lst) + ' '
    elif len(lst) == 1:
        if type(lst) == list:
            return unboxing(lst[0])
        else:
            return lst + ' '
    elif type(lst) == list:
        return unboxing(lst[0]) + unboxing(lst[1::])
