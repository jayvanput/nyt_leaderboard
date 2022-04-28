// Button to open modal form
let entry_button = document.getElementById("show_form")
let close_btn = document.getElementById("form__close")
let form = document.getElementById("dialog")

entry_button.addEventListener("click",() => {
    form.showModal();
})

close_btn.addEventListener("click",() => {
    form.close()
})

// function toggle_form() {
//     form.classList.toggle("shown")
//     document.body.classList.toggle("shown")
// }

// entry_button.addEventListener("click", () => {
//     toggle_form()
// })

// // X button to close form.
// let close_button = document.getElementById("form__close")

// close_button.addEventListener("click", () => {
//     form.reset()
//     toggle_form()
// })

// Enter date sends you to that page.
// let date_picker = document.getElementById("nav__form")
// let date_picker_input = document.getElementById("nav__date")

// date_picker_input.addEventListener("change", (e) => {
//     date_picker.submit()
// })