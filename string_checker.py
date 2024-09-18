class StringCheck:
  def __init__(self, word) -> bool:
    self.word = word
  # functions 
  def alphaNumcheck(self):
    if self.word.isalnum():
      return True
    else:
      return False
    
  def alphaCheck(self):
    if self.word.isalpha():
      return True
    else:
      return False

test1 = StringCheck("ejid0")
print(test1.alphaNumcheck())

print(test1.alphaCheck())
