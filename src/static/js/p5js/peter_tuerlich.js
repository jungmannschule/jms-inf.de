let x = 100, y = 110;
let startX = 100, startY = 110;
let zielX = 285, zielY = 142.5;
let hin = false;
let zurück = false;

function setup() {
  createCanvas(400, 400).parent('p5js');
}

function draw() {
  background(220);

  fill("green");
  square(0, 0, 400);

  fill(54, 21, 9);
  rect(200, 80, 150, 100);

  fill("yellow");
  rect(260, 135, 50, 15);

  fill(163, 111, 64);
  circle(x, y, 100);

  if (hin) {
    if (x < zielX) x += 2;
    if (x > zielX) x -= 2;
    if (y < zielY) y += 2;
    if (y > zielY) y -= 2;

    if (abs(x - zielX) < 2 && abs(y - zielY) < 2) {
      hin = false;
      zurück = true;
    }
  }

  if (zurück) {
    if (x < startX) x += 2;
    if (x > startX) x -= 2;
    if (y < startY) y += 2;
    if (y > startY) y -= 2;

    if (abs(x - startX) < 2 && abs(y - startY) < 2) {
      zurück = false;
    }
  }
}

function mousePressed() {
  if (mouseX > 260 && mouseX < 310 && mouseY > 135 && mouseY < 150) {
    hin = true;
    zurück = false;
  }
}