dict_val = [{'name':'test1','age':20},
            {'name':'test2','age':19},
            {'name':'test3','age':23}]

#Ascending Order
print (sorted(dict_val, key = lambda i: i['age']))

#Descending Order
print (sorted(dict_val, key = lambda i: i['age'], reverse=True))

