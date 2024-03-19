import os
import shutil
import tkinter
import ctypes
from tkinter import filedialog

#img_here 폴더 안 이미지 이름을 확인
#캐릭터별 폴더 생성 후 이미지 이동
#전문 예시: cmn_cx10000200
#cmn_cx 이미지 타입 : 1080p 전체화면 이미지
#8자리 숫자
#[6]첫 번째 : 레어도 - 1:n 2:r 3:sr 4:ssr 5:ur 6:lr
#[7]두 번째 : 각성여부 - 0:통상 1:통상(특수) 2:각성 3: 신유제(변신)
#[8:11]3~5 번째 : 캐릭터번호 - ex 000(아스카) 165(손권) 비어있는 번호 있음 자세한 목록은 cName 함수에서 확인
#[11]여섯 번째 : 속성 - 0:blue 1:red 2:yellow 3:purple 4:green
#[11:13]7~8 번째 : 출시 순서 - 00~99 속성이 같을 시 출시 순에 따라 00,01,02 순으로 지어짐

#캐릭터 번호 읽기
def fileList(file_list):
    #캐릭터 번호 리스트
    cNum = []
    for file in file_list:
        #리스트에 캐릭터 번호 추가
        cNum.append(file[8:11])
    
    #중복 제거
    tempSet = set(cNum)
    #리스트로 변경
    c_num_list = list(tempSet)
    #결과
    return c_num_list

#캐릭터 폴더 생성
def makeFolder(result_path : str, c_num_list : list):
    
    #폴더 존재시 예외처리 패스
    for file in c_num_list:
        try:
            #캐릭터 이름
            cName = num2Name(file)
            #경로: path_after\캐릭터이름
            os.makedirs(result_path+"/No."+file+" "+cName)
        except:
            pass

#캐릭터 번호 -> 이름 변환 23.02.24
def num2Name(cNum : str):
    #캐릭터 번호:이름 사전
    cName = {
        "000" : "아스카" ,"001" : "이카루가" ,"002" : "카츠라기" ,"003" : "야규" ,"004" : "히바리"

        ,"005" : "호무라" ,"006" : "요미" ,"007" : "히카게" ,"008" : "미라이" ,"009" : "하루카"

        ,"010" : "유미" ,"011" : "무라쿠모" ,"012" : "요자쿠라" ,"013" : "시키" ,"014" : "미노리"

        ,"015" : "미야비" ,"016" : "무라사키" ,"017" : "이무" ,"018" : "료비" ,"019" : "료나"

        ,"020" : "재스민" ,"021" : "료키"
        ,"022" : "렌카" ,"023" : "하나비" ,"024" : "카후루"
        ,"025" : "다이도지"
        ,"026" : "린"
        ,"028" : "아야메"
        #DOA
        ,"029" : "아야네"
        #일기당천
        ,"030" : "손책"
        ,"031" : "여포"
        ,"032" : "관우"

        ,"033" : "나라쿠"
        ,"034" : "카구라"
        ,"035" : "레오"
        ,"036" : "유우야키"
        ,"037" : "소우지"
        #공란
        #일기당천
        ,"042" : "여몽"
        #공란
        #DOA
        ,"045" : "마리 로즈"
        ,"046" : "호노카"
        #공란
        ,"049" : "바쇼"
        #공란
        ,"100" : "후부키"
        ,"101" : "겟코"
        ,"102" : "센코"
        #공란
        ,"106" : "우시마루"
        #아랑 전설 : 스트리트 파이트
        ,"107" : "시라누이 마이"

        ,"108" : "긴레이"
        #퀸즈 블레이드
        ,"109" : "레이나"
        ,"110" : "아이리"

        ,"111" : "미사토"
        ,"112" : "구미"
        ,"113" : "나치"
        #공란
        #킹 오브 파이터즈
        ,"115" : "쿨라"
        ,"116" : "아테나"
        ,"117" : "레오나"
        #DOA
        ,"118" : "카스미"

        ,"119" : "메이메이"
        ,"120" : "마이"
        ,"121" : "츠바키"
        ,"122" : "후가"
        ,"123" : "란마루"
        ,"124" : "아시야"
        #하이스쿨 DxD
        ,"125" : "리아스"
        ,"126" : "슈노"
        #퀸즈 블레이드
        ,"127" : "엘리나"
        ,"128" : "토모에"
        ,"129" : "시즈카"
        #공란
        ,"134" : "이부키"
        #공란
        ,"140" : "토키"
        ,"141" : "우이"
        ,"142" : "카자키리"
        ,"143" : "히요리"
        ,"144" : "아마네"
        #
        ,"146" : "스이렌"
        ,"147" : "쿠레하"
        ,"148" : "타마유라"
        #일기당천
        ,"151" : "조운"
        #백화요란
        ,"152" : "쥬베"
        ,"153" : "카네츠구"
        #하이스쿨 DxD
        ,"154" : "코네코"
        ,"155" : "로스바이세"
        #ToLOVE
        ,"156" : "라라"
        ,"157" : "야미"
        ,"158" : "모모"
        ,"159" : "코테가와 유이"
        #DOA
        ,"160" : "타마키"
        #ToLOVE
        ,"161" : "쿠로사키 메아"
        #던만추
        ,"162" : "헤스티아"
        ,"163" : "아이즈"
        ,"164" : "류 리온"
        #일기당천
        ,"165" : "손권"
        #하이스쿨 DxD
        ,"166" : "제노비아 콰르타"
        ,"167" : "시도 이리나"
        #퀸즈 블레이드
        ,"168" : "아레인"
        #초차원게임 넵튠
        ,"169" : "퍼플 하트"
        ,"170" : "화이트 하트"
        #백화요란
        ,"171" : "사나다 유키무라"
        ,"172" : "도쿠가와 센"



        #만우절
        ,"424" : "메이코"
    }
    #결과 값
    result = cName.get(cNum)
    #사전에 없는 값일 시
    if(result == None):
        result = "기타"

    return result

#폴더에 이미지 이동
def moveFile(dir_path : str, result_path : str, file_list : list):
    #캐릭터 폴더 리스트
    folderList = os.listdir(result_path)
    dict = {}

    #파일명 : 폴더명 형태로 사전 저장
    for file in file_list:
        dict[file] = num2Name(file[8:11]) 
    ##사전 이용해 파일 이동
    for key, value in dict.items():
        shutil.move(dir_path+"/"+key, result_path+"/No."+key[8:11]+" "+value)


#처리 종료 메시지
def endMessage():
    ctypes.windll.user32.MessageBoxW(0, "처리 종료", "처리 알림", 16)





#==========================실행단========================
if __name__ == "__main__" :
    root = tkinter.Tk()
    root.withdraw()
    #폴더 선택
    dir_path = filedialog.askdirectory(parent=root,initialdir="/",title="이미지가 들어있는 폴더를 선택해주세요.")
    print("\n 선택된 경로 : ",dir_path)
    #폴더의 파일명 리스트
    file_list = os.listdir(dir_path)
    #캐릭터 번호 리스트
    c_num_list = fileList(file_list)
    #결과 경로
    result_path = dir_path+"/"+"result"
    #결과 폴더 생성
    os.makedirs(result_path)
    #캐릭터 폴더 생성
    makeFolder(result_path, c_num_list)
    #폴더에 이미지 이동
    moveFile(dir_path,result_path,file_list)
    #처리 종료 메시지
    endMessage()
    