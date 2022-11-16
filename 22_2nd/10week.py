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
    def stop (self):
        print("bike({},{}) : stop".format(self.ws,self.c))

demi = Demi(25,"blue")
print(demi.asd)

demi.named = "jkakk"
print(demi.named)

demi.move(30)
demi.stop()