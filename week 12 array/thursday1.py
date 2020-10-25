def countA(words):
    result=0
    for value in words:
        for n in range(len(value)):
            if value[n]=="a" or value[n]=="A":
               result=result+1
    return result
words=eval(input("enter word :"))
print("Total number of A is : ",countA(words))

    