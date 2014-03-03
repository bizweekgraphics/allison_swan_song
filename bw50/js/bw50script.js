var $ = INK.$;


new INK.Blocks('#ink-content-collection-4', { onActivate: function(index){
  var scene = (index + 1);
  $('#container').attr('class', 'scene-'+scene+'-active');
  // $('#svg-container').attr('class', 'scene-'+scene+'a-active');

}});

