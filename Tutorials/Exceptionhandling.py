# in Java we do handle Exception by using try/catch block, in the same way try,except block with finally block

a=12
b=6

try:
    output=a/b
    print(output)
except ZeroDivisionError as e:
    print("Number cannot be division by Zero",e)
except ValueError as e:
    print("Please enter a valid number",e)
except Exception as e:
    print("Failed with Exception")
finally:
    print("executed finally block")
