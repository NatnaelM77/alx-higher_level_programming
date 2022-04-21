$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const listItem = $('<li>', { text: 'Item' });
    $('UL.my_list').append(listItem);
  });

  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
