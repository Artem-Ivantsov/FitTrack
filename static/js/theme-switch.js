function toggleDarkMode() {
  const root = document.documentElement;

  if (root.style.getPropertyValue('--bg-main') === '#121212') {
    root.style.setProperty('--bg-main', '#fff');
    root.style.setProperty('--bg-secondary', '#e8e8e8');
    root.style.setProperty('--bg-accent', '#006400');
    root.style.setProperty('--bg-subaccent', '#00a650');
    root.style.setProperty('--btn-bg', '#1b5e20');
    root.style.setProperty('--btn-hover-bg', '#128c19');
    root.style.setProperty('--btn-text', '#fff');
    root.style.setProperty('--text-main', '#222');
    root.style.setProperty('--text-secondary', '#555');
    root.style.setProperty('--text-accent', '#006400');
    root.style.setProperty('--link-color', '#006400');
    root.style.setProperty('--link-hover', '#004d00');
    root.style.setProperty('--card-bg', '#f8f8f8');
    root.style.setProperty('--shadow', 'rgba(0, 0, 0, 0.15)');
    root.style.setProperty('--scrollbar-thumb', '#a8a8a8');
  } else {
    root.style.setProperty('--bg-main', '#121212');
    root.style.setProperty('--bg-secondary', '#222');
    root.style.setProperty('--bg-accent', '#004d00');
    root.style.setProperty('--bg-subaccent', '#007700');
    root.style.setProperty('--btn-bg', '#128c19');
    root.style.setProperty('--btn-hover-bg', '#1b5e20');
    root.style.setProperty('--btn-text', '#ddd');
    root.style.setProperty('--text-main', '#eee');
    root.style.setProperty('--text-secondary', '#aaa');
    root.style.setProperty('--text-accent', '#00a650');
    root.style.setProperty('--link-color', '#00a650');
    root.style.setProperty('--link-hover', '#006400');
    root.style.setProperty('--card-bg', '#1e1e1e');
    root.style.setProperty('--shadow', 'rgba(0, 0, 0, 0.8)');
    root.style.setProperty('--scrollbar-thumb', '#555');
  }
}
