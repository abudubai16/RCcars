const socket = io()

window.addEventListener('keydown', function(event){
  key = event.key.toLowerCase();
  if (key === 'a')
    movements.steering = -1;
  else if (key === 'd')
    movements.steering = 1;
  else if (key === 'w')
    movements.throttle = 1;
  else if (key === 's')
    movements.throttle = -1;
  else
    ;
    printKey()
},true);

window.addEventListener('keyup', function(event){
  key = event.key.toLowerCase();
  if (key === 'a')
    movements.steering = 0;
  else if (key === 'd')
    movements.steering = 0;
  else if (key === 'w')
    movements.throttle = 0;
  else if (key === 's')
    movements.throttle = 0;
  else
    ;
    printKey()
}, true)

let movements = {
  throttle: 0,
  steering: 0
}

const throttle_map = new Map();
throttle_map.set(0, 'Stop');
throttle_map.set(-1, 'Reverse');
throttle_map.set(1, 'Straight');

const steering_map = new Map();
steering_map.set(0, 'Neutral');
steering_map.set(-1, 'Left');
steering_map.set(1, 'Right');

function updateScreen(){
  document.getElementById('steering').innerHTML = steering_map.get(movements.steering);
  document.getElementById('throttle').innerHTML = throttle_map.get(movements.throttle);
}

function printKey(){
  socket.emit("player_game", movements)
  updateScreen();
}
