const buttons = document.querySelectorAll('button');
const box = document.querySelector('#box');

buttons.forEach((button) => {
  button.addEventListener('click', () => {
    const color = button.innerHTML;
    box.style.background = color;
  });
});
