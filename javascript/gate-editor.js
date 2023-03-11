window.onload = init()


function init() {
    const canvas = document.getElementById('canvas')
    const ctx = canvas.getContext('2d')
    canvas.background = "white"
    ctx.lineWidth = 3;
    ctx.imageSmoothingEnabled = false;
    canvas.width=canvas.clientWidth
    canvas.height=canvas.clientHeight
    ctx.beginPath()
    ctx.moveTo(20, 20)
    ctx.bezierCurveTo(10, 20, 40, 50, 40, 40)
    ctx.stroke()
}

