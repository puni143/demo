class AgeError(Exception):
    pass

try:
    age=int(input("enter your age:"))
    if age < 18:
        raise AgeError("you are not eligible to vote")
    else:
        print("you are eligible to vote")


except AgeError as e:
    print("user defined exception caught:",e)


except ValueError:
    print("invalid input! please enter a number")
