def in1to10(n, outside_mode):
  if outside_mode == True:
    a = in1to10T(n)
    return a
  else:
    b = in1to10F(n)
    return b
  
def in1to10T(n):
    if n not in range(1, 11):
      return True
    else:
      return False
      
def in1to10F(n):
    if n in range(1, 11):
      return True
    else:
      return False

in1to10(10, True)