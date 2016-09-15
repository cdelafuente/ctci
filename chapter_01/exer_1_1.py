#!/user/bin/env python

def words():
  text = open("small_text.txt", 'r')
  items = text.read()
  for item in items.split():
    yield item

def has_duplicates(word):
  chars = {}
  for c in word:
    if chars.get(c) is None:
      chars[c] = 1
    else:
      return True 
  return False

if __name__ == "__main__":
  for item in words():
    if has_duplicates(item):
      print item

