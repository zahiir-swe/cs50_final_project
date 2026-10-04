const sidebar = document.querySelector("nav");
const toggleBtn = document.querySelector("#sidebar-btn");

toggleBtn.addEventListener("click", () => {
  const closed = sidebar.classList.toggle("closed");
  toggleBtn.setAttribute("aria-expanded", String(!closed));
  toggleBtn.setAttribute("aria-label", closed ? "Ouvrir le menu" : "Réduire le menu");
});