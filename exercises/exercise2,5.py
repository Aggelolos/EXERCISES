a = int(input('where is the starting point?'))
b = int(input('where is the end point?'))
c = int(input('with what step do you want to?'))
if a < b:
    while a <= b:
        print(a)
        a = a + c
else:
    while a >= b:
        print (a)
        a = a - c