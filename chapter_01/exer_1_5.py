#!/user/bin/env python

def words():
  text = open("word_list.txt", 'r')
  for word in text:
    yield word.strip()

def compress(x):
  compressed = []
  counter = 1
  current = x[0]
  i = 1
  while True:
    if i >= len(x):
      break
    char = x[i]
    if char == current:
      counter = counter + 1
    else:
      compressed.append('%s%s' % (current, counter))
      current = x[i]
      counter = 1
    i = i + 1
  compressed.append('%s%s' % (current, counter))
  output = ''.join(compressed)
  return output if len(output) < len(x) else x

if __name__ == "__main__":
  for w in words():
    c = compress(w)
    print "%s => %s" % (w, c)

