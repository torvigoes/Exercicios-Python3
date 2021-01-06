from random import sample

t = tuple(sample(range(10), 5))
print(t)
print(f'O maior valor é {max(t)}\n'
      f'E o menor valor é {min(t)}')
