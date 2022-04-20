document.addEventListener('DOMContentLoaded', function () {
    let request = $.get('https://fourtonfish.com/hellosalut/?lang=fr',
        function (response) {
            $('DIV#hello').text(response.hello)
        }
    );
});
