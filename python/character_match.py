# Don't forget to run your tests!

def is_character_match(string1, string2):
	if len(string1) != len(string2):
      return False
    
  char_counts = {}
  
  lower1 = string1.lower()
  lower2 = string2.lower()
  
  for char in lower1:
    char_counts[char] = char_counts.get(char, 0) + 1
    
  for char in lower2:
    if not char_counts.get(char):
      return False
    
    char_counts[char] -= 1
  
  return True
