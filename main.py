"""
    https://github.com/pwaller/pyfiglet

    Font Types:
    - 3x5
    - 5lineoblique
    - alligator
    - alphabet
    - banner3-D
    - bubble
    - bulbhead
    - digital
    - doh
    - dotmatrix
    - isometric1
    - letters
    - slant
"""
import os
import sys
import pyfiglet
  
output = ''
root = f'{os.getcwd()}\main.py'
for i in sys.argv:
    output += i

output = output.replace(root, '')
result = pyfiglet.figlet_format(output, font = 'slant')
print(result)


