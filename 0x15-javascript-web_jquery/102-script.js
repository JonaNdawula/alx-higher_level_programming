// A JavaScript script that fetches and prints 
// how to say “Hello” depending on the language

$('document').ready (function () {
  const givenUrl = 'https://www.fourtonfish.com/hellosalut/hello/'
  $('input#btn_translate').click(function () {
    $.get(givenUrl + $.param({ lang: $('input#language_code').val() }), function (dt) {
      $('div#hello').html(dt.hello);
    });
  });
});
