// A JavaScript script that fetches and prints how 
// to say “Hello” depending on the language

$('document').ready(function () {
  $('input#btn_translate').click(change_lang);
  $('input#language_code').focus(function () {
    $(this).keydown(function (enter) {
      if (enter.keycode == 13) {
	change_lang();
      }
    });
  });
});

function change_lang () {
  const givenUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
  $.get(givenUrl + $.param( lang: $('input#language_code').val() }), function (dt) {
    $('div#hello').html(dt.hello);
  });
}
