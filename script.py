def my_function():
  # Full title should be no longer than len (e.g.25) symbols
  var = "Volvo released a new car with the following spec: V6 236HP. It will cost $22647 and going to be sold in New York only"
  title = str("25")
  print(var[0:25])

  #If title longer than len (e.g.25) symbols than you need to show “...” at the end
  if (var) > title:
    print(var,"...")

  #Title should end on full word
  

my_function()
