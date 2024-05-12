import tkinter
from tkinter import filedialog
from PIL import Image
import os
import shutil

# 선택한 폴더 내의 이미지 중 1024x1024 초과 이미지 모으기

# 걸러낼 이미지 크기
min_width = 1024
min_height = 1024

if __name__ == "__main__":
    root = tkinter.Tk()
    root.withdraw()
    path = filedialog.askdirectory(parent=root,initialdir="/",title="걸러낼 폴더 선택")
    print("\n 선택된 경로 : ",path)
    result_path = os.path.join(path, "result")
# result 폴더 생성
    os.makedirs(result_path, exist_ok=True)
    
    for filename in os.listdir(path):
        # 이미지 크기 가져오기
        if filename.endswith(".png"):
            try:
                filepath = os.path.join(path, filename)
                with Image.open(filepath) as img:
                    width, height = img.size
                    # 초과 이동
                    if width > min_width and height > min_height:
                        # os.remove(filepath)
                        dest_path = os.path.join(result_path, filename)
                        shutil.move(filepath,dest_path)
                img.close()
            except Exception as e:
                print(f"{filename} 처리 중 오류 발생 : {e}")