#!/usr/bin/node

$(function () {
  $.get('https://swapi.co/api/films/?format=json', function (data, statusTxt) {
    if (statusTxt === 'success') {
      let films = data.results;
      for (let i in films) {
        $('#list_movies').append('<li>' + films[i].title + '</li>');
      }
    }
  });
});
