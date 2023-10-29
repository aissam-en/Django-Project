console.log('test signup.js');

const organisateurCategories = document.getElementById("OrganisateurCategories");
const userTypeDropdown = document.getElementById("id_user_type");

userTypeDropdown.addEventListener("change", function() {
  if (userTypeDropdown.value === 'Organisateur') {
    organisateurCategories.style.display = "block";
  } else {
    organisateurCategories.style.display = "none";
  }
});