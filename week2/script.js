const switchButton = document.querySelector('.switch');
const title = document.querySelector('.title');

switchButton.onclick = () => {
  const type = document.body.className;
  document.body.className = type == 'dark' ? 'light' : 'dark';
}

