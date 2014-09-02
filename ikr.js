$(function (){
    $("#rnd").click(function() {
        $("#list_name").val(Math.random().toString(36).substring(2));
    })
})
