$('.follow_toggle_button').click(function(){
    var id;
    id = $(this).attr("data-user-id");
    // console.log(id);
    $.ajax({
        type: "POST",
        url: "../follow",
        data: {user_id: id},
        success: function( data ) {
            // alert(data.followers_cnt);
            $(".follow_toggle_button").text(data.follow_button_status);
            $(".followers").text(data.followers_cnt);
            // console.log($( '#like'+id ).children().first());
            // if (data.like_status == 1) {
            //     // alert("Liked");
            //     $( '#like'+id ).children().first().attr('class', 'fas fa-heart');
            // }
            // else {
            //     // alert("Unliked");
            //     $( '#like'+id ).children().first().attr('class', 'far fa-heart');
            // }
        }
    })
})