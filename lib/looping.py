#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
  i = 10
  while i >= 1 :
    print (i)
    i -= 1
  print ("Happy New Year!")   

def square_integers(int_list):
    # code goes here!
   
  squaredNumbers = [int ** 2 for int in int_list]
  return squaredNumbers    

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    
