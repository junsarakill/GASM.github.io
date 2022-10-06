const imgMap = new Map();
//이미지 정보
const imgObj = function(id, status, prevImg, nextImg, rarity, type)
{
    //번호 : 이미지의 이름
    this.id = id;
    //status : 0 = 미획득, 1 = 획득
    this.status = status;
    //prevImg : 이전 이미지 번호 없으면 start
    this.prevImg = prevImg;
    //nextImg : 다음 이미지 번호 없으면 end
    this.nextImg = nextImg;
    //rarity : n,r,sr,ssr,ur,lr
    this.rarity = rarity;
    //type : b=blue, r=red, y=yellow, p=purple, g=green
    this.type = type;
}
const imgInfo1 = new imgObj("1",0,"start","11","ur","b");
imgMap.set(imgInfo1.id,imgInfo1);
const imgInfo2 = new imgObj("2",0,"start","12","ur","r");
imgMap.set(imgInfo2.id,imgInfo2);
const imgInfo3 = new imgObj("3",0,"start","13","ur","y");
imgMap.set(imgInfo3.id,imgInfo3);
const imgInfo4 = new imgObj("4",0,"start","14","ur","p");
imgMap.set(imgInfo4.id,imgInfo4);
const imgInfo5 = new imgObj("5",0,"start","15","ur","g");
imgMap.set(imgInfo5.id,imgInfo5);
const imgInfo6 = new imgObj("6",0,"start","16","ur","b");
imgMap.set(imgInfo6.id,imgInfo6);
const imgInfo7 = new imgObj("7",0,"start","end","ssr","g");
imgMap.set(imgInfo7.id,imgInfo7);
const imgInfo8 = new imgObj("8",0,"start","end","sr","y");
imgMap.set(imgInfo8.id,imgInfo8);
const imgInfo9 = new imgObj("9",0,"start","end","r","p");
imgMap.set(imgInfo9.id,imgInfo9);
const imgInfo10 = new imgObj("10",0,"start","end","ssr","r");
imgMap.set(imgInfo10.id,imgInfo10);
const imgInfo11 = new imgObj("11",0,"1","end","ur","b");
imgMap.set(imgInfo11.id,imgInfo11);
const imgInfo12 = new imgObj("12",0,"2","end","ur","r");
imgMap.set(imgInfo12.id,imgInfo12);
const imgInfo13 = new imgObj("13",0,"3","end","ur","y");
imgMap.set(imgInfo13.id,imgInfo13);
const imgInfo14 = new imgObj("14",0,"4","end","ur","p");
imgMap.set(imgInfo14.id,imgInfo14);
const imgInfo15 = new imgObj("15",0,"5","end","ur","g");
imgMap.set(imgInfo15.id,imgInfo15);
const imgInfo16 = new imgObj("16",0,"6","end","ur","b");
imgMap.set(imgInfo16.id,imgInfo16);
const imgInfo17 = new imgObj("17",0,"7","end","ur","r");
imgMap.set(imgInfo17.id,imgInfo17);

const imgInfo100 = new imgObj("100",0,"start","101","ssr","p");
imgMap.set(imgInfo100.id,imgInfo100);
const imgInfo101 = new imgObj("101",0,"100","102","ssr","p");
imgMap.set(imgInfo101.id,imgInfo101);
const imgInfo102 = new imgObj("102",0,"101","103","ur","p");
imgMap.set(imgInfo102.id,imgInfo102);
const imgInfo103 = new imgObj("103",0,"102","end","lr","p");
imgMap.set(imgInfo103.id,imgInfo103);

const imgInfo444 = new imgObj("444",0,"start","445","ur","g");
imgMap.set(imgInfo444.id,imgInfo444);