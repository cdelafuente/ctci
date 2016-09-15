#!/user/bin/env python

def words():
  """
  A generator that iterates over the words in the `word_list.txt` file.
  """
  text = open("word_list.txt", 'r')
  for word in text:
    yield word.strip()

def compress(string):
  """
  Compress a string.

  input: 'aaabbbbcc
  output: 'a3b4c2'
  """
  compressed = []
  current = string[0]
  counter = 1

  # Compress characters
  for c in string[1:]:
    if c == current:
      counter = counter + 1
    else:
      compressed.append('%s%s' % (current, counter))
      current = c
      counter = 1

  # Append last item
  compressed.append('%s%s' % (current, counter))

  # Build compressed string
  output = ''.join(compressed)

  # Return compressed string if lenght is less than the original string
  if len(output) < len(string):
    return output
  else:
    return string
    

if __name__ == "__main__":
  for w in words():
    c = compress(w)
    print "%s => %s" % (w, c)

