$(function (){
    $("#rnd").click(function() {
        $("#list_name").val(Math.random().toString(36).substring(2));
    })
    $(".votes a").click(function(e) {
        var that = $(this);
        var tr = that.parent().parent()
        e.preventDefault();
        $.get(that.attr("href") + "?format=json", function(data) {
            that.parent().children(".number").text(data.votes);

            /* should we reorder? */
            prev = tr.prev();
            if (prev && prev.find(".votes .number").text() < data.votes) {
                tr.insertBefore(prev);
            }

            next = tr.next();
            if (next && next.find(".votes .number").text() > data.votes) {
                tr.insertAfter(next);
            }
        })
    })
})
