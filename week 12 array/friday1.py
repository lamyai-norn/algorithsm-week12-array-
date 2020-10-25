def orderWords(words):
  orderOfWords=""
  for value in indexOfWords:
    for n in range(len(words)):
        result=words[n]
        if n==value:
            orderOfWords=orderOfWords+result+" "
  return orderOfWords
words=eval(input("Enter words : "))
indexOfWords=eval(input("Enter the order of words:"))
print(orderWords(words))