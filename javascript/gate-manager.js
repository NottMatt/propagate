// get gate buttons
const andBtn = document.getElementById("and-btn");
const nandBtn = document.getElementById("nand-btn");
const orBtn = document.getElementById("or-btn");
const norBtn = document.getElementById("nor-btn");
const xorBtn = document.getElementById("xor-btn");
const xnorBtn = document.getElementById("xnor-btn");
const notBtn = document.getElementById("not-btn");
const ledRBtn = document.getElementById("led_r-btn");
const ledGBtn = document.getElementById("led_g-btn");
const ledBBtn = document.getElementById("led_b-btn");
const clockBtn = document.getElementById("clock-btn");

andBtn.addEventListener("click", buttonActivity);
nandBtn.addEventListener("click", buttonActivity);
orBtn.addEventListener("click", buttonActivity);
norBtn.addEventListener("click", buttonActivity);
xorBtn.addEventListener("click", buttonActivity);
xnorBtn.addEventListener("click", buttonActivity);
notBtn.addEventListener("click", buttonActivity);
ledRBtn.addEventListener("click", buttonActivity);
ledGBtn.addEventListener("click", buttonActivity);
ledBBtn.addEventListener("click", buttonActivity);
clockBtn.addEventListener("click", buttonActivity);

function buttonActivity() {
    console.log("click!");
}
