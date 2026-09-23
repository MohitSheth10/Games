import random
bottom=int(input("Enter the start of the range:\n"))
while bottom<0:
  print("Enter a positive number: ")
  bottom=int(input("Enter the start of the range:\n"))
top=int(input("Enter end of the range:\n"))
while top<bottom:
  print("The end of the range must be bigger than the start.")
  top=int(input("Enter end of the range:\n"))
num2=random.randint(bottom,top)
num=0
while num!=num2:
  num=int(input("Enter a number: "))
  if num<num2:
    print("Try higher")
  elif num>num2:
    print("Try lower")
if num==num2:
  print("Excellent")
