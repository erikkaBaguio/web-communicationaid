function progress() {
    $.ajax({
        url: 'http://127.0.0.1:5000/api/educational/progress/',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            'prog_num': $("#prog_num").val(),
            'title': $("#title").val(),
            'details': $("#details").val(),
            'prog_date': $("#prog_date").val(),
            'prog_time': $("#prog_time").val(),
            'score': $("#score").val(),
            'ed_num': $("#ed_num").val()
        }),
        type: "POST",
        dataType: "json",
        crossDomain: true,
        success: function (resp) {
                console.log("success")

        },
        error: function (resp) {
            window.location.replace('/texts/404.html');
        }
    });
}
