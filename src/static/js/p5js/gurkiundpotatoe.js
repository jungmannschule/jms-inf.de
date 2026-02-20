
let player1, player2;
let fallingObjects = [];
let score = 0;
let gameOver = false;
let keys = {};

function setup() {
  createCanvas(400, 400).parent('p5js');
  resetGame();
}

function draw() {
  background(30);

  if (gameOver) {
    showGameOverScreen();
    noLoop();
    return;
  }

  displayScore();
  movePlayers();
  drawPlayers();
  updateFallingObjects();
  maybeAddNewObject();
}

// ---------- Spieler ----------

function createPlayer(x, color) {
  return {
    x: x,
    y: height - 30,
    r: 30,
    speed: 5,
    color: color
  };
}

function drawPlayers() {
  drawPlayer(player1);
  drawPlayer(player2);
}

function drawPlayer(player) {
  fill(player.color);
  ellipse(player.x, player.y, player.r);
}

function movePlayers() {
  // Spieler 1: A/D
  if (keys[65]) player1.x -= player1.speed;
  if (keys[68]) player1.x += player1.speed;

  // Spieler 2: Links/Rechts
  if (keys[LEFT_ARROW]) player2.x -= player2.speed;
  if (keys[RIGHT_ARROW]) player2.x += player2.speed;

  player1.x = constrain(player1.x, player1.r / 2, width - player1.r / 2);
  player2.x = constrain(player2.x, player2.r / 2, width - player2.r / 2);
}

// ---------- Objekte ----------

function createFallingObject() {
  return {
    x: random(20, width - 20),
    y: 0,
    r: 30,
    speed: random(2, 4),
    type: random() < 0.7 ? "good" : "bad"
  };
}

function updateFallingObjects() {
  for (let i = fallingObjects.length - 1; i >= 0; i--) {
    let obj = fallingObjects[i];

    obj.y += obj.speed;

    if (obj.type === "good") {
      fill(255, 200, 0);
    } else {
      fill(255, 0, 0);
    }

    ellipse(obj.x, obj.y, obj.r);

    if (obj.type === "bad") {
      fill(255);
      textAlign(CENTER, CENTER);
      textSize(18);
      text("X", obj.x, obj.y);
    }

    if (checkCollision(player1, obj) || checkCollision(player2, obj)) {
      if (obj.type === "good") {
        score++;
        fallingObjects[i] = createFallingObject();
      } else {
        gameOver = true;
      }
    } else if (obj.y > height) {
      // Objekt unten aus dem Bildschirm – neu spawnen
      fallingObjects[i] = createFallingObject();
    }
  }
}

function maybeAddNewObject() {
  if (frameCount % 120 === 0 && fallingObjects.length < 10) {
    fallingObjects.push(createFallingObject());
  }
}

function checkCollision(player, obj) {
  let d = dist(player.x, player.y, obj.x, obj.y);
  return d < (player.r + obj.r) / 2;
}

// ---------- Anzeige ----------

function displayScore() {
  fill(255);
  textSize(18);
  textAlign(LEFT, TOP);
  text("Score: " + score, 10, 10);
}

function showGameOverScreen() {
  background(30);
  fill(255);
  textAlign(CENTER, CENTER);
  textSize(32);
  text("Game Over", width / 2, height / 2 - 20);

}

// ---------- Steuerung ----------

function keyPressed() {
  keys[keyCode] = true;

if (gameOver && keyCode === 82) { // R
    resetGame();
    loop();
  }
}

function keyReleased() {
  keys[keyCode] = false;
}

// ---------- Neustart ----------

function resetGame() {
  player1 = createPlayer(100, color(0, 150, 255));  // Blau
  player2 = createPlayer(300, color(200, 0, 200));  // Lila

  fallingObjects = [];
  for (let i = 0; i < 5; i++) {
    fallingObjects.push(createFallingObject());
  }

  score = 0;
  gameOver = false;
}