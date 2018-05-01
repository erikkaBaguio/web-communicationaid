function addClass() {
	var class_name = $('#child_name').val();


	$.ajax(
		{
			url: 'http://127.0.0.1:5000/addClass',
			contentType: 'application/json; charset=utf-8',
			data: JSON.stringify({
				'class_name': $("#class_name").val(),
			}),
			type: "POST",
			dataType: "json",
			error: function (e) {
			},
			success: function (resp) {
                if (resp.status == 'ok') {
                	alert("Successfully Added!")
                    window.location.replace('class.html')

                 }
				else {
					alert("ERROR")
				}

			}
		});
}

function addstudents() {
	var c_id = $('#c_id').val();


	$.ajax(
		{
			url: 'http://127.0.0.1:5000/addstudents',
			contentType: 'application/json; charset=utf-8',
			data: JSON.stringify({
				'fname_c': $("#fname_c").val(),
				'lname_c': $("#lname_c").val(),

			}),
			type: "POST",
			dataType: "json",
			error: function (e) {
			},
			success: function (resp) {
                if (resp.status == 'ok') {
                	alert("Successfully Added!")
                    window.location.replace('students.html')

                 }
				else {
					alert("ERROR")
				}

			}
		});
}