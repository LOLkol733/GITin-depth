const menuActive = document.querySelector("div.menu");
console.log(menuActive);

const menuClose = menuActive.querySelector("button.menu__close");
console.log(menuClose);

const menuButton = document.querySelector("a.menu__button");
console.log(menuButton);

const topEl = document.querySelector("div.top");
console.log(topEl);

menuButton.addEventListener("click", function (e) {
  menuActive.classList.toggle("hidden");
  topEl.classList.toggle("top__image_menu");
});

menuClose.addEventListener("click", function (e) {
  menuActive.classList.toggle("hidden");
  topEl.classList.toggle("top__image_menu");
});
