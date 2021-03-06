#!/usr/bin/env python

def words():
  """
  A generator thta return the words from the `small_text.txt` file.
  """
  text = open("small_text.txt", 'r')
  content = text.read()
  for item in content.split(' '):
    yield item.strip()

def reverse(word):
  """
  Reverse the characters in the given string.
  """
  middle = len(word) / 2
  chars = list(word) 
  for x in xrange(middle):
    index = (len(chars) - 1) - x
    temp = chars[index]
    chars[index] = chars[x]
    chars[x] = temp
  return ''.join(chars) 

if __name__ == "__main__":
  for w in words():
    print "%s => %s" % (w, reverse(w))
