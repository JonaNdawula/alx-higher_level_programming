//A JavaScript script that adds a <li> element 
//to a list when the user clicks on the tag DIV#add_item

$('div#add_item').click(function () {
    let el = '<li>Item</li>';
    $('ul.my_list').append(el);
  });
