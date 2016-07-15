#!/usr/bin/env python

def is_substring(a, b):
  n = (len(a) - len(b)) + 1
  for x in xrange(n):
    for y in xrange(x, x+len(b)):
      i = a[y]
      j = b[y-x]
      if i != j:
        break
      if y == ((x + len(b)) - 1):
        return True
  return False
    

if __name__ == "__main__":
  input = [
    ('abcdefghij', 'abcd'),
    ('abcdefghij', 'abcde'),
    ('abcdefghij', 'abcdef'),
    ('abcdefghij', 'abcdefg'),
    ('abcdefghij', 'abcdefgh'),
    ('abcdefghij', 'abcdefghi'),
    ('abcdefghij', 'abcdefghij'),
    ('abcdefghij', 'bcde'),
    ('abcdefghij', 'cdef'),
    ('abcdefghij', 'defg'),
    ('abcdefghij', 'efgh'),
    ('abcdefghij', 'fghi'),
    ('abcdefghij', 'ghij'),
    ('abcdefghij', 'abce')
  ]
  for x, y in input:
    print "%s, %s => %s" % (x, y, is_substring(x, y))
