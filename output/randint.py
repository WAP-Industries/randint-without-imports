def randint(l, u):
    c = ''
    while not bool(len(str(c))):
        with open('C:\\Users\\jerom\\Documents\\NoModule\\number.txt', 'r') as file:
            c = file.read()
    return int(u*float(c)+l)