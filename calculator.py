def calculator():
    print("welcome to the calculator!")
    num1 = float(input("enter the first number:"))
    num2 = float(input("enter second number:"))
      print("select operation:")
        print("1 addition:")
        print("2 subtraction:")
        print("multiplication:")
        print("division:")
    operation =input("enter operation choice(1-4):")

    result = 0

    if operation =="1":
         result =num1 + num2
    elif operation =="2":
         result =num1 - num2
    elif operation =="3":
         result =num1 * num2
    elif operation =="4":
         result =num1 / num2
     else:
         peint("error: division by zero!")
       return
  else: 
    print("invalid operation choice!
          return")
  print("result":,result)