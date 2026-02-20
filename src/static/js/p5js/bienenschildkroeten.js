
let janne=50;
function setup() {
  createCanvas(400, 400).parent('p5js');
}

 function draw() {
  fill("pink");
  background(164,210,224);
  circle(200,janne,50);
  fill(164,210,224);
  circle(200,janne,20);
  janne=janne+1;
  fill("rgb(233,229,168)");
  rect(mouseX,380,70,100);
  if (janne == 380) {
      janne = -50
      }
  }
