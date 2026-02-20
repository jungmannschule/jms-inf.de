
let ball;
let target;

function setup() {
  createCanvas(600, 400).parent('p5js');
  ball = createVector(width / 2, height / 2);
  target = ball.copy();
}

function draw() {
  background(255, 165, 0);


  let dir = p5.Vector.sub(target, ball);
  dir.mult(0.05);
  ball.add(dir);


  fill(255, 255, 0);
  noStroke();
  ellipse(ball.x, ball.y, 75, 75);
}

function mousePressed() {

  target.set(mouseX, mouseY);
}