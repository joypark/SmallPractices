def string_match(a, b):
  #figure out which string is shorter
  shorter = min(len(a), len(b))
  count = 0
  #loop i over every substring starting spot
  #use length-1 here, so can usechar str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1



  print
  print
  print "Your count is",count
  return count
#
# print ("%", &count)
string_match('xxcasdasdaaazz', 'xaxbaaz')
string_match('h', 'hello')