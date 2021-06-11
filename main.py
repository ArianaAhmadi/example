two_list=input("Enter a string with spaces separating the words and numbers: ").split()#Prompt the user   
numbers = []
def finder(n):
  list1 = []
  global numbers
  for i in n:
    if i.isdigit() == True:
      numbers.append(i)
    else:
      list1.append(i)
  print("The words in the list are:", (', '.join(list1)))
  return (', '.join(numbers))
print("The numbers in the given list are:",finder(two_list))
print()

total_list=input("Enter a string of numbers and words seperated by spaces:\n").split() #asks the user to Enter a string of numbers and words seperated by spaces, then saves it in the variable total_list
num_list = [] # creates an empty list called num_list
def find_numbers(n):  #defines a function where it takes a list and splits it into a list of numbers and a list of words 
  word_list = [] # creates an empty list called word_list
  global num_list
  for i in n: # loops through all the objects in string n
    if i.isdigit() == True: # if the object in string n at position i is a number then
      num_list.append(i) # add the number at position i to the list num_list
    else: #if the value is not a number
      word_list.append(i) # add the word at position i to the list word_list
  print("The words in the list are:", (', '.join(word_list)))  #outputs the list of words
  return (', '.join(num_list))  #returns the list of numbers
print("The numbers in the given list are:",find_numbers(total_list))  #states the list of numbers
print()  #separate the two functions
'''
def list(n):
  a = []
  b = []
  if n.isdigit() == True:    #n.isdigit()
    n = input()
    a.append(n)
    print(a)
  elif n.isdigit == False:
    n = input()
    b.append(n)
    print(b)
  else: 
    print("What are you typing?")

n = [str(s) for s in input().split()]
print(list(n))
'''

''''
#Function 2
a = [int(s) for s in input().split()]
for elem in a:
  print(elem, end = ' ')

for i in list:
  if i.isdigit == True:
    print("Yes")

def count(list_1):
  list_1 = []
  list_2 = []
  for i in list_1:
    if i.isdigit() == True:
      list_1.append(i)
      return list_1

list_1 = [(s) for s in input().split()]
print(count(list_1))
'''
''''
import re 
a = input()

list_1 = " ".join(re.split("[^a-zA-Z]*", a))
list_2 = " ".join(re.split("[^0-9]*", a))

print(list_1)
print(list_2)
'''

''''
def first_list(n):
  import re
  if n == " ":
    return None
  else:
    return " ".join(re.split("[^a-zA-Z]*", n)
print(first_list(input()))
'''