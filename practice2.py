for i in range(1,51):
    
  if i % 3 == 0 and i % 5 == 0:
    print(f'FizzBuzz',i)
  elif i % 3 == 0:
    print(f'fizz',i) 
  elif i % 5 == 0:
    print(f'buzz',i)
  else:
    print(i)           