let circle1 = { x: 100, y: 200, size: 50, speed: 20 };
let circle2 = { x: 300, y: 200, size: 50, speed: 20 };

function setup() {
  createCanvas(500, 400).parent('p5js');
  textSize(32);
  textAlign(CENTER, CENTER);
  fill(0);
}

function draw() {
  background(240);

  // Steuerung Kreis 1 – WASD
  if (keyIsDown(87)) circle1.y -= circle1.speed; // W
  if (keyIsDown(83)) circle1.y += circle1.speed; // S
  if (keyIsDown(65)) circle1.x -= circle1.speed; // A
  if (keyIsDown(68)) circle1.x += circle1.speed; // D

  // Steuerung Kreis 2 – Pfeiltasten
  if (keyIsDown(UP_ARROW)) circle2.y -= circle2.speed;
  if (keyIsDown(DOWN_ARROW)) circle2.y += circle2.speed;
  if (keyIsDown(LEFT_ARROW)) circle2.x -= circle2.speed;
  if (keyIsDown(RIGHT_ARROW)) circle2.x += circle2.speed;

  // Kreise zeichnen
  fill(0, 102, 204);
  ellipse(circle1.x, circle1.y, circle1.size);

  fill(255, 100, 100);
  ellipse(circle2.x, circle2.y, circle2.size);

  // Abstand berechnen
  let dx = circle1.x - circle2.x;
  let dy = circle1.y - circle2.y;
  let distance = sqrt(dx * dx + dy * dy);

  // Prüfen, ob die Kreise kollidieren
  if (distance <= (circle1.size / 2 + circle2.size / 2)) {
    fill(0);
    text("Gefangen!", width / 2, height / 4);
  }

}