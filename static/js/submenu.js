document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.second_menu a[data-section]').forEach(link => {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      const section = this.dataset.section;

      document.querySelectorAll('.submenu .submenu-content').forEach(sub => {
        sub.style.display = sub.dataset.content === section ? 'block' : 'none';
      });
    });
  });

  const defaultSection = 'home';
  document.querySelectorAll('.submenu .submenu-content').forEach(sub => {
    sub.style.display = sub.dataset.content === defaultSection ? 'block' : 'none';
  });
});