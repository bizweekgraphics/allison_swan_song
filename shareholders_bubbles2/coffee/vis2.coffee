# HUGE THANKS to Jim Vallandingham for walking me through coffeescript !!!!! 

class BubbleChart
  constructor: (data) ->
    @data = data
    @width = 950
    @height = 760

    @tooltip = CustomTooltip("gates_tooltip", 240)

    # locations the nodes will move towards
    # depending on which view is currently being
    # used
    @center = {x: @width / 2, y: @height / 2.2}
    @industry_centers = {
      "Technology": {x: 350, y: @height / 2.5},
      "Financial": {x: 375, y: @height / 1.45},
      "Energy": {x: 475, y: @height / 1.4},
      "Basic materials": {x: 625, y: @height / 1.35},
      "Industrial": {x: 650, y: @height / 3},
      "Utilities": {x: 750, y: @height / 1.3},
      "Communications": {x: 450, y: @height / 3},
      "Consumer,Non-cyclical": {x: 250, y: @height / 1.4},
      "Consumer,Cyclical": {x: 550, y: @height / 3},
    }

    # used when setting up force and
    # moving around nodes
    @layout_gravity = -0.01
    @damper = 0.1

    # these will be set in create_nodes and create_vis
    @vis = null
    @nodes = []
    @force = null
    @circles = null

    # nice looking colors - no reason to buck the trend
    @fill_color = d3.scale.ordinal()
      .domain(["Technology","Financial","Energy","Basic materials","Industrial","Utilities","Communications","Consumer,Non-cyclical","Consumer,Cyclical"])
      .range(["#FFFF00", "#00FFFF", "#00ff00","#ff00ff","#FF0000","#6600CC","#0000FF","#FF6600","#9900CC"])

    # use the max total_amount in the data as the max in the scale's domain
    max_amount = d3.max(@data, (d) -> parseInt(d.total_amount))
    @radius_scale = d3.scale.pow().exponent(.5).domain([0, max_amount]).range([2, 85])
    
    this.create_nodes()
    this.create_vis()

  # create node objects from original data
  # that will serve as the data behind each
  # bubble in the vis, then add each node`````````````  ````  ``  `
  # to @nodes to be used later
  create_nodes: () =>
    @data.forEach (d) =>
      node = {
        id: d.id
        radius: @radius_scale(parseInt(d.total_amount*5))
        value: d.total_amount
        name: d.name
        industry: d.industry
        company: d.company
        x: Math.random() * 900
        y: Math.random() * 800
      }
      @nodes.push node

    @nodes.sort (a,b) -> b.value - a.value


  # create svg at #vis and then 
  # create circle representation for each node
  create_vis: () =>
    @vis = d3.select("#vis").append("svg")
      .attr("width", @width)
      .attr("height", @height)
      .attr("id", "svg_vis")

    @circles = @vis.selectAll("circle")
      .data(@nodes, (d) -> d.name)

    # used because we need 'this' in the 
    # mouse callbacks
    that = this

    # radius will be set to 0 initially.
    # see transition below
    @circles.enter().append("circle")
      .attr("r", 0)
      .attr("fill", (d) => @fill_color(d.industry))
      .attr("stroke-width", 2)
      .attr("id", (d) -> "#{d.name}")
      .on("mouseover", (d,i) -> that.show_details(d,i,this))
      .on("mouseout", (d,i) -> that.hide_details(d,i,this))

  


    # Fancy transition to make bubbles appear, ending with the
    # correct radius
    @circles.transition().duration(2000).attr("r", (d) -> d.radius)


  # Charge function that is called for each node.
  # Charge is proportional to the diameter of the
  # circle (which is stored in the radius attribute
  # of the circle's associated data.
  # This is done to allow for accurate collision 
  # detection with nodes of different sizes.
  # Charge is negative because we want nodes to 
  # repel.
  # Dividing by 8 scales down the charge to be
  # appropriate for the visualization dimensions.
  charge: (d) ->
    -Math.pow(d.radius, 2.0) / 8

  # Starts up the force layout with
  # the default values
  start: () =>
    @force = d3.layout.force()
      .nodes(@nodes)
      .size([@width, @height])

  # Sets up force layout to display
  # all nodes in one circle.
  display_group_all: () =>
    @force.gravity(@layout_gravity)
      .charge(this.charge)
      .friction(0.9)
      .on "tick", (e) =>
        @circles.each(this.move_towards_center(e.alpha))
          .attr("cx", (d) -> d.x)
          .attr("cy", (d) -> d.y)
    @force.start()

    this.hide_industry()

  # Moves all circles towards the @center
  # of the visualization
  move_towards_center: (alpha) =>
    (d) =>
      d.x = d.x + (@center.x - d.x) * (@damper + 0.02) * alpha
      d.y = d.y + (@center.y - d.y) * (@damper + 0.02) * alpha

  # sets the display of bubbles to be separated
  # into each year. Does this by calling move_towards_year
  display_by_industry: () =>
    @force.gravity(@layout_gravity)
      .charge(this.charge)
      .friction(0.9)
      .on "tick", (e) =>
        @circles.each(this.move_towards_industry(e.alpha))
          .attr("cx", (d) -> d.x)
          .attr("cy", (d) -> d.y)
    @force.start()

    this.display_industry()

  # move all circles to their associated @industry_centers 
  move_towards_industry: (alpha) =>
    (d) =>
      target = @industry_centers[d.industry]
      d.x = d.x + (target.x - d.x) * (@damper + 0.02) * alpha * 1.1
      d.y = d.y + (target.y - d.y) * (@damper + 0.02) * alpha * 1.1

  # Method to display year titles
  display_industry: () =>
    industry_x = {"Technology": 200, "Financial": 375, "Energy": 525, "Basic materials": 700, "Industrial": 775, "Utilities": 850, "Communications": 400, "Consumer, Non-cyclical": 175, "Consumer, Cyclical": 600}
    industry_y = {"Technology": 15, "Financial": 600, "Energy": 600, "Basic materials": 600, "Industrial": 15, "Utilities": 600, "Communications": 15, "Consumer, Non-cyclical": 600, "Consumer, Cyclical": 15}
    industry_data = d3.keys(industry_x)
    industry = @vis.selectAll(".industry")
      .data(industry_data)

    industry.enter().append("text")
      .attr("class", "industry")
      .attr("x", (d) => industry_x[d] )
      .attr("y", (d) => industry_y[d] )
      .attr("text-anchor", "middle")
      .text((d) -> d)

  # Method to hide year titiles
  hide_industry: () =>
    industry = @vis.selectAll(".industry").remove()

  show_details: (data, i, element) =>
    d3.select(element).attr("stroke", "black")
    content = "<span class=\"name\">#{data.name}</span><br/>"
    content +="<span class=\"title\"> #{data.company}</span><br/>"
    content +="<span class=\"title\">Value of shares:</span><span class=\"value\"> $#{addCommas(data.value)}</span>"
    @tooltip.showTooltip(content,d3.event)


  hide_details: (data, i, element) =>
    d3.select(element).attr("stroke", (d) => d3.rgb(@fill_color(d.industry)).darker())
    @tooltip.hideTooltip()


root = exports ? this

$ ->
  chart = null

  render_vis = (csv) ->
    chart = new BubbleChart csv
    chart.start()
    root.display_all()
  root.display_all = () =>
    chart.display_group_all()
  root.display_industry = () =>
    chart.display_by_industry()
  root.toggle_view = (view_type) =>
    if view_type == 'industry'
      root.display_industry()
    else
      root.display_all()

  d3.csv "data/500CLEAN.csv", render_vis
