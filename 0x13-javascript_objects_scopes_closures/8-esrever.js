#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let index = 0;
  while ((len - index) > 0) {
    const aux = list[len];
    list[len] = list[index];
    list[index] = aux;
    index++;
    len--;
  }
  return list;
};
