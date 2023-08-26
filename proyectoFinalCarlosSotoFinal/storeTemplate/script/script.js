document.addEventListener("DOMContentLoaded", function () {
  const container = document.querySelector(".container-fluid");
  const sections = document.querySelectorAll(".section");
  const navLinks = document.querySelectorAll(".navbar-nav .nav-link");
  const navbar = document.querySelector(".navbar");

  container.addEventListener("wheel", function (event) {
    event.preventDefault();
    container.scrollLeft += event.deltaY;
  });

  container.addEventListener("scroll", function () {
const scrollPosition = container.scrollLeft;
const containerWidth = container.offsetWidth;

sections.forEach(function (section) {
const sectionOffsetLeft = section.offsetLeft;

if (
  scrollPosition >= sectionOffsetLeft - containerWidth / 2 &&
  scrollPosition < sectionOffsetLeft + section.offsetWidth - containerWidth / 2
) {
  const sectionId = section.getAttribute("id");
  window.location.hash = sectionId;
  updateActiveNavLink(sectionId);
  return;
}
});
});


  navLinks.forEach(function (navLink) {
    navLink.addEventListener("click", function (event) {
      event.preventDefault();
      const targetId = navLink.getAttribute("href").substring(1);
      const targetSection = document.getElementById(targetId);
      const targetOffsetLeft = targetSection.offsetLeft;

      container.scrollTo({
        left: targetOffsetLeft,
        behavior: "smooth"
      });

      updateActiveNavLink(targetId);
    });
  });

  function updateActiveNavLink(sectionId) {
    navLinks.forEach(function (navLink) {
      if (navLink.getAttribute("href") === "#" + sectionId) {
        navLink.classList.add("active");
      } else {
        navLink.classList.remove("active");
      }
    });
  }
});