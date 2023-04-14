# 1.1 What does SDLC stand for?
Software development lifecycle

# 1.2 What exception is thrown when you divide a number by 0?
ZeroDivision Error

# 1.3 What is the git command that moves code from the local repository to the remote repository? 
git push --all

# 1.4 What does NULL represent in a database?
It represents the absence of a value in a column, an instance where the data is non-existent.

# 1.5 Name 2 responsibilities of the Scrum Master
-	Organising and leading scrum stand-ups everyday
-	Managing the scrum board, ensuring it is accurate, up to date, and that everyone has the correct tasks

# 1.6 Name 2 debugging methods, and when you would use them.
-	You can use the inbuilt debugging functionality in Pycharm, identified by the green bug symbol to the right of the 
Run button. This can be used when debugging within Pycharm, or other ‘smart’ IDEs.
-	pdb, which is a Python library, and can be used in any IDE. This allows you to step through your code, 
line-by-line, in order to investigate exactly how it works, beginning wherever you choose, either using the syntax:
breakpoint()

or 

import pdb
pdb.set_trace()

# 1.7 Looking at the following code, describe a case where this function would throw an error when called. Describe 
# this case and talk about what exception handling you’ll need. 
This case would throw TypeError if one of the variables was in string format, as the operator ‘>=’ cannot work 
between string and integers. If someone put the price or cash as ‘£3’ or  ‘3’ or  ‘three’, this would raise the error. 
To handle this error, you could use this syntax:

def can_pay(price, cash_given):
    try:
       if cash_given >= price:
           return True
       else:
           return False
    except TypeError:
        print('Please input an integer rather than a string')
        exit()

This is not only a better experience for the user, it also prints ‘Please input an integer rather than a string’, 
which directs the user to correct their input, and therefore be able to use the program. 
You could also create a custom error. This could be done using this syntax:

class StringInputIncompatibleError(Exception):
    pass

# 1.8 What is git branching? Explain how it is used in Git. 
A branch of a repository is a different version of the original repository. It allows for alterations to be made to 
code, without losing the original. This improves collaborative work, allowing different people to work on the same code 
at the same time (using pull requests), as well as ensuring that code is not lost, or altered irretrievably. Branches 
can then be ‘merged’, recombining them with the original, or with another branch that someone has been working on. In 
the terminal, you can create a new branch (git branch <new branch name>), create a new branch and switch to it (git 
switch -c <new branch name>) or just easily switch between branches (git switch <branch name>). To check which branch 
you are working on, you can simply type ‘git branch’, and the name of the branch you are currently on will be printed.

# 1.9 Design a restaurant ordering system.
I took the question to mean creating a system for taking restaurant orders within a restaurant, via QR codes on the 
tables, with the option for delivery.

a) Key requirements:
- menu – items and prices
- table numbers and table capacities
- server id numbers 
- delivery option 
- menu online – on a QR code, payment through QR code
- link between servers and kitchen – for orders

b) Main considerations and problems:
-	menu and prices need to be updateable/accessible in case they are sold out/prices change – daily specials?
-	When ordering through QR code, do they need to give table numbers? Or email address? 
- what is maximum capacity of the restaurant?
  o	in terms of tables
  o	in terms of how much the kitchen can produce (relevant for takeaway)
- delivery considerations:

  o	is there any food that can’t be delivery e.g. is there a different delivery menu. How is it differentiated from 
the in-house menu when kitchen receives orders?

o	How to take the deliveries – online? By phone? By app?
  
o	Are they linked with food delivery apps e.g. Deliveroo
  
o	Is there a cut-off on deliveries (e.g. freeze orders, take offline) if the restaurant is full – relevant to 
maximum capacity of how much the kitchen can produce
  
o	Delivery fee standard, or dependent on how busy the restaurant is e.g. surge prices
-	Which tables to be served first – depending on what has been ordered, how long it will take to make, how long 
they have been waiting?
-	How secure is the online/QR payment system? Do they need to create an account to pay?
-	How are tips on the bill divided – built into prices? Or shared equally among staff? Or specific to the server?

c) What components or tools would you use?
-	QR codes on tables to order
-	Connecting to apps – for delivery/takeaway
-	Peak times – meal times
-	Privacy for takeaway/delivery (e.g. personal information, address etc.) and payments (security)
