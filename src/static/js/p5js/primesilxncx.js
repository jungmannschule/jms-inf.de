let x;
let speed;

let rectX;
let rectSpeed;
let rectWidth = 25;
let rectHeight = 50;

function setup() {
  createCanvas(750,750).parent('p5js');
  x = 50;
  speed = 5;
  noStroke();

    rectX = width;
  rectSpeed = 2;
}

function draw() {
  background(135, 206, 235);
  fill(255, 102, 0);
  let y = height * 0.75;

  ellipse(x, y, 85, 100);

  x += speed;

  if (x > width - 25 || x < 25)
    speed = -speed;

  fill(128, 0, 32);
  noStroke();

  rect(100, 200, 200, 125)

 fill(255);
  let rectY = height * 0.4 - rectHeight / 2;
  rect(rectX, rectY, rectWidth, rectHeight);

  rectX -= rectSpeed;

  if (rectX + rectWidth < 0)
    rectX = width;
}