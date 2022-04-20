document.addEventListener('DOMContentLoaded', function () {
    $('INPUT#btn_translate').click(function () {
        let lang = $('INPUT#language_code').val();
        let request = $.get(`https://fourtonfish.com/hellosalut/?lang=${lang}`,
            function (response) {
                $('DIV#hello').text(response.hello)
            }
        );
    });
});
