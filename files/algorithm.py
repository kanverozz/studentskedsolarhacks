import random
print("How many extracurricular activities do you do?")
r=int(input())
a=r
f=0
activ={}
list=[1,2,3,4,5,6,7]
while a != 0:
  f=0
  print("Please enter the name and details of the activities")
  print("Name:")
  m=input()
  print("Length in Hours:")
  l=(input())
  print("Time Start:")
  ts=input()
  print("Time End:")
  te=input()
  while f==0:
      print("Day of Week:")
      print(  "[1]Sunday")
      print( "[2]Monday")
      print(  "[3]Tuesday")
      print(  "[4]Wednesday")
      print(  "[5]Thursday")
      print(   "[6]Friday")
      print(   "[7]Saturday")
      p=int(input())
      if p==1:
          list.append(1)
          list.remove(1)
          dow="Sunday"
      elif p==2:
          list.append(2)
          list.remove(2)
          dow="Monday"
      elif p==3:
          list.append(3)
          list.remove(3)
          dow="Tuesday"
      elif p==4:
          list.append(4)
          list.remove(4)
          dow="Wednesday"
      elif p==5:
          list.append(5)
          list.remove(5)
          dow="Thursday"
      elif p==6:
          list.append(6)
          list.remove(6)
          dow="Friday"
      elif p==7:
          list.append(7)
          list.remove(7)
          dow="Saturday"
      print("Does this activity occur on another day?")
      if input()== "Yes":
          f=0
      else:
          f+=1

  activ[m]=[l,ts,te,p]
  a-=1
p=random.choice(list)
if p==1:
    dow="Sunday"
elif p==2:
    dow="Monday"
elif p==3:
    dow="Tuesday"
elif p==4:
    dow="Wednesday"
elif p==5:
    dow="Thursday"
elif p==6:
    dow="Friday"
elif p==7:
    dow="Saturday"
print("On a scale of 1-10, How ready are you for the test? Please be honest.")
readiness=int(input())
if readiness < 6:
    print("You definitely need to study, get on it!")
    print("A good time to study may be on",dow,"for 2 - 3 hours")
elif readiness >= 6 and readiness < 9:
    p=random.choice(list)
    print("Great! You may want to review material a few more times to ensure a great score.")
    print("A good time to study may be on",dow,"for 30 min to 1.5 hr")
elif readiness >= 9 and readiness <=10:
    print("Amazing! You could review a little if wanted. A good time may be at",dow,"for 15 to 20 min")
