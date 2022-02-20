let button = document.getElementById("show_form")
let form = document.getElementById("time_form")

button.addEventListener("click", () => {
    form.classList.toggle("shown")
})