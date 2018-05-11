function login() {
  var username = $("#username").val();
  var password = $("#password").val();

    $.ajax({
        url: "https://mighty-badlands-16603.herokuapp.com/api/login",
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            'username': username,
            'password': password
        }),
        type: "POST",
        dataType: "json",
        crossDomain: true,
        headers: {
            'Authorization' : 'Basic ' + btoa(username + ':' + password)
        },
        // beforeSend: function (xhr) {
        //     xhr.setRequestHeader("Authorization", auth)
        // },
        success: function(resp) {
            if(resp.acc_type == '1'){
            localStorage.setItem('acc_type', resp.acc_type);
            localStorage.setItem('acc_id', resp.acc_id);
            console.log("success");
            localStorage.setItem('token', resp.token);
            window.location.href ='/mode/<int:acc_id>';
            alert('login success!');
            console.log(resp);
          }
          if(resp.acc_type == '2'){
            localStorage.setItem('acc_type', resp.acc_type);
            localStorage.setItem('acc_id', resp.acc_id);
            console.log("success");
            localStorage.setItem('token', resp.token);
            window.location.href ='/mode/<int:acc_id>';
            alert('login success!');
            console.log(resp);

          }
        },
        error: function(e, stats, err){
      console.log(err);
      console.log(stats);
    }
    })
}
function createuser() {
    console.log('qwertyuiop');
  var acc_type = $("#acc_type").val();
  var username = $("#username_r").val();
  var email = $("#email").val();
  var password = $("#password_r").val();
    .ajax({
        url: 'https://mighty-badlands-16603.herokuapp.com/api/signup',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            // 'acc_id': $("#acc_id").val(),
            'acc_type': acc_type,
            'username': username,
            'email': email,
            'password': password
        }),
        type: "POST",
        dataType: "json",
        crossDomain: true,
        success: function (resp) {
          alert('okkkkkkkkkkkkk');
            console.log("success");
            console.log(resp);

        },
        error: function (e) {
          console.log(e);
        console.log('BYE');
            // window.location.replace('/texts/404.html');
        }
    });
}
function create() {
    window.location.href='/signup';
}
function addClass(){
  var class_name = $("#class_name").val();

    $.ajax({
        // url: 'http://127.0.0.1:5000/api/addClass',
        url: "https://mighty-badlands-16603.herokuapp.com/api/add_class",
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            'classname': class_name
        }),    
        type: "POST",
        dataType: "json",
        crossDomain: true,
        // headers: {
        //  'x-access-token': tokens
        // },
        success: function () {
            console.log("success");
            alert("Added class success!");
            // window.location.assign("/manageclass")
        },
        error: function () {
            console.log('error')
        },
        complete: function (jqXHR) {
            if (jqXHR.status == '401') {
                console.log(jqXHR.status)
            }
        }
    });
}