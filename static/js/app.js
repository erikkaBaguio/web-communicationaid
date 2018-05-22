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


function addstudent() {
var c_id = $('#c_id').val();
var fname_c = $('#fname_c').val();
var lname_c = $('#lname_c').val();

$.ajax({
    // url: 'http://127.0.0.1:5000/api/addstudents',
    url: "https://mighty-badlands-16603.herokuapp.com/api/add_student",
    contentType: 'application/json; charset=utf-8',
    data: JSON.stringify({
        'c_id':$('#c_id').val(),
        'fname_c':$('#fname_c').val(),
        'lname_c':$('#lname_c').val(),
    }),    
    method: "POST",
    dataType: "json",
    crossDomain: true,
    // headers: {
    //  'x-access-token': tokens
    // },
    success: function () {
        console.log("success");
        alert("Enroll success!");
        window.location.href='/students'
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


function viewstudents(){
    table1();
    viewstud();
    showRes();
 }


function viewstud(){

		$("#view_c_id").show();

		$.ajax({
				// url: 'http://127.0.0.1:5000/api/students',
				url: 'https://mighty-badlands-16603.herokuapp.com/api/students',
				type: "GET",
				dataType: "json",
				crossDomain: true,
				//  headers: {
				// 'x-access-token': tokens
				// },
success: function(resp) {

 if (resp.status  === 'ok') {
       for (i = 0; i < resp.count; i++) {
                      c_id = resp.entries[i].c_id;
                      fname_c = resp.entries[i].fname_c;
                      lname_c = resp.entries[i].lname_c;
                      $("#view_c_id").append(showRes(c_id,fname_c,lname_c));
                            }
    } else {
        $("#view_c_id").html("");
      alert('No Data')
            }
                            }
});
         }

        function showRes(c_id,fname_c,lname_c)
        {
           return '<div class="widget-content">'+
                    '<table class="table table-striped table-bordered" id="view_res">'+
                        '<tbody><tr class="edit" id="details">'+
                            '<td>'+ c_id +'</td>'+
                            '<td>'+ fname_c +'</td>'+
                            '<td>'+ lname_c +'</td>'+
                        '</tr></tbody>' +
                    '</table>' +
               '</div>'
        }
        
        
        function table()
        {
             $("table.table-bordered").html('<thead><tr>' +
                    '<th>Class ID</th>' +
                    '<th>First Name</th>' +
                    '<th>Last Name</th>' +
                    '</tr></thead>')
        }


function viewClass(){
	 viewClas();
   showRes();
   table();
}

function viewClas(){
   $("#view_classname").show();

     $.ajax({
               url: 'https://mighty-badlands-16603.herokuapp.com/api/class_data',
               // url: 'http://127.0.0.1:5000/api/manageclass',
               type: "GET",
               dataType: "json",
               crossDomain: true,
                // headers: {
                //      'x-access-token': tokens
                //          },
               success: function(resp) {
                 if (resp.status  === 'ok') {
                    for (i = 0; i < resp.count; i++) {
                                   classname = resp.entries[i].class_name;
                                   $("#view_classname").append(showRes(class_name));
                                                             }
                 } else {
                     $("#view_classname").html("");
                    alert('No Data')
                         }
                                         }
           });
                       }  

     function showRes(class_name)
     {
        return '<div class="widget-content">'+
                 '<table class="table table-striped table-bordered" id="view_res">'+
                     '<tbody><tr class="edit" id="details">'+
                         '<td>'+ class_name +'</td>'+
                     '</tr></tbody>' +
                 '</table>' +
            '</div>'
     }


      function table()
           {
         $("table.table-bordered").html('<thead><tr>' +
                 '<th>Class Name</th>' +
                 '</tr></thead>')
           }