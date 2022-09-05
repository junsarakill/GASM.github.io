function turnOnDarkMode()
{
	const checkbox = document.getElementById("darkCheckbox");
	const is_checked = checkbox.checked;

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
