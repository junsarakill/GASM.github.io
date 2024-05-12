import os
import shutil
import tkinter
import ctypes
from tkinter import filedialog

# 소녀전선 .ab 압축 파일 업데이트
# 신규 파일 폴더와 기존 폴더를 선택
# 신규 파일을 기존 폴더로 이동
# 그 중 중복이 아닌 신규 파일들을 복사해서 1brandnew 폴더에 생성(기존 1brandnew 폴더는 삭제)


# 폴더 내 파일 이동
def moveFile(start, destination):
    # 신규 파일 리스트
    new_file_list = []
    # 폴더 내 파일명 리스트
    for file_name in os.listdir(start):
        # 파일 경로 설정
        file = os.path.join(start, file_name)
        destination_file = os.path.join(destination, file_name)
        
        # 신규인 경우만 이동
        if not os.path.exists(destination_file):
            shutil.move(file, destination_file)
            # 신규 파일 리스트에 추가
            new_file_list.append(destination_file)
        else:
            # @@ 테스트용으로 일단 미삭제
            print(f"{file} 은 이미 존재함")
            os.remove(file)
        
    return new_file_list

def makeNewFolder(path, file_list):
    # 신규 폴더
    new_folder_path = path + "/1brandnew"
    # 기존 brandnew 폴더 삭제
    if os.path.exists(new_folder_path):
        shutil.rmtree(new_folder_path)
    
    # 폴더 생성 및 신규 파일 복사
    os.makedirs(new_folder_path)
    
    for file in file_list:
        shutil.copy(file, new_folder_path)

    



# ========실행단

if __name__ == "__main__" :
    root = tkinter.Tk()
    root.withdraw()
    # 신규 폴더 선택
    new_folder_path = filedialog.askdirectory(parent=root,initialdir="/",title="신규 파일이 들어있는 폴더를 선택하세요.")
    print("\n 선택된 경로 : ",new_folder_path)
    # 기존 폴더 선택
    dest_folder_path = filedialog.askdirectory(parent=root,initialdir=os.path.dirname(new_folder_path),title="기존 폴더를 선택하세요.")
    print("\n 선택된 경로 : ",dest_folder_path)
    try:
        # 파일 이동 및 신규 파일 리스트 받기
        new_file_list = moveFile(new_folder_path, dest_folder_path)
        # 신규 파일 복사 폴더 생성
        makeNewFolder(dest_folder_path, new_file_list)
        # 종료 메시지
        ctypes.windll.user32.MessageBoxW(0, "처리 종료", "처리 알림", 16)
    except:
        ctypes.windll.user32.MessageBoxW(0, "문제 발생", "처리 알림", 16)
        pass