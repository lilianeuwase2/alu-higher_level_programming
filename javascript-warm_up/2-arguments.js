#!/usr/bin/node
const numArgs = Process.argv.length - 2;
if (numArgs === 0) {
    console.log('No argument');
} else if (numArgs === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}