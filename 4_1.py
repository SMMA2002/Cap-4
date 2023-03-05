from SimpleStack import *

s = Stack(3)
s.push('A')
s.push('B')
s.push('C')
print(str(s)) # Imprime '[A, B, C]'

try:
    s.push('D') # This will cause an exception
except Exception as e:
    print(e) # Imprime 'Stack excedido'
    
s.pop()
s.pop()
s.pop()
print(str(s)) # Imprime '[]'

try:
    s.pop() # This will cause an exception
except Exception as e:
    print(e) # Imprime 'Stack bajo del tamaño'
