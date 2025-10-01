#!/usr/bin/node
// 8-esrever.js
exports.esrever = function (list) {
  const reversedList = []; // Initialize an empty array to store the reversed list

  // Loop through the list from the last element to the first
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]); // Add each element to the reversedList
  }

  return reversedList; // Return the reversed list
};
