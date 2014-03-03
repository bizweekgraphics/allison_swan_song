// ##Requires:
// ### jQuery.js

INK.Blocks = function( el, options ) {
  this.$            = INK.$;
  var defaults      = {
    // the content collection container
    $el               : this.$(el),
    History           : null,
    
    via               : 'index', //or by slug
    history           : false,
    // selector to find the nav item
    navSelector       : '.ink-content-item',
    // selector to find the content block    
    blockSelector     : '.ink-content-block',
    activeNavClass    : 'ink-content-item-active',
    activeBlockClass  : 'ink-content-block-active',    
    patternPrefix     : 'panel',
    URLPattern        : null,
    $navItems         : null, 
    $blocks           : null,
    onActivate        : function(){ return null; }
  };
  
  if ( arguments.length > 1 ) {
    this.$.extend(defaults, options);
  }  
  
  this.$.extend(this, defaults);
  
  if (this.$el.length > 1) {
    throw 'You can only target one content collection at a time';
    return;
  }  
  this.init();  
};


INK.Blocks.prototype = {
  init : function() {
    // if mobile, we'll use touch events to make it feel a little faster from the UI
    var e = (INK.isMobile()) ? 'touch' : 'click';
    
    this.$navItems  = this.$el.find(this.navSelector);
    this.$blocks    = this.$el.find(this.blockSelector);

    this.$navItems.on(e, this.$.proxy(this.handleNav, this));

    // if bookmarking is enabled, we'll check for the pattern in the url and activate block if it matches
    if ( this.history ) {
      this.URLPattern = new RegExp('#'+this.patternPrefix+'\/([a-zA-Z0-9_]*)','i');
      this.History    = new INK.History(this);
      this.History.register(this.URLPattern, this.$.proxy(this.activate, this));
      this.History.loadURL(true);
    }
    
    // If it can't find an already active block, it will trigger the first
    // if ( this.$el.find('.'+this.activeNavClass).length === 0 ) {
    //   this.$(this.$navItems[0])[e]();
    // }

    return this;
  },
    
  // Handle the click|touch activation event
  handleNav: function( e ) {
    var $target, $navItem, identifier;
    $target   = this.$(e.target);
    $navItem  = ($target.hasClass(this.navSelector.substr(1,this.navSelector.length))) ? $target : $target.parents(this.navSelector);
    
    // Extract the unique identifier based on the via option. Defaults to ordered index, but you can pass in an arbritary DATA attribute to look for
    identifier = (this.via === 'index') ? this.$navItems.index($navItem) : $navItem.data(this.via);

    this.activate(identifier);
  },
  
  // Toggle the nav item and its corresponding block as selected
  activate:  function ( identifier ) {
    var slug, $navItem, $block;
    
    if ( this.via === 'index' ) {
      $navItem  = this.$(this.$navItems[identifier]);
      $block    = this.$(this.$blocks[identifier]);
    }else{
      $navItem  = this.$el.find(this.navSelector+'[data-'+this.via+'="'+identifier+'"]');
      $block    = this.$el.find(this.blockSelector+'[data-'+this.via+'="'+identifier+'"]');
    }

    // hide and activate items
    this.$el.find('.'+this.activeNavClass).removeClass(this.activeNavClass);
    $navItem.addClass(this.activeNavClass);
    // hide and activate blocks  
    this.$el.find('.'+this.activeBlockClass).removeClass(this.activeBlockClass);
    $block.addClass(this.activeBlockClass);  
    
    // Change the hash if bookmarking is enabled. Will create a history entry
    if ( this.history ) {
      slug = $block.data('slug');
      this.History.save(this.patternPrefix+'/'+slug);    
    }
    // Trigger the optional activate event
    this.onActivate(identifier);
    return this;
  }
    
};