
# range(stop = 10)
for _ in range(4):
  print('run', end=' ')
  # run run run run

# range(start = 5, stop = 10)
for i in range(5, 10):
  print(i, end=', ')
  # 5, 6, 7, 8, 9

# range(start = 2, end = 12, step = 2)
for i in range(2, 12, 2):
  print(i, end=', ')
  # 2, 4, 6, 8, 10