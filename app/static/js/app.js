function login() {
  var username = $("#username").val();
  var password = $("#password").val();

    $.ajax({
        url: "https://cryptic-fjord-60133.herokuapp.com/api/login",
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
        success: function(resp) {
            if(resp.acc_type == '2'){
            localStorage.setItem('acc_type', resp.acc_type);
            localStorage.setItem('acc_id', resp.acc_id);
            console.log("success");
            localStorage.setItem('token', resp.token);
            window.location.href ='/dashboard/teacher/'+resp.acc_id;
            console.log(resp);
          }
          if(resp.acc_type == '1'){
            localStorage.setItem('acc_type', resp.acc_type);
            localStorage.setItem('acc_id', resp.acc_id);
            console.log("success");
            localStorage.setItem('token', resp.token);
            window.location.href ='/mode/'+resp.acc_id;
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
  var username = $("#username").val();
  var email = $("#email").val();
  var password = $("#password").val();
    $.ajax({
        url: 'https://cryptic-fjord-60133.herokuapp.com/api/signup',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            'acc_type': acc_type,
            'username': username,
            'email': email,
            'password': password
        }),
        type: "POST",
        dataType: "json",
        crossDomain: true,
         success: function(resp) {
            if(resp.acc_type == '2'){
            localStorage.setItem('acc_type', resp.acc_type);
            localStorage.setItem('acc_id', resp.acc_id);
            console.log("success");
            localStorage.setItem('token', resp.token);
            window.location.href ='/personalinfo/teacher/'+resp.acc_id;
            console.log(resp);
          }
          if(resp.acc_type == '1'){
            localStorage.setItem('acc_type', resp.acc_type);
            localStorage.setItem('acc_id', resp.acc_id);
            console.log("success");
            localStorage.setItem('token', resp.token);
            window.location.href ='/personalinfo/parent/'+resp.acc_id;
            console.log(resp);
          }
        },
        error: function (e) {
          console.log(e);
        console.log('BYE');
        }
    });
}
function create() {
    window.location.href='/signup';
}

// function child(){
//     var gender = $('gender').val();
//     $.ajax({
//         url: "https://api/pic-a-talk/api/child/"+c_id;
//         contentType: 'application/json; charset=utf-8',
//         type: "GET",
//         dataType: "json",
//         crossDomain: true,
//         success: function(){
//             window.location.href="/api/child/"+c_id;
//             alert("DONE");
//         }
//         error: function(){
//             window.location.href = "/api/child/"+c_id;
//             alert("PAGSHOR")
//         }
//     })
// }

function addClass(){
  var class_name = $("#class_name").val();

    $.ajax({
        url: "https://cryptic-fjord-60133.herokuapp.com/api/add_class",
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
function register_user(form,acc_type){
       
    xhr = new XMLHttpRequest();
    var url = "https://cryptic-fjord-60133.herokuapp.com/api/signup";
    xhr.open("POST", url, true);
    // xhr.setRequestHeader("Authorization", 'Basic ' + btoa(form.id.value + ":" + form.pass.value));
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () { 
        alert(xhr.status)
        if (xhr.readyState == 4 && xhr.status == 200) {
            alert("success")
            var json = JSON.parse(xhr.responseText);
            location="mode.html";  
            console.log(json.form.id.value +", " + json.form.acc_type.value + ", " + json.form.email.value + ", " + json.form.pass.value);
        }
    }
    var json =JSON.stringify({"username": form.id.value,"acc_type":form.acc_type.value, "email":form.email.value, "password":form.pass.value});
    console.log(json)
    xhr.send(json);

    
    alert("Thanks " + form.id.value  + "! You are now Registered.");
    

}
