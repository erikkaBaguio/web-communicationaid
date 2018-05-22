//alert("hello world ");

// function change(.message a){

//     src='https://code.jquery.com/jquery-3.3.1.min.js'
//     $('.message a').click(function(){
//      $('form').animate({height:"toggle", opacity:"toggle"}, "slow");
//     });

// }
// change;
function back(){
    location=("index.html");
}

function pasuser(form) {
    var uid = form.id.value;
    var pass = form.pass.value;
    
    xhr = new XMLHttpRequest();
    var url = "https://mighty-badlands-16603.herokuapp.com/api/login";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Authorization", 'Basic ' + btoa(uid + ":" + pass));
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () { 
        if (xhr.readyState == 4 && xhr.status == 200) {
            var json = JSON.parse(xhr.responseText);
            alert(json.acc_id);
            alert(json.token);
            alert(" Successfully login");
            location="mode.html";

            console.log(json);
        }
    }
    
    var json =JSON.stringify({"username": uid, "password":pass});
    console.log(json)
    xhr.send(json);


    
    
    
}
function register_user(form,acc_type){


        
    xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/api/signup";
    xhr.open("POST", url, true);
    // xhr.setRequestHeader("Authorization", 'Basic ' + btoa(form.id.value + ":" + form.pass.value));
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () { 
        alert(xhr.status)
        if (xhr.readyState == 4 && xhr.status == 200) {
            var json = JSON.parse(xhr.responseText);
            alert("pugsit")
            console.log(json.form.id.value +", " + json.form.acc_type.value + ", " + json.form.email.value + ", " + json.form.pass.value);
        }
    }
    var json =JSON.stringify({"username": form.id.value,"acc_type":form.acc_type.value, "email":form.email.value, "password":form.pass.value});
    console.log(json)
    xhr.send(json);

    
    alert("Thanks " + form.id.value  + "! You are now Registered.");
    location="mode.html";  

}



function add_directory(form){

    var name = form.name.value;
    var contact = form.contact.value;
    var address = form.address.value;

    
        
    xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:80/directory";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () { 
        if (xhr.readyState == 4 && xhr.status == 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(json.name + ", " + json.contact + ", " + json.address);
        }
    }
    var json =JSON.stringify({"name": name, "contact":contact, "address":address});
    console.log(json)
    xhr.send(json);


    
    location="enroll_home.html"  
    alert("Thanks ! " + name  + " is successfully added to your Directory.");
    

}


// function get_req(form){

//     var what_ever = form.wtevr.value;

//     var xhr = new XMLHttpRequest();
//     xhr.open("GET", "https://127.0.0.1:5000/what_ever");
//     xhr.send();

//     console.log(xhr.status);
//     console.log(xhr.statusText);

// }
