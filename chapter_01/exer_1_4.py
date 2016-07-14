#!/user/bin/env python

def convert(x, length):
  i = 0
  items = []
  word = []
  is_word = False
  while True:
    if i < length:
      c = x[i]
      if c != ' ':
        items.append(c)
        is_word = True;
      else:
        if is_word:
          items.append('%20')
          is_word = False
    else:
      break;
    i = i + 1
  return ''.join(items) 

if __name__ == "__main__":
  print convert('Mr John Smith  ', 13)
