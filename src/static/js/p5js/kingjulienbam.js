let pipo;
let posx = 430;
let losx = 420;
let mosx = 430;
function setup() {
  createCanvas(400, 400).parent('p5js');
  rectMode(CENTER)
}

function draw() {
  background(0, 200, 240);
  pipo = mouseY;

  fill("darkblue");
  rect(70, pipo, 80, 30);

  fill("pink");
  circle(posx, 365, 50);

  if (posx == -20) {
    posx = 430;
  }

  fill("darkred");
  circle(losx, 200, 50);

  if (losx < -20) {
    losx = 430;
  }

  fill("grey");
  circle(mosx, 40, 50);
  if (mosx == -20) {
    mosx = 430;
  }

  posx = posx - 2;
  losx = losx - 4;
  mosx = mosx - 3;


if (pipo > 150 && pipo < 220 && losx > 60 && losx < 100) {
    background("darkblue");
    textSize(40);
    text('game over', 90 ,200);
	 noLoop() }

if (pipo > 310 && pipo < 390 && posx > 60 && posx < 100) {
     background("darkblue");
    textSize (40);
     text('game over', 90, 200);
	noLoop() }

if (pipo > 0 && pipo < 80 && mosx > 60 && mosx < 100) {
    background("darkblue");
    textsize (40);
text('game over', 90, 200);
 noLoop() }



}