var username = $("#usern").val();
var password = $("#passw").val();

function make_base_auth(user, password) {
  var to = user + ':' + password;
  var hash = btoa(to);
  return "Basic " + hash;
}

var auth = make_base_auth(username,password);

function login() {
    $.ajax({
        url: "http://127.0.0.1:5000/login/",
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            'username': username,
            'password': password
        }),
        method: "GET",
        dataType: "json",
        crossDomain: true,
        headers: {
            'Authorization' : 'Basic ' + btoa(username + ':' + password)
        },

        success: function(resp) {
            console.log("success");
            localStorage.setItem('token', resp.token);
            window.location.replace('teacher.html');
            alert.message('login successful!')
        },
        error: function () {
            console.log('error')
        }
    })
}
