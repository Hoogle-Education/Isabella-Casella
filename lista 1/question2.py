def f(x):
  return 2*(x**2) - 200*x + 2500

for number in range(101):
  result = f(number)
  
  if result == 600.0:
    print(number)