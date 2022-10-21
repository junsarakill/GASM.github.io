
#자동용 데이터
type = {
    "blue" : [9,15]
    ,"red" : [4,38]
    ,"yellow" : [5,18]
    ,"purple" : [5,11]
    ,"green" : [5,17]    
}
#색상표
Colors = {
    "BLACK" : '\033[30m'
    ,"RED" : '\033[31m'
    ,"GREEN" : '\033[32m'
    ,"YELLOW" : '\033[33m'
    ,"BLUE" : '\033[34m'
    ,"PURPLE" : '\033[95m'
    ,"MAGENTA" : '\033[35m'
    ,"CYAN" : '\033[36m'
    ,"WHITE" : '\033[37m'
    ,"UNDERLINE" : '\033[4m'
    ,"RESET" : '\033[0m'
}
    
#출처: https://info-lab.tistory.com/230 [:: IT School :::티스토리]

#ssr, sr 개수 받아서 총합치 계산
def calcJow(ssr, sr):
    #ssr*10 + sr*5
    result = int(ssr)*10 + int(sr)*5
    return result

def calcJowAuto():
    #반환값 선언
    result = ""

    for x in type:
        sum = calcJow(type[x][0],type[x][1])
        result += "{2}{0}{3} 속성의 행운합계: {2}{1}{3}\n".format(x,sum,Colors[x.upper()],Colors["RESET"])

    return result

def calcJowManual():
    input2 = input("ssr, sr 수치를 입력해주세요(공백으로 구분): ").split()
    sum = calcJow(input2[0],input2[1])
    retry = input("결과: {}, 다시하시겠습니까? y/n: ".format(sum)).lower()
    
    if(retry == "y"):
        return calcJowManual()
    else:
        return "종료"

#행운 저장량 계산
def SKCJ():
    #자동 여부
    input1 = input("자동으로 하시겠습니까?"
        +"(데이터가 입력 되어 있어야 합니다) y/n: ").lower()

    if(input1 == "y"):
        result = calcJowAuto()
    else:
        result = calcJowManual()
    #결과 출력
    print(result)



#---------------실행단----------
SKCJ()






