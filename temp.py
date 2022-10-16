def calc(n1,n2):
    result = n1*10 + n2*5
    print("{}, {} = {}".format(n1,n2,result))


a = [[14,16],[4,38],[5,15],[5,11],[5,14]]

for x in a:
    calc(x[0],x[1])