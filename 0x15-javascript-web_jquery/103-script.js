$(document).ready(function () {
    $('INPUT#btn_translate').on('click', function () {
            let lang = $('INPUT#language_code').val();
            let request = $.get(`https://fourtonfish.com/hellosalut/?lang=${lang}`,
                function (response) {
                    $('DIV#hello').text(response.hello)
                }
            );
        },
        'keypress', function (keyEvent) {
            if (keyEvent.which == 13) {
                let lang = $('INPUT#language_code').val();
                let request = $.get(`https://fourtonfish.com/hellosalut/?lang=${lang}`,
                    function (response) {
                        $('DIV#hello').text(response.hello)
                    }
                );
            }
        }
    );
});
