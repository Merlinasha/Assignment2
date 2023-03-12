#Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

def last(n): 
   return n[-1]

def sort(tuples):
  return sorted(tuples, key=last)

print(sort([(2,5),(1,4),(2,2),(3,1),(6,3)]))



#  Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

character = input('Enter a Alphabet:')
ascii_values = {character: ord(character) for character  in character}
print("The ASCII value of alphabet'" + character+ "' is", ascii_values)




