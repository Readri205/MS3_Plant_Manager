/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
});
/*
    vanilla JavaScript for MaterializeCSS initialization
*/

// document.addEventListener('DOMContentLoaded', function () {
//     let sidenavs = document.querySelectorAll(".sidenav");
//     let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});
// });

$(document).ready(function () {
    $('.collapsible').collapsible();
    $('select').material_select();
    $('.button-collapse').sideNav();
});
$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
});
document.getElementById("matfix").addEventListener("click", function (e) {
    e.stopPropagation();
});
document.getElementById("matfix1").addEventListener("click", function (e) {
    e.stopPropagation();
});
document.getElementById("matfix2").addEventListener("click", function (e) {
    e.stopPropagation();
});