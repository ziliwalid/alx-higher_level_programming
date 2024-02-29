#!/usr/bin/node

$(function () {
  $.get('https://swapi.co/api/people/5/?format=json', function (data, statusTxt) {
    if (statusTxt === 'success') {
      $('#character').text(data.name);
    }
  });
});
