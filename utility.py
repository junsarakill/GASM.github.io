#행운 저장량 계산
blue = [0,0]
red = [0,0]
yellow = [0,0]
purple = [0,0]
green = [0,0]

type = [blue,red,yellow,purple,green]

#select = input("select type, ssr, sr delimeter is nbsp: ").split()
#select[1] = int(select[1])
#select[2] = int(select[2])

#result = 10*select[1] + 5*select[2]
i = 0
for x in type:
    select = input("type ssr, sr delimeter is nbsp: ").split()
    x = select
    result = int(x[0])*10 + int(x[1])*5
    print("type: {} result: {}".format(i,result))
    i +=1





