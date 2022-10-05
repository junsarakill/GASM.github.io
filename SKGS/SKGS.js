//이미지 리스트
const imgInfo = 
{
    id : "name"
};
//
var fs = require('fs');
fs.readdir('./img', function(err, fileList)
{
    console.log(fileList);
});

//이미지 선택시 비활성화 : 클래스명 변경
function switchImg(e)
{
    if(e.classList.item(0) == 'deactiveImg')
        e.className = 'activeImg';    
    else
        e.className = 'deactiveImg';   
}

//이미지 불러오기
function viewImg()
{
    for(var i = 1;i < 10; i++)
    {
        document.write(
            "<img id=\""+i+"\" src=\"./img/"+i+".png\" "
            +"onclick=\"switchImg(this)\">");
    }
}