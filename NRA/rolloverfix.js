		var defaultdesc = 'Roll over a company name to view its description.';
		$('#bw-text').html('<p>'+defaultdesc+'</p>');
	
	$('.bw-rollover').on('mouseover', function(){
		var headline = $(this).data('headline'),
			summary = $(this).data('summary');
		$(this).addClass('bw-active');
		$('#bw-text').html('<h2>'+headline+'</h2><p>'+summary+'</p>');
	  });
		
	$('.bw-rollover').on('mouseout', function(){
		$(this).removeClass('bw-active');
		$('#bw-text').html('<p>'+defaultdesc+'</p>');
	  });