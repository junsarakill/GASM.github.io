//�̹��� ����Ʈ
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

//�̹��� ���ý� ��Ȱ��ȭ : Ŭ������ ����
function switchImg(e)
{
    if(e.classList.item(0) == 'deactiveImg')
        e.className = 'activeImg';    
    else
        e.className = 'deactiveImg';   
}

//�̹��� �ҷ�����
function viewImg()
{
    for(var i = 1;i < 10; i++)
    {
        document.write(
            "<img id=\""+i+"\" src=\"./img/"+i+".png\" "
            +"onclick=\"switchImg(this)\">");
    }
}