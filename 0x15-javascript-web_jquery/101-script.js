$(document).ready(function () {
    $('DIV#add_item').click(function () {
        let list_item = $('<li>', {text: 'Item'});
        $('UL.my_list').append(list_item);
    });

    $('DIV#remove_item').click(function () {
        $('UL.my_listL.my_list li:last-child').remove();
    });

    $('DIV#clear_list').click(function () {
        $('UL.my_list').empty();
    });
});
