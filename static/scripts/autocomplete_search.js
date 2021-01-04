function searchOpen() {
    var search = $('#txtSearch').val()
    var data = {
        search: search
    };
    $.ajax({
        type: "GET",
        url: '/search.json',
        data: data,
        dataType: 'jsonp',
        jsonp: 'callback',
        jsonpCallback: 'searchResult'
    });
}


function searchResult(data) {
    $( "#txtSearch" ).autocomplete ({
        source: data,
        select: function() {
            var user_to_search = $('#txtSearch').val();
            window.location.href = "/users/"+user_to_search;
        }
    });
}