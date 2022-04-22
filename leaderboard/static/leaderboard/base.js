// Button to open modal form
let entry_button = document.getElementById("show_form")
let form = document.getElementById("time_form")

function toggle_form() {
    form.classList.toggle("shown")
    document.body.classList.toggle("shown")
}

entry_button.addEventListener("click", () => {
    toggle_form()
})

// X button to close form.
let close_button = document.getElementById("form__close")

close_button.addEventListener("click", () => {
    form.reset()
    toggle_form()
})