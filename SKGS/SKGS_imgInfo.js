//이미지 정보 맵
const imgMap = new Map();
//등급 리스트
const rarityList =
[
    "n","r","sr","ssr","ur","lr"
]
//속성 리스트
const typeList = 
[
    "blue","red","yellow","purple","green"
]
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
const imgInfo1 = new imgObj("1","active","start","11",rarityList[4],typeList[0]);
imgMap.set(imgInfo1.id,imgInfo1);
const imgInfo2 = new imgObj("2","active","start","12",rarityList[4],typeList[1]);
imgMap.set(imgInfo2.id,imgInfo2);
const imgInfo3 = new imgObj("3","active","start","13",rarityList[4],typeList[2]);
imgMap.set(imgInfo3.id,imgInfo3);
const imgInfo4 = new imgObj("4","active","start","14",rarityList[4],typeList[3]);
imgMap.set(imgInfo4.id,imgInfo4);
const imgInfo5 = new imgObj("5","active","start","15",rarityList[4],typeList[4]);
imgMap.set(imgInfo5.id,imgInfo5);
const imgInfo6 = new imgObj("6","active","start","16",rarityList[4],typeList[0]);
imgMap.set(imgInfo6.id,imgInfo6);
const imgInfo7 = new imgObj("7","active","start","end",rarityList[3],typeList[4]);
imgMap.set(imgInfo7.id,imgInfo7);
const imgInfo8 = new imgObj("8","active","start","end",rarityList[2],typeList[2]);
imgMap.set(imgInfo8.id,imgInfo8);
const imgInfo9 = new imgObj("9","active","start","end",rarityList[0],typeList[3]);
imgMap.set(imgInfo9.id,imgInfo9);
const imgInfo10 = new imgObj("10","active","start","end",rarityList[3],typeList[1]);
imgMap.set(imgInfo10.id,imgInfo10);
const imgInfo11 = new imgObj("11","active","1","end",rarityList[4],typeList[0]);
imgMap.set(imgInfo11.id,imgInfo11);
const imgInfo12 = new imgObj("12","active","2","end",rarityList[4],typeList[1]);
imgMap.set(imgInfo12.id,imgInfo12);
const imgInfo13 = new imgObj("13","active","3","end",rarityList[4],typeList[2]);
imgMap.set(imgInfo13.id,imgInfo13);
const imgInfo14 = new imgObj("14","active","4","end",rarityList[4],typeList[3]);
imgMap.set(imgInfo14.id,imgInfo14);
const imgInfo15 = new imgObj("15","active","5","end",rarityList[4],typeList[4]);
imgMap.set(imgInfo15.id,imgInfo15);
const imgInfo16 = new imgObj("16","active","6","end",rarityList[4],typeList[0]);
imgMap.set(imgInfo16.id,imgInfo16);
const imgInfo17 = new imgObj("17","active","7","end",rarityList[4],typeList[1]);
imgMap.set(imgInfo17.id,imgInfo17);

const imgInfo100 = new imgObj("100","active","start","101",rarityList[3],typeList[3]);
imgMap.set(imgInfo100.id,imgInfo100);
const imgInfo101 = new imgObj("101","active","100","102",rarityList[3],typeList[3]);
imgMap.set(imgInfo101.id,imgInfo101);
const imgInfo102 = new imgObj("102","active","101","103",rarityList[4],typeList[3]);
imgMap.set(imgInfo102.id,imgInfo102);
const imgInfo103 = new imgObj("103","active","102","end",rarityList[5],typeList[3]);
imgMap.set(imgInfo103.id,imgInfo103);

const imgInfo444 = new imgObj("444","active","start","445",rarityList[4],typeList[4]);
imgMap.set(imgInfo444.id,imgInfo444);

const imgInfo666 = new imgObj("666",0,"start","end",rarityList[4],typeList[1]);
imgMap.set(imgInfo666.id,imgInfo666);


//필터에 따른 시작 객체 모음
//fixme 221006 여기에 필터 리스트에 따른 if 문 추가 필요
function collectStartMap(map)
{
    const ism = new Map();
    
    map.forEach(imgInfo => {
        if(imgInfo.prevImg == "start")
        {
            ism.set(imgInfo.id,imgInfo);
        }
    });
    console.log(ism);

    return ism;
}
//마지막 시작객체만 정리
const imgStartMap = collectStartMap(imgMap);

