class math():
    a = 20
class Car():
    @staticmethod
    def chkType(mCode):
        if mCode >= 20:
            print("this car is electro car")
        elif mCode >= 10:
            print("this car gasolin car")
        else:
            print("this car is dezel car")

Car.chkType(1)
asd = Car()
asd.chkType(20)