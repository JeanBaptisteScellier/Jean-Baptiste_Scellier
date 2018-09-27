#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

# A. utility_function
# Fonction qui lit un fichier et en extraie les mots et leur nombre d'apparitions
# Renvoie ces informations sous forme de dictionnaire
def utility_function(filename):
  f = open(filename, 'rU')
  dict = {}
  for line in f:
    for word in line.split():
      lowcase = word.lower()
      if(lowcase in dict):
        dict[lowcase] += 1
      else:
        dict[lowcase] = 1
  f.close()
  return dict

# B. print_words
# Renvoie les mots d'un fichier et leur nombre d'apparitions
def print_words(filename):
  dict = utility_function(filename)
  for key in dict:
    print key + ' ' + str(dict[key])
  return

# C. print_top
# Renvoie les 20 mots au plus grand nombre d'apparitions, chacun suivi de ce nombre
def print_top(filename):
  dict = utility_function(filename)
  # Transformation du dictionnaire en liste de tuples
  tuples = []
  for key in dict:
    tuples.append((key, dict[key]))
  # Ordonnancement de la liste en fonction du nombre d'itérations
  top = sorted(tuples, key=(lambda t: t[1]), reverse=True)
  # Affichage du top 20
  for t in top[:20]:
    print t[0] + ' ' + str(t[1])
  return

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
