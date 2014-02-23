def get_coords():
  coords = raw_input("coords x,y: ")
  coords.split(",")
  if(len(coords.split(",")) == 2):
    x_str,y_str = coords.split(",")
    try:
      x = int(x_str)
    except ValueError:
      print("error, input again")
      return get_coords()
      #
    try:
      y = int(y_str)
    except ValueError:
      print("error, input again")
      return get_coords()
      # 
    return x,y
  else:
    print("error, input again")
    return get_coords()