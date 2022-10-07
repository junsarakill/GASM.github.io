//필터 리스트 불러오기
if(localStorage.getItem("filter") == null)
{
    console.log("기본 필터 리스트 저장");
    localStorage.setItem("filter", JSON.stringify(filterList));
}
else
{
    filterList = JSON.parse(localStorage.getItem("filter"));
    
    console.log("필터 정보: " + filterList);
}

//이미지 활성화 리스트 불러오기
function deactiveImg()
{
    if(localStorage.getItme("deactiveImg") != null)
    {
        imgDeactiveList = JSON.parse(localStorage.getItem("deactiveImg"))
    }
}

//필터 활성화
function activeFilter()
{
    for(var i = 0; i < filterList.length; i++)
    {
        console.log(filterList[i]);
        document.getElementById(filterList[i]).classList.replace("deactive","active");
    }
}

//필터에 따른 시작 객체 모음
function collectStartMap(map)
{
    const ism = new Map();
    
    map.forEach(imgInfo => {
        if(filterList.includes(imgInfo.rarity) && filterList.includes(imgInfo.type) && imgInfo.prevImg == "start")
        {
            ism.set(imgInfo.id,imgInfo);
        }
    });
    console.log(ism);

    return ism;
}

//시작객체만 정리
let imgStartMap = collectStartMap(imgMap);


//리스트 추가 : 매개변수 = 객체 담긴 맵
function viewImgList(map)
{
    map.forEach(imgInfo => {
        addImg(imgInfo.id);
    });
}

//@@ 재귀함수 : 이미지 추가
function addImg(imgId)
{
    var imgInfo = imgMap.get(imgId);
    var imgClass = imgInfo.status+" "+imgInfo.rarity+" "+imgInfo.type
    if(imgInfo != null)
    {
        //이미지 추가
        document.write(
            "<img id=\""+imgId+"\" class=\""+imgClass+"\""
            +" src=\"./img/"+imgId+".png\""
            +" alt=\"No Image\" onclick=\"switchImg(this)\">");
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
    else
    {
        document.write("No Img Info")
    }
}

//이미지 선택시 비활성화 : 클래스명 변경
function switchImg(e)
{
    console.log(e);

    if(e.classList.item(0) == 'deactive')
        e.classList.replace('deactive','active');
    else
        e.classList.replace('active','deactive');
}

//필터 선택
function typeFilter(e, list)
{
    console.log(list);
    if(e.classList.item(1) == 'active')
    {
        //클래스 변경
        e.classList.replace('active','deactive');
        //필터리스트에서 해당 속성 제거
        list = list.filter(function(data)
        {
            return data != e.id;
        });
    }
    else
    {
        //클래스 변경
        e.classList.replace('deactive','active');
        //리스트에서 해당 속성 추가
        list.push(e.id);
    }
    //필터 리스트에 저장
    filterList = list;
    
    console.log("처리 후: "+filterList);
    localStorage.setItem("filter", JSON.stringify(filterList));
    //변경된 필터로 검색하기 위해 새로고침
    location.reload();
}