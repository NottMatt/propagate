function preload() {
    andGate = loadImage("../svg/and.svg");
    nandGate = loadImage("../svg/nand.svg");
    norGate = loadImage("../svg/nor.svg");
    notGate = loadImage("../svg/not.svg");
    orGate = loadImage("../svg/or.svg");
    xnorGate = loadImage("../svg/xnor.svg");
    xorGate = loadImage("../svg/xor.svg");
    clockGate = loadImage("../svg/clock.svg");
}

function setup() {
    let windowRoot = document.querySelector(".editor-window");
    let width = windowRoot.offsetWidth;
    let height = windowRoot.offsetHeight;
    console.log({ width, height });
    let cnv = createCanvas(width, height);
    cnv.parent("editor-window");
    cnv.style("border-radius", "6px");
  }

  function draw() {
    let windowRoot = document.querySelector(".editor-window");
    let width = windowRoot.offsetWidth;
    let height = windowRoot.offsetHeight;
    resizeCanvas(width, height);
    background(30, 30, 35);
  }