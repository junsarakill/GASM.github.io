#import math 


#class calc:
#    def calcDmg1(atk,de,**buff):
#        dmg = (atk + buff["aBuff"]) - de

#        if(dmg < 0):
#            dmg = 0

#        return dmg
#    def calcDmg2(atk,defR, **buff):
#        dmg = atk * (1 + buff["aBuff"] - defR)
#        dmg = round(dmg)
#        return dmg

#class main:
#    atk = 5000
#    aBuff1 = 500
#    aBuff2 = 0.1
#    de = 5000
#    defR = 0.6

#    dmg = calc.calcDmg1(atk,de,aBuff = aBuff1)
#    print("flat:",dmg)

#    dmg = calc.calcDmg2(atk,defR, aBuff = aBuff2)
#    print("rate:",dmg)
from math import ceil


def solution(survey, choices):
    type = {
        "R" : 0,
        "T" : 0,
        "F" : 0,
        "C" : 0,
        "M" : 0,
        "J" : 0,
        "A" : 0,
        "N" : 0
    }
        
    #survey 0~length for문
    for i in range(len(survey)):
        
        #함수1 삽입값 selectType
        sType = ""
        if(selectType(choices[i])):
            sType = survey[i][0]
        else:
            sType = survey[i][1]
        #함수2 점수 calcScore 
        score = calcScore(choices[i])
        #유형에 점수 추가
        



    answer = ""

    return answer

#값 넣을 유형 선택 true = 앞
def selectType(choice):
    if(choice <= 4):
        return True
    else:
        return False
#점수 계산
def calcScore(choice):
    #선택기의 중간값
    for x in range(4):
        if(choice == 1 or choice == 7):
            return 3
        elif(choice == 2 or choice == 6):
            return 2
        elif(choice == 3 or choice == 5):
            return 1
        else:
            return 0

type = {
"R" : 0,
"T" : 0,
"F" : 0,
"C" : 0,
"M" : 0,
"J" : 0,
"A" : 0,
"N" : 0
}

print(type)
s = "R"
score = 3
#@@ 코데 진행중
print(type[s])

