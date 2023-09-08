dict = {
  'a': 1,
  'b': 3,
  'c': 3
}

counter = 0

for key , val in dict.items():
  if val > 1: 
    counter += 1
    
print(counter)