$(document).ready(function() {
         // When the document is ready, the user is able to select a category before submiting the recipe
         $('select').material_select();
         // On smaller screens (mobile version) the user can use the menu by the side navigation
         $(".button-collapse").sideNav();
         // Feedback form modal
         $('.modal').modal();
         });