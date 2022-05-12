"""
Make a program allows you to enter a student's name and notes
corresponding to 3 notes with equal weighting. Print the student's name and
grade average.
"""
name = str(input("Write your name:"))
c1 = float(input("type the first rating:"))
c2 = float(input("type the second rating:"))
c3 = float(input("type the third rating:"))
g_average = (c1 + c2 + c3)/3

print(f"Your name is '{name}' and you grade average is '{g_average:.1f}'")