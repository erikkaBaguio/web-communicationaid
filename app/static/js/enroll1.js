function goto_enroll(form) {
	xhr = new XMLHttpRequest();
    var url = "https://cryptic-fjord-60133.herokuapp.com/api/add_class";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () { 
        if (xhr.readyState == 4 && xhr.status == 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(json.form.classname.value);
        }
    }
    var json =JSON.stringify({"classname":form.classname.value});
    console.log(json)
    xhr.send(json);

    location="enroll_home.html";
    alert("Thanks " + form.classname.value  + "! Successfully added.");
}

function goto_home() {
	location = "enroll_home.html";
}

function goto_class2() {
	location="addclass.html";
}

function goto_classpage() {
    location="class_page.html";
}

function delete_class(val){
    if (confirm("Are you sure you want to DELETE?")) {
        var url  = "https://cryptic-fjord-60133.herokuapp.com/api/del_class="+val;
        var xhr  = new XMLHttpRequest()
        xhr.open('GET', url, true)
        xhr.onload = function () {
            var users = JSON.parse(xhr.responseText);
            if (xhr.readyState == 4 && xhr.status == "200") {
                alert('Successfully deleted');
                location = "enroll_home.html"
            } else {
                alert('error')
            }
        }
        xhr.send(null);
    }
}


function goto_enroll1() {
    location="enroll.html";
}

function classpage() {
    location="class_page.html";
}
