var $ = INK.$;

$('.blue-star').on('mouseover', 
  function(e){ 
    $('#container').attr('class','blue-star-active');
  }
);

$('.blue-star').on('mouseout', 
  function(e){ 
    $('#container').attr('class',''); 
  }
);



// $('.scene-1a').on('click',
//  function(e){
//    $('#svg-container').attr('class', 'scene-1a-active');
//    }
//  );



new INK.Blocks('#ink-content-collection-4', { onActivate: function(index){
  var scene = (index + 1);
  $('#svg-container').attr('class', 'scene-'+scene+'-active');
  // $('#svg-container').attr('class', 'scene-'+scene+'a-active');

}});

new INK.Tooltip({ 
	target:  '#svg-container .state-law, #svg-container .scene-1, #svg-container .scene-2, #svg-container .scene-3,#svg-container .scene-4,#svg-container .scene-5,#svg-container .scene-6', 
	getContent: function(e){
    var targetID = this.$activeTarget.attr('id');
    // console.log(targetID)
    // console.log(_.find(abortionDetails, function(detail) { return details.ID == targetID; }))
    return _.find(abortionDetails, function(details) { return details.ID === targetID; }).details;


	},
	onShow: function(e,t){ 
    // INK.$(e.target).addClass('nytg-blue'); 
    // console.log('this')
	}, 
	onHide: function(e,t){
    // INK.$(e.target).removeClass('nytg-blue'); 
	} 
});