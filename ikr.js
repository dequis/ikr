$(function (){
    $("#rnd").click(function() {
        $("#list_name").val(Math.random().toString(36).substring(2));
    })
    $(".votes a").click(function(e) {
        var that = $(this);
        e.preventDefault();
        $.get(that.attr("href") + "?format=json", function(data) {
            that.parent().children(".number").text(data.votes);
        })
    })
})
