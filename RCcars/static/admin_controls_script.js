socket = io()

window.onload = function(){
    socket.emit("get_db")
    update_elements()
}

let admin_controls = {
    start : false,
    reset : false
}

// Sockets
socket.on("admin_controls", function(){
    console.log(admin_controls.reset, admin_controls.start)
});

socket.on("receive_db", function(data){
    console.log("Hello")
    console.log(data)
})


// Functions
function update_elements(){
    if (admin_controls.start){
        document.getElementById("text-start").innerHTML = "Game Running!"
        document.getElementById("btn-start").innerHTML = "Stop Race"
        document.getElementById("text-reset").style.display = 'none'
        document.getElementById("btn-reset").style.display = 'none'

    }
    else{
        document.getElementById("text-start").innerHTML = "Game Not Running!"
        document.getElementById("btn-start").innerHTML = "Start Race"
        document.getElementById("text-reset").style.display = 'inline'
        document.getElementById("btn-reset").style.display = 'inline'
    }
    if (admin_controls.reset){
        document.getElementById("text-reset").innerHTML = "New Players can Join!"
        document.getElementById("btn-reset").innerHTML = "Start Game"
    }
    else{
        document.getElementById("text-reset").innerHTML = "New Player Cannot Join!"
        document.getElementById("btn-reset").innerHTML = "Reset"
    }
}

function ClickedRestart(){
    admin_controls.start = !admin_controls.start
    
    socket.emit("get_db")
    update_elements()

    socket.emit("change_game", admin_controls)
}

function ClickedReset(){
    admin_controls.reset = !admin_controls.reset

    update_elements()

    socket.emit("game_state", admin_controls)
}
