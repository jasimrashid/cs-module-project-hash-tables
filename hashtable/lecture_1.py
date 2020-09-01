a = ['the','quick','brown','fox']


for i in a:
    if i == 'c':
        print('yes it is')
        break


# print(a.index('b'))
# print(a.get('b'))
table = [None]*8

def hashf(s):
    b = s.encode()

    total = 0

    for i in b:
        total += i

    # hash_value = ???

    return total

def put(key,value):
    pass

def get(key):
    pass

def delete(key):
    pass




print(hashf('quick'))
print(table)
print((get('quick')))
print((put('bim',3490))