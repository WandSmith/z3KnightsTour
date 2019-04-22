var row = 0
var col = 0
var pos = []
function draw(m,n){
    row = m
    col = n
    var c = document.getElementById("myCanvas")
    var ctx = c.getContext("2d")
    ctx.strokeStyle="black"
    for(i = 0;i <= m;i++){
        ctx.moveTo(0,80*i)
        ctx.lineTo(80*n,80*i)
    }
    for(i = 0;i <= n;i++){
        ctx.moveTo(80*i,0)
        ctx.lineTo(80*i,80*m)
    }
    ctx.stroke()
}

var count = 0
function update(){
    if(count < row*col){
        updateDraw(count)
        count++
        if(count === row*col){
            var button = document.getElementById("nextStep")
            button.innerText = "Finish!"
        }
    }else{}
}

function updateDraw(count){
    var c = document.getElementById("myCanvas")
    var ctx = c.getContext("2d")
    ctx.fillStyle = "yellow"
    pos_y = parseInt(pos[count] / col)
    pos_x = parseInt(pos[count] % col)
    console.log(pos_y)
    console.log(pos_x)
    ctx.fillRect(80*pos_x,80*pos_y,80,80)
    ctx.strokeStyle = "black"
    ctx.strokeRect(80*pos_x,80*pos_y,80,80)
    ctx.font = "40pt Times"
    ctx.fillStyle = "black"
    ctx.textAlign = "center"
    ctx.textBaseline = "middle"
    ctx.fillText(count+1,80*pos_x+40,80*pos_y+40)
}