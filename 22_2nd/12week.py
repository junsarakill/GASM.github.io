#string & text file
#a = "asd.dsd. eqe.cxz .dad"
#print(a.replace(" ","").split("."))
#print(a.split("."))

#pn = "+82-10-4054-9620"

#sn = pn.split("-",1)

#print(sn)

#a = ["123","234","67"]

#f = "Python codeaaaaaa"

#print(f.find("easy"),f.find("python"))

#print(f.count("a"))
#print("$!@#@!".isalpha())

fn = "11w\coffeeShopSales.txt"
f = open(fn)
for line in f :
    print(line,end="")
f.close()