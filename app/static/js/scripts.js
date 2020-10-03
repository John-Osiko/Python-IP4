$(document).ready(function() {
    $("#profbutton").click(function() {
        $("#profbutton").slideDown('1000').hide('1000');
        $("#form").show('1000');
    });
    $("#submit").click(function() {
        $("#profbutto").slideUp('1000');
        $("#form").slideDown('1000');
    });



    $("#showform").click(function() {
        $("#profileupdate").slideDown('1500');
    });
    $("#submit").click(function() {
        $("#profileupdate").slideUp('1500');

    });

});