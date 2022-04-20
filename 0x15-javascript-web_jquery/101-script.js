document.addEventListener('DOMContentLoaded', function () {
    $('DIV#add_item').click(function () {
        let list_item = $('<li>', {text: 'Item'});
        $('UL.my_list').append(list_item);
    });

    $('DIV#remove_item').click(function () {
        let list_item = $('UL.my_list li:last-child');
        $('UL.my_list').remove(list_item);
    });

    $('DIV#clear_list').click(function () {
        $('UL.my_list').html('');
    });
});
