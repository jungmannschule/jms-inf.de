let x = 320


function setup() {
  createCanvas(400, 400).parent('p5js');
};

function draw() {
  background(220);

  fill("#00FF0A");
  rect(-2, 350, 410);

  fill("yellow");
  rect(30, 320, 30);

  fill("red");
  triangle(x, 270, x, 350, x-20, 350);
  x = x - 2
  if (x == 400)
      x =20


}
