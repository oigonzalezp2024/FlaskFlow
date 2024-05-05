function myFunction(tagId = "myTopnav") {
  const x = document.getElementById(tagId);
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const btnMenu = document.getElementById('btnMenu');
  btnMenu.setAttribute('href','javascript:void(0);');
  btnMenu.addEventListener('click', () => {
    myFunction();
  });
});
