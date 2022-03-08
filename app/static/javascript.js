let change_weight = document.getElementById("button_weight");
let change_height = document.getElementById("button_height");
let change_age = document.getElementById("button_age");
let change_tmb = document.getElementById("button_tmb");
let change_get_off = document.getElementById("button_get_off");
let change_get_workout = document.getElementById("button_get_workout");
let change_protein = document.getElementById("button_protein");
let change_fat = document.getElementById("button_fat");


change_weight.addEventListener('click', () => {
    let form = document.getElementById("change_weight");
    form.innerHTML = "<form action='/' method='post'><input type='text' name='weight'><input type='submit'></form>";
});


change_height.addEventListener('click', () => {
    let form = document.getElementById("change_height");
    form.innerHTML = "<form action='/' method='post'><input type='text' name='height'><input type='submit'></form>";
});


change_age.addEventListener('click', () => {
    let form = document.getElementById("change_age");
    form.innerHTML = "<form action='/' method='post'><input type='text' name='age'><input type='submit'></form>";
});


change_tmb.addEventListener('click', () => {
    let form = document.getElementById("change_tmb");
    form.innerHTML = "<form action='/' method='post'><input type='text' name='tmb'><input type='submit'></form>";
});


change_get_off.addEventListener('click', () => {
    let form = document.getElementById("change_get_off");
    form.innerHTML = "<form action='/' method='post'><input type='text' name='get_off'><input type='submit'></form>";
});


change_get_workout.addEventListener('click', () => {
    let form = document.getElementById("change_get_workout");
    form.innerHTML = "<form action='/' method='post'><input type='text' name='get_workout'><input type='submit'></form>";
});


change_protein.addEventListener('click', () => {
    let form = document.getElementById("change_protein");
    form.innerHTML = "<form action='/' method='post'><input type='text' name='protein'><input type='submit'></form>";
});


change_fat.addEventListener('click', () => {
    let form = document.getElementById("change_fat");
    form.innerHTML = "<form action='/' method='post'><input type='text' name='fat'><input type='submit'></form>";
});