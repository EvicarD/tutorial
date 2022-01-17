function hello() {
  return "hello world.";
}
function date() {
  const date = new Date();
  return date.getFullYear();
}
function toDo(inputValue) {
  if (inputValue) {
    const el = document.getElementById("hello");
    const div = document.createElement("div")
    const input = document.createElement("input")
    const label = document.createElement("label")
    input.setAttribute("id", inputValue)
    input.setAttribute("type", "checkbox")
    label.setAttribute("for", inputValue)
    label.innerText = inputValue
    div.appendChild(input)
    div.appendChild(label)
    el.appendChild(div)
  } 
}
export { hello, date, toDo };
