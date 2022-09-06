import math 


class calc:
    def calcDmg1(atk,de,**buff):
        dmg = (atk + buff["aBuff"]) - de

        if(dmg < 0):
            dmg = 0

        return dmg
    def calcDmg2(atk,defR, **buff):
        dmg = atk * (1 + buff["aBuff"] - defR)
        dmg = round(dmg)
        return dmg

class main:
    atk = 5000
    aBuff1 = 500
    aBuff2 = 0.1
    de = 500
    defR = 0.6

    dmg = calc.calcDmg1(atk,de,aBuff = aBuff1)
    print("flat:",dmg)

    dmg = calc.calcDmg2(atk,defR, aBuff = aBuff2)
    print("rate:",dmg)




