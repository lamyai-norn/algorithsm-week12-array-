def numberOfSevens(numbers):
    result=0
    for value in numbers:
      if value==7:
        result=result+1
    return result
numbers=eval(input("Enter value:"))
print("result is : ",numberOfSevens(numbers))
