
function readURL(input) {


  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $('#blah').attr('src', e.target.result);
      var img_source =document.getElementById("imgInp").getAttribute('src');
      document.getElementById('get_src').innerHTML = img_source;
      // var img_source =document.getElementById("blah").getAttribute('src');
      // document.getElementById('get_src').innerHTML = img_source;
      
    }

    reader.readAsDataURL(input.files[0]);
  }
}


$("#imgInp").change(function() {
  readURL(this);
});




  function formCreate(img_name, img_type, filetype1, fileVal1,filetype2,fileVal2){
      var form = new FormData();
      for
      form.append(filetype1, fileVal1);
      form.append('type1',filetype1);
      form.append(filetype2, fileVal2);
      form.append('type2',filetype2);

      return form;
  }

  function upload(){
      $.ajax({
          type: 'POST',
              url: 'https://cryptic-fjord-60133.herokuapp.com/api/v3/upload',
              data: formCreate('img_name','img_type','image', $('input[name="image"]')[0].files[0],'audio', $('input[name="audio"]')[0].files[0]),
              cache: false,
              contentType: false,
              processData: false,
              async: false,
              success: function(response) {
                if(response.msg=='ok'){
                      alert("red")
                      console.log('Welcome Home im')
                      window.location.assign(response.next_node);
                  }
                  else{
                      console.log(response.msg);
                      alert(response.msg);
                  }
              },
      });

  }
