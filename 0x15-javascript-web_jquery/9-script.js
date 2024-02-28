// A JavaScript script that fetches from https: hellosalut.stefanbohacek.dev/?lang=fr /// and displays the value of hello from that fetch in the HTML tag DIV#hello.

$('document').ready(function () {
  let givenUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
  $.get(givenUrl, function (dt) {
    $('div#hello').text(dt.hello);
  });
});
