"""
create a numeric variable, if it is between 0 and 10 show a message indicating
it and do the same with 11 and 20 and 21 and 30
"""
num = float(input("Type a number: "))

if -1<num<11:
    print("Is between 0 and 10")
elif 10<num<21:
    print("Is between 11 and 20")
elif 20<num<31:
    print("Is between 21 and 30")
