function turnOnDarkMode()
{
	const checkbox = document.getElementById("darkCheckbox");
	const is_checked = checkbox.checked;

	//fixme 이거 이상 아마 if문 제거 해도 될듯?
	if(is_checked)
	{
		var element = document.body;
		element.classList.toggle("light-mode");
	}
	else
	{
		var element = document.body;
		element.classList.toggle("light-mode");
	}
}
