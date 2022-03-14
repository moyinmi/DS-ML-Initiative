#Questi0n 1

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))  # intersection is a pre-defined function that brings together identical items in a set


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
identical_items = set()

for items_Set1 in set1: # iterates over elemnets in set 2   
    for items_Set2 in set2: #iterates over the set2 elements 
        if items_Set1 == items_Set2: # identifies the matching items in set1 and set2.
            identical_items.add(items_Set1)     # it adds the identical items into a new set       


print(identical_items)

#Question2 
'''Create a python program that can help a user print out email addresses with a specific hostname from a list of email addresses. (your function will accept two parameters; email list and the hosting address to be looked out for)'''



mail_list = ['joyfloyd2@hotmail.com', 'jb23forever@yahoo.com', 'adesade4@gmail.com', 'bimpeadeola@gmail.com', 'harunaik@yahoo.com', 'chikaoluchi@gmail.com', 'sweetheart4eva@hotmail.com', 'fionashrek@gmail.com', 'peace_goodness@hotmail.com', 'edmud@yahoo.com' ]


def mail_extractor(mail_list, host): # a function to extract the mails
  for name in mail_list: # iterates through the email list
    if host == name.split("@")[+1]: 
      print(name)
    else:
      continue
     
print(mail_extractor(mail_list,'yahoo.com'))
print(mail_extractor(mail_list,'hotmail.com'))
print(mail_extractor(mail_list,'gmail.com'))

#Question 3
'''Create a simple calculator that can add, subtract, multiply or divide depending upon the input from the user.
sample function:
calculator('multiply', 30, 2)     >>>output:  30 multiplied by 2 is 60
calculator(‘x’, 30, 2)      >>>output:  30 multiplied by 2 is 60
 '''

def Calc(Operator, num_1, num_2): # function that accepts the operator and input
    if Operator == "add" or Operator == "+" : # conditional statements to perform the operations
        ans = num_1 + num_2
        print("Answer: " + str(ans))

    elif Operator == "subtarct" or Operator == "-":
        ans = num_1 - num_2
        print("Answer: " + str(ans))
    
    elif Operator == "multiply" or Operator == "*":
        ans = num_1 * num_2
        print("Answer: " + str(ans))

    elif Operator == "divide" or Operator == "/":
        ans = num_1 / num_2
        print("Answer: " + str(ans))

    else :
        print("Multipy, Subtract, divide, add numbers only") # prints this statement if user enters a wrong input
    

Calc('multiply', 30,2)
Calc("+", 30, 2)

#Question 4
'''
Create a function that counts the number of elements within a list that are greater than 30 and outputs a custom message with the count. The function should return the numbers that meet the condition.
Test list : [1, 4, 62, 78, 32, 23, 90, 24, 2, 34, 28, 18, 12, 64, 50, 11, -1, 0, 30]
'''

test_list = [1, 4, 62, 78, 32, 23, 90, 24, 2, 34, 28, 18, 12, 64, 50, 11, -1, 0, 30]
def count_num(): 
    count = 0 
    numbers = []

    for i in test_list:
        if i > 30:
            count += 1
            numbers.append(i)
    print(count)
    print(numbers)
    print("There are {} numbers greater than 30".format(count))
count_num()

#Question 5
'''Build a palindrome checker. Your function should accept user input of the word and then perform the palindrome test. Your function should return a custom message to inform the user of the status of their test.

		Test words:  ‘Madam’, ‘Tent’, ‘Racecar’'''

def palindrome_checker():

    string=input(("Enter a string:"))
    if(string==string[::-1]):
        print("The string is a palindrome")
    else:
        print("Not a palindrome")

palindrome_checker()

#Question 6
'''Build an app that can raise invoices for each customer that makes an order We have a store that sells scarfs in large quantities. They have different types of scarf'''
 

from datetime import date
today = date.today()

red_Scarfs = 500 
blue_Scarfs = 750 
white_Scarfs = 800 

def invoice():
    print("Insert the name of the customer")
    customer_Name = input()

    formated_Customer_Name = " ".join(customer_Name.split()).title() # It combines split() + join() to remove additional space from string. title();is used to convert the first character in each word to Uppercase and remaining characters to Lowercase in the string and returns a new string.

    print("How much Red scarfs do the customer needs")
    red_Scarf_Q = int(float(input()))

    print("How much Blue scarfs do the customer needs")
    blue_Scarf_Q = int(float(input()))

    print("How much White scarfs do the customer needs")
    white_Scarf_Q = int(float(input()))

    order_Price = (red_Scarfs * red_Scarf_Q) + (blue_Scarfs * blue_Scarf_Q) + (white_Scarfs * white_Scarf_Q)
    current_Date_Formated = today.strftime("%b " + "%d, " + "%Y")  #It formats today to get the name of the month, the day of the month and the current year
    
    print("Name: " + formated_Customer_Name + " \nRed scarf: " + str(red_Scarf_Q) + " \nBlue scarf: " + str(blue_Scarf_Q) + " \nWhite scarf: " + str(white_Scarf_Q) + " \nOrder price: ₦" + str(order_Price) + " \nDate ordered: " + current_Date_Formated)    # \n takes the string to a new line


invoice()

#Question 7
'''Write a function generate_colors which can generate any number of Hexa or RGB colors. The function should have two parameters: colour code type, number of colours to be generated'''
#i do not understand

#Question 8
'''Write a Python program that prints all the numbers from 0 to 20 except even numbers'''
counts = 0
odd_number = []
while counts != 21:
    if counts % 2 != 0:
        odd_number.append(counts)
    counts += 1
print(odd_number)

#Question 9
'''Write a function called fizz_buzz that takes a number. If the number is divisible by 3, it should return “Fizz”. If it is divisible by 5, it should return “Buzz”. If it is divisible by both 3 and 5, it should return “FizzBuzz”. Otherwise, it should return the same number.'''
def fizz_buzz():
    num = int(float(input(("Enter a number: "))))
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 ==0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    

fizz_buzz()

#Question 10
''''Write a function for checking the speed of drivers. This function should have one parameter: speed.'''
def check_speed(speed):
  limit = 70
  point = 0
  if speed <= limit:
    print("OK")
  elif speed >= limit:
    point = int((speed - limit)/5)
    print("points: {}".format(point))
  if point >= 12:
     print("License suspended")
check_speed(65)
check_speed(70)
check_speed(80)
check_speed(100)
check_speed(105)

#Question 11
'''Write a Python program to create Fibonacci series up to ‘n’ using Lambda.'''
def fibonacci(count):
   listA = [0, 1]

   any(map(lambda _:listA.append(sum(listA[-2:])),
         range(2, count)))

   return listA[:count]

print(fibonacci(8))

#Question 12
''' Write a Python class that has two methods get_String and print_String. '''
class python_class():
   def __init__(self):
       self.string = ""

   def get_String(self):
       self.string = input("Enter string: ")

   def print_String(self):
       print(self.string.upper())

p = python_class()
p.get_String()
p.print_String()

    
