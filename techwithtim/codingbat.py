def missing_char(str, n):
  front = str[:n]
  back = str[n+1:]
  return front + back

def front_back(str):
  if len(str) <= 1:
    return str
    
  mid = str[1:len(str)-1]
  
  return str[len(str)-1] + mid + str[0]

