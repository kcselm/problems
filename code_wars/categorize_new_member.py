input = [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]

def openOrSenior(data):
  result = []
  for i in data: 
    if i[0] > 54 and i[1] > 6:
      result.append("Senior")
    else:
      result.append("Open")
  return result
  
print(openOrSenior(input))