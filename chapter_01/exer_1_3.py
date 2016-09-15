#!/usr/bin/env python

def frequency(a):
  """
  Count the frequency of characters in a given string.
  """
  freq = {}
  for c in a:
    if freq.get(c) is None:
      freq[c] = 1
    else:
      freq[c] = freq[c] + 1
  return freq

def is_permutation(a, b):
  """
  Check if a string is a permutation of the other.
  """
  if len(a) == len(b):
    freqa = frequency(a)
    freqb = frequency(b)
    for key, value in freqa.items():
      if freqb.get(key) is None:
        return False
      else:
        if freqb.get(key) != value:
          return False
    return True
  return False

if __name__ == "__main__":
  options = [
    ('abcde', 'abced'),
    ('abcde', 'abcdf'),
    ('abcde', 'abcdef'),
    ('abcdef', 'abcde'),
    ('abcde', 'abcee')
  ]
  
  for item in options:
    a, b = item
    print "%s, %s => %s" % (a, b, is_permutation(a, b))

