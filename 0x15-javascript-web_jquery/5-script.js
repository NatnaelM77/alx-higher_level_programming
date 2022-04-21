$('DIV#add_item').click(function () {
  const listItem = $('<li>', { text: 'Item' });
  $('UL.my_list').append(listItem);
});
