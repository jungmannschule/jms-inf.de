

let moveY = 400
let speed = 4
function setup() {
  createCanvas(800, 600).parent('p5js');
}

function draw() {
  background("black");
  noStroke()
 fill("rgb(0,255,0)")
  rect(mouseX, 550, 120, 20)
  fill("rgb(255,0,178)")
  rect(0, 580, 800, 20)
  circle(400, moveY, 60)
moveY = moveY+speed
if (moveY == 552 && mouseX > 280 && mouseX < 400){
  speed = -speed

}
if (moveY == 32){
  speed = -speed

}

}
