import os
import pickle
def savecontacts():
  #f=open('contact.dat','bw')
  with open('contact.dat','bw')as f:
    pickle.dump(contacts,f)


contacts={}
class contact:
  def __init__(self,number,firstname,lastname,address):
    self.number=number
    self.firstname=firstname
    self.lastname=lastname
    self.address=address

def addcontact():
  os.system('cls')
  number=input("enter number")
  if number in contacts:
    input('this number is exits ,press enter to back menu')
  else:
    firstname=input('fn')
    lastname=input('ln')
    address=input('ad')
    contacts[number]=contact(number,firstname,lastname,address)
    input('contact created,press enter to back menu..')
    savecontacts()

def removecontact():
  os.system('cls')
  number=input("enter number")
  if number in contacts:
    del contacts[number]
    input('successful')
  else:
    input('not exist,press enter')
    savecontacts()

def updatecontact():
  os.system('cls')
  number=input("enter number")
  if number in contacts:
    firstname=input('fn('+contacts[number].firstname+'):')
    lstname=input('fn('+contacts[number].lstname+'):')
    address=input('fn('+contacts[number].address+'):')
    contacts[number].firstname=firstname
    contacts[number].lstname=lstname
    contacts[number].address=address
    input('successful')
    savecontacts()
  else:
    input('not exist,press enter')

def findcontact():
  os.system('cls')
  number=input("enter number")
  if number in contacts:
    contact=contacts[number]
    print("{0}:{1},{2},{3}:".format(contact.number,contact.firstname,contact.lastname,contact.address))
    input('back')
  else:
    input('not exits,press enter')

def listcontact():
  for i in contacts:
    contact=contacts[i]
    print("{0}:{1},{2},{3}:".format(contact.number,contact.firstname,contact.lastname,contact.address))
input('press enter')


def displaymenu():
  print('welcome')  
  print('-------')
  print('1.add')
  print('2.remove')
  print('3.update')
  print('4.find')
  print('5.list')
  print('6.exit')

if os.path.exists('contact.dat'):
  with open('contact.dat','br') as f:
    contacts=pickle.load(f)

while True:
  os.system('cls')
  displaymenu()
  print()
  option=input("select number")
  if option=='1':
    addcontact()
  elif option=='2':
    removecontact()
  elif option=='3':
    updatecontact()
  elif option=='4':
    findcontact()
  elif option=='5':
    listcontact()
  elif option=='6':
    break 
