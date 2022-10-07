//이미지 정보 맵
const imgMap = new Map();
//필터 정보
let filterList = 
["n","r","sr","ssr","ur","lr"
,"blue","red","yellow","purple","green"];
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
const imgInfo1 = new imgObj("1","active","start","11","ur","blue");
imgMap.set(imgInfo1.id,imgInfo1);
const imgInfo2 = new imgObj("2","active","start","12","ur","red");
imgMap.set(imgInfo2.id,imgInfo2);
const imgInfo3 = new imgObj("3","active","start","13","ur","yellow");
imgMap.set(imgInfo3.id,imgInfo3);
const imgInfo4 = new imgObj("4","active","start","14","ur","purple");
imgMap.set(imgInfo4.id,imgInfo4);
const imgInfo5 = new imgObj("5","active","start","15","ur","green");
imgMap.set(imgInfo5.id,imgInfo5);
const imgInfo6 = new imgObj("6","active","start","16","ur","blue");
imgMap.set(imgInfo6.id,imgInfo6);
const imgInfo7 = new imgObj("7","active","start","end","ssr","green");
imgMap.set(imgInfo7.id,imgInfo7);
const imgInfo8 = new imgObj("8","active","start","end","sr","yellow");
imgMap.set(imgInfo8.id,imgInfo8);
const imgInfo9 = new imgObj("9","active","start","end","n","purple");
imgMap.set(imgInfo9.id,imgInfo9);
const imgInfo10 = new imgObj("10","active","start","end","ssr","red");
imgMap.set(imgInfo10.id,imgInfo10);
const imgInfo11 = new imgObj("11","active","1","end","ur","blue");
imgMap.set(imgInfo11.id,imgInfo11);
const imgInfo12 = new imgObj("12","active","2","end","ur","red");
imgMap.set(imgInfo12.id,imgInfo12);
const imgInfo13 = new imgObj("13","active","3","end","ur","yellow");
imgMap.set(imgInfo13.id,imgInfo13);
const imgInfo14 = new imgObj("14","active","4","end","ur","purple");
imgMap.set(imgInfo14.id,imgInfo14);
const imgInfo15 = new imgObj("15","active","5","end","ur","green");
imgMap.set(imgInfo15.id,imgInfo15);
const imgInfo16 = new imgObj("16","active","6","end","ur","blue");
imgMap.set(imgInfo16.id,imgInfo16);
const imgInfo17 = new imgObj("17","active","7","end","ur","red");
imgMap.set(imgInfo17.id,imgInfo17);
const imgInfo18 = new imgObj("18","active","start","end","ur","purple");
imgMap.set(imgInfo18.id,imgInfo18);
const imgInfo19 = new imgObj("19","active","start","end","ur","green");
imgMap.set(imgInfo19.id,imgInfo19);

const imgInfo100 = new imgObj("100","active","start","101","ssr","purple");
imgMap.set(imgInfo100.id,imgInfo100);
const imgInfo101 = new imgObj("101","active","100","102","ssr","purple");
imgMap.set(imgInfo101.id,imgInfo101);
const imgInfo102 = new imgObj("102","active","101","103","ur","purple");
imgMap.set(imgInfo102.id,imgInfo102);
const imgInfo103 = new imgObj("103","active","102","end","lr","purple");
imgMap.set(imgInfo103.id,imgInfo103);

const imgInfo444 = new imgObj("444","active","start","445","ur","green");
imgMap.set(imgInfo444.id,imgInfo444);

const imgInfo666 = new imgObj("666",0,"start","end","ur","red");
imgMap.set(imgInfo666.id,imgInfo666);

