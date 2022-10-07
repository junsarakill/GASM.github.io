//이미지 정보 맵
const imgMap = new Map();
//필터 정보
let filterList = 
["n","r","sr","ssr","ur","lr"
,"blue","red","yellow","purple","green"];
//이미지 활성화 정보 불러오기
let imgDeactiveList = [];
if(localStorage.getItem("deactiveImg") == null)
    localStorage.setItem("deactiveImg",JSON.stringify(imgDeactiveList));
else
    imgDeactiveList = JSON.parse(localStorage.getItem("deactiveImg"));
//이미지 정보
class imgObj 
{
    constructor(id, status, prevImg, nextImg, rarity, type) 
    {
        //번호 : 이미지의 이름
        this.id = id;
        //status : active = 미획득, deactive = 획득
        this.status = status;
        //prevImg : 이전 이미지 번호 없으면 start
        this.prevImg = prevImg;
        //nextImg : 다음 이미지 번호 없으면 end
        this.nextImg = nextImg;
        //rarity : n,r,sr,ssr,ur,lr
        this.rarity = rarity;
        //type : blue, red, yellow, purple, green
        this.type = type;
    }
}
//이미지 정보 객체 모음
const imgInfoList =
[
    new imgObj("1","active","start","11","ur","blue")
    ,new imgObj("2","active","start","12","ur","red")
    ,new imgObj("3","active","start","13","ur","yellow")
    ,new imgObj("4","active","start","14","ur","purple")
    ,new imgObj("5","active","start","15","ur","green")
    ,new imgObj("6","active","start","16","ur","blue")
    ,new imgObj("7","active","start","end","ssr","green")
    ,new imgObj("8","active","start","end","sr","yellow")
    ,new imgObj("9","active","start","end","n","purple")
    ,new imgObj("10","active","start","end","ssr","red")
    ,new imgObj("11","active","1","end","ur","blue")
    ,new imgObj("12","active","2","end","ur","red")
    ,new imgObj("13","active","3","end","ur","yellow")
    ,new imgObj("14","active","4","end","ur","purple")
    ,new imgObj("15","active","5","end","ur","green")
    ,new imgObj("16","active","6","end","ur","blue")
    ,new imgObj("17","active","7","end","ur","red")
    ,new imgObj("18","active","start","end","ur","purple")
    ,new imgObj("19","active","start","end","ur","green")
    ,new imgObj("20","active","start","end","ur","yellow")
    ,new imgObj("21","active","start","end","r","red")
    ,new imgObj("100","active","start","101","ssr","purple")
    ,new imgObj("101","active","100","102","ssr","purple")
    ,new imgObj("102","active","101","103","ur","purple")
    ,new imgObj("103","active","102","end","lr","purple")

    ,new imgObj("444","active","start","445","ur","green")

    ,new imgObj("666","active","start","end","ur","red")
]


//이미지 비활성화
function deactiveImg()
{
    imgDeactiveList.forEach(imgId => {
        //해당 이미지 객체 수정
        const imgInfo = imgInfoList.find(imgInfo => imgInfo.id === imgId);
        imgInfo.status = "deactive";
    });
}

//이미지 객체 맵에 추가
function addImgMap(imgList)
{
    //기존 정보 제거
    imgMap.clear();
    //객체 추가
    imgList.forEach(imgInfo => {
        imgMap.set(imgInfo.id, imgInfo);
    });
}

deactiveImg();
addImgMap(imgInfoList);

