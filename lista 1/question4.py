list = [134, 137, 243, 243, 137, 137, 201]
dict = {}

for i in range(len(list)):
  elem = list[i]
  
  if elem not in dict.keys():
    dict[elem] = 1
  else:
    dict[elem] += 1
    
  print(f'element: {elem} | dict: {dict}')
    
for tag, quantity in dict.items():
  print(f'{tag}: {quantity}')