document.addEventListener("DOMContentLoaded", function () {
  
    // === NAVBAR ACTIVATOR ===
    // Sets the current site's navbar link to active ===
    // Adds 'active' to the class list on the navbar links according to the current site url ending
  
      const navbarLinks = document.querySelectorAll("#navbar a.nav-link"); // Get all navbar link elements
      let currentPath = window.location.pathname; // Get the current path
    
      // Iterate through every link element
      navbarLinks.forEach(link => {
        if (link.getAttribute("href") === currentPath) {
          link.classList.add("active"); // Add active class tag
        } else {
          link.classList.remove("active"); // remove active class tag
        }
      });
  
    // === END OF NAVBAR ACTIVATOR ===
});