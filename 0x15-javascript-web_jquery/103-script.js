$(document).ready(function () {
	
	function translate() {
		let lang = $('INPUT#language_code').val();
        let request = $.get(`https://fourtonfish.com/hellosalut/?lang=${lang}`,
          function (response) {
		    $('DIV#hello').text(response.hello)
          }
       );
	}
	
    $('INPUT#btn_translate').click(translate);
    $('INPUT#language_code').keypress(function (keyEvent) {
		if (keyEvent.which == 13)
		{
			translate();
		}
	});
});
