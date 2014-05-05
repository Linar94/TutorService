$(document).ready(function(){
	$('#reg').click(function() {
		$('.form').css('display', 'inline').
		animate({top: '10px'}, 'slow');
		$('.do').css('display', 'inline');
	});

	$('#close').click(function() {
		$('.form').css('display', 'none').
		css({top: '-505px'});
		$('.do').css('display', 'none');
	});

	$(function() {
		$('.list li').click(function() {
			$(this).children('ul').toggle();
		});
	});
	
	$(function(){
    	$('.tutor').hide();
    });

	$(function(){
        $('#id_category').change(function(){
         curselect = $('#id_category :selected').val();
         if(curselect == 2) {
         	$('.tutor').show();
         }else{
         	$('.tutor').hide();
         }
    });
});

});