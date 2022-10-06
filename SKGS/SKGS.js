//리스트 추가
function viewImgList()
{
    imgMap.forEach(imgInfo => {
        //시작 이미지라면 이미지 추가
        if(imgInfo.prevImg == "start")
        {
            console.log(imgInfo.id);
            addImg(imgInfo.id);
        }
    });
}

//@@ 재귀함수 : 이미지 추가
function addImg(imgId)
{
    var imgInfo = imgMap.get(imgId);
    //이미지 추가
    document.write(
        "<img id=\""+imgId+"\" src=\"./img/"+imgId+".png\" "
        +"alt=\"No Image\" onclick=\"switchImg(this)\">");
    //다음이미지 존재시 함수 재실행
    if(imgInfo.nextImg != "end")
    {
        document.write("<em>→</em>");
        
        return addImg(imgInfo.nextImg);
    }
    //이미지 구분 공백 삽입
    else
    {
        document.write("&nbsp&nbsp&nbsp&nbsp&nbsp");
    }
}

//이미지 선택시 비활성화 : 클래스명 변경
function switchImg(e)
{
    if(e.classList.item(0) == 'deactiveImg')
        e.className = 'activeImg';    
    else
        e.className = 'deactiveImg';   
}
