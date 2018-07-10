//alert("hello world ");

// function change(.message a){

//     src='https://code.jquery.com/jquery-3.3.1.min.js'
//     $('.message a').click(function(){
//      $('form').animate({height:"toggle", opacity:"toggle"}, "slow");
//     });

// }
// change;
function back(){
    location=("directory.html");
}

function pasuser(form) {
    var uid = document.getElementById("id");
    var pass = document.getElementById("pass");
    
    xhr = new XMLHttpRequest();
    var url = "https://mighty-badlands-16603.herokuapp.com/api/login";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () { 
        if (xhr.readyState == 4 && xhr.status == 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(json.uid + ", " + json.pass);
        }
    }
    var json =JSON.stringify({"username": uid, "password":pass});
    console.log(json)
    xhr.send(json);


    
    location="mode.html"  
    alert("Thanks ! " + name  + " is successfully added to your Directory.");
}

function register_user(form,acc_type){


        
    xhr = new XMLHttpRequest();
    var url = "https://cryptic-fjord-60133.herokuapp.com/api/signup";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () { 
        if (xhr.readyState == 4 && xhr.status == 200) {
            var json = JSON.parse(xhr.responseText);
            
            console.log(json.form.id.value +", " + acc_type+ ", " + json.form.email.value + ", " + json.form.pass.value);
        }
    }
    var json =JSON.stringify({"username": form.id.value,"acc_type":acc_type, "email":form.email.value, "password":form.pass.value});
    
    xhr.send(json);

    location="mode.html";
    alert("Thanks " + form.id.value  + "! You are now Registered got to mode.");
       

}


function add_directory(form){

    var name = form.name.value;
    var contact = form.contact.value;
    var address = form.address.value;

    
        
    xhr = new XMLHttpRequest();
    var url = "https://cryptic-fjord-60133.herokuapp.com/api/add_directory";
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


    
    location="directory.html"  
    alert("Thanks ! " + name  + " is successfully added to your Directory.");
    

}

function update_directory(form){
    if (confirm("Do you want to save Changes?")) {
        var name = form.name.value;
        var contact = form.contact.value;
        var address = form.address.value;

        var dir_id= localStorage.getItem("dir_id");
            
        xhr = new XMLHttpRequest();
        var url = "https://cryptic-fjord-60133.herokuapp.com/api/edit_directory="+dir_id;
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


        
        location="directory.html"  
        alert("Thanks for your help! " + name  + " is now successfully updated.");
        
    }
}




