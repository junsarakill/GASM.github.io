//이미지 선택시 비활성화 : 클래스명 변경
function switchImg(e)
{
    if(e.classList.item(0) == 'deactiveImg')
        e.className = 'activeImg';    
    else
        e.className = 'deactiveImg';   
}