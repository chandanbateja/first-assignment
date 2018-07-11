Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # question 1

import time
import datetime
import threading

def threadd():
   time.sleep(5)
   print("Inside the function after 5 seconds")
      
threadd()


# question 2

import time
import datetime
import threading

def numbers():
   i=1
   for x in range(10):
      print(i)
      i+=1
      time.sleep(2)
      
numbers()



# question 3

import time
import datetime
import threading

l1 = [1,2,3,4,5]
def printl(l1):
   i = 2
   for x in l1:
      time.sleep(i)
      print("number: ",x)
      i+=2

printl(l1)



# question 4

import time
import datetime
import threading

class Factt(threading.Thread):
   def __init__(self,n):
      threading.Thread.__init__(self)
      self.n = n
      
   def run(self):
      fact = 1
      while(self.n>0):
         fact = fact*self.n
         time.sleep(1)
         self.n = self.n-1
      print("Factorial: ",fact)
      

thread1 = Factt(5)
thread1.start()

