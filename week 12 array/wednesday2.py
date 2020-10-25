def countOfValueGreater(numbers):
    box=0
    result=0
    for value in numbers:
       if box==0:
         box=value
       else:
         if value>box:
            result=result+1  
         box=value
    return result
numbers=eval(input("Enter numbers:"))
print("result is : ",countOfValueGreater(numbers))
