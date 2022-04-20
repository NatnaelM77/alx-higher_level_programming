$('DIV#add_item').click(function() {
    let list_item = $('<li>', {text: 'Item'});
    $('UL.my_list').append(list_item);
});
