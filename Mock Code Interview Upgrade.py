import re
#dictionary to convert our letters to numbers based off of the phonepad
lettersToNumbers = {'a': 2,'b': 2,'c': 2,'d' : 3 ,'e' : 3,'f' : 3,'g' : 4,'h' : 4,'i': 4,'j' : 5,'k' : 5,'l' : 5,'m' : 6,'n' : 6,'o' : 6,'p' : 7,'q' : 7,'r' : 7,'s' : 7,'t' : 8,'u' : 8,'v' : 8,'w' : 9,'y' : 9,'x' : 9,'z' : 9}

#using our dict to convert each word to numbers then adds them to a list in line 20 'wordsAsNumbers'
def ConverToNumbersFromLetters(list):
  numbers = ''
  for items in range(len(list)):
    numbers = numbers + str(lettersToNumbers[list[items]])
  return numbers

phoneNumber = '3662277815781519518916891'
words = ['foo','bar','baz','foobar', 'emo', 'cap', 'car', 'cat']
wordsAsNumbers = []
wordsInPhoneNumber = []

#this is the solver of the problem, this takes the numbers in the list and pattern matches it using
#re.findall in line 22
for word in range(len(words)):
  wordsAsNumbers.append(ConverToNumbersFromLetters(list(words[word])))
for items in range(len(wordsAsNumbers)):
  if len(re.findall(wordsAsNumbers[items], phoneNumber)) >= 1:
    wordsInPhoneNumber.append(words[items])
#then we print our answer which lies in the var wordsInPhoneNumber
print(wordsInPhoneNumber)