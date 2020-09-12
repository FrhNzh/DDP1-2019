def decipher_requiem(mantra):
    ''' fungsi untuk me-reverse sebuah string'''
    
    if len(mantra) == 1:
        return mantra
    else:
        return mantra[-1] + decipher_requiem(mantra[:-1])