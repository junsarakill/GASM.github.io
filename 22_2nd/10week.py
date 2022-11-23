#class & object
#객체 속성(상태, 특징) 과 행위(행동, 동작, 기능) 으로 구성된 대상
print("aaa")

class Demi():
    pass
    asd = 123
    def __init__(self, ws,c):
        self.ws = ws
        self.c = c
    def move (self, speed):
        print("자전거 : {}km/h 로 전진".format(speed))
    def turn (self, direction):
        print("자전거: {} 회전".format(direction))
    def stop (self):
        print("bike({},{}) : stop".format(self.ws,self.c))
    
class pedoDemi(Demi):
    def __init__(self,ws,c,state):
        Demi.__init__(self,ws,c)
        self.state = state
    
    def fold(self):
        self.state = "folding"
        print("bike: fold, state = {0}".format(self.state))
    def unfold(self):
        self.state = "unfolding"
        print("bike: unfold, state= {}".format(self.state))

demi = Demi(25,"blue")
print(demi.asd)

demi.named = "jkakk"
print(demi.named)

demi.move(30)
demi.turn("right")
demi.stop()

pedo = pedoDemi(11, "white","folding")
pedo.move(30)
pedo.fold()
pedo.stop()