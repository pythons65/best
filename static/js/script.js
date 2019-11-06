$('button').on('click',function(){
	var name = $('.name').val()
	var email = $('.email').val()
	var msg = $('textarea').val()
	$.ajax({
		url: '/submit',
        data: {
          'username': name,
          'email': email,
          'msg': msg
        },
        dataType: 'json',
        success: function (data){
		if(data.valid){
			alert('done');
		}else{
			alert('not sent');
		}
	}
	})
})