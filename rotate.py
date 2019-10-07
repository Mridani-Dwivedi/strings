#Write a function called rotate_word that takes a string and an integer as parameters, and returns a new string that contains the letters from the original string rotated by the given amount.
def rot1(lett,n):
  if lett.isupper():
    start=ord('A')
  elif lett.islower():
    start=ord('a')
  else:
    start=ord(lett)

  char_lett=ord(lett)
  diff= start+((char_lett-start)+n)%26
  return(chr(diff))
def rot(word,n):
  print(word)
  new=''
  for i in word:
      new=new+rot1(i,n)
    
  print(new)

rot('MeLoN',-10)