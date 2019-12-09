var a = 1;
var b = 2;

function* foo() {
  a++;
  yield;
  b = b * a; // 9 9
  a = (yield b) + 3; // 12 9
}
function* bar() {
  b--;
  yield;
  a = (yield 8) + b; //9 1
  b = a * (yield 2);
}
function step(gen) {
  var it = gen();
  var last;

  return function() {
    // console.log(last);
    last = it.next(last).value;
  };
}
var s1 = step(foo); //a 1
var s2 = step(bar); //b 2
s2(); // a 1 b 1
s2(); //a 1 b 1

s1(); //a 2 b 1

s2(); //a 9 b 1

s1(); //a 9 b 9
s1(); //a 12 b 9

s2(); //a 12 b 18
console.log(a, b);
