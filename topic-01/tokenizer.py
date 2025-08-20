import re

patterns = [
  [r"\d*\.\d+|\d+\.\d*|\d+","number"], #Number
  [r"\+","+"],                         #Plus sign
  [r".","error"]                       #Unexpected error
]

for pattern in patterns:
  pattern[0] = re.compile(pattern[0])

def tokenize(characters):
  tokens = []
  position = 0
  while (position < len(characters)):
    for pattern,tag in patterns:
      match = pattern.match(characters,position)
      if (match):
        break
      
      assert(match)
