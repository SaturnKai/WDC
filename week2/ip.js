const description = document.querySelector('.description');

async function main() {
  const response = await fetch('https://api.ipify.org?format=json');
  const data = await response.json();

  description.innerHTML = `
  IP addresses define the way our computers communicate to the internet, with yours being <span class="bold">131.216.14.13</span>.`
}

main();