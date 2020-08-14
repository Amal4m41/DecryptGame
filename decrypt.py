import random as r
import d_lib as dq


def pick():
  global s,l,l1
  l=r.choice(dq.lst_dq)
  l1=l.split('-')[0]
  l1=l1.split()
  #print(l1)

def reorder():
  count=c=0
  for i in l1:
    
    for k in i:
      if(k.isalpha()==0 and k.isspace()==0):
        i=i.replace(k,'')
    
    sol_lst.append(i)
    i=list(i)
    a=i.copy()
    if(ch2==1):
      n=3
    elif(	ch2==2):
      n=5
    else:
      n=6
    if(len(a)>n):
      b=a[:n]
      r.shuffle(b)
      a=b+a[n:]
    else:
      r.shuffle(a)
    for j in range(len(a)):
      if(a[j]==i[j]):
        count+=1 
      c+=1     
    lst_reord.append(''.join(a))
    
  return count,c

def display(c1,c2):
  print()
  print(' '.join(lst_reord))
  print("                                                                                                     -",l.split('-')[1])
  print(str((c1/c2)*100)[:4]+'% of the text is identical to the original')  
  
def check():
  ans=input("Enter your answer : ")
  p=ans.split()
  ans_lst=[]
  for i in p:
    for j in i:
      if(j.isalpha()==0 and j.isspace()==0):
        i=i.replace(j,'')
    ans_lst.append(i)
    while('' in ans_lst):
      ans_lst.remove('')
  #print(sol_lst,ans_lst)
  if(len(sol_lst)!=len(ans_lst)):
    status=0
  else:
    for i in range(len(sol_lst)):
      #print(sol_lst[i].lower(),ans_lst[i].lower())
      if(sol_lst[i].lower()!=ans_lst[i].lower()):
        status=0
        break
    else:
      status=1

  return status 

while(1):
  l=s=''
  ans_lst=[]
  sol_lst=[]
  l1=[];lst_reord=[]
  lst=[]

  print(
'''                                                       DECRYPT 
   ********************************************************MENU**************************************************************
                                                        1-Info
                                                        2-Play game
                                                        3-Exit
''')
  ch=int(input("Enter the choice : "))
  if(ch==1):
    print('''
    Decrypt is a game of decryption. Your goal is to recover a text which is presented to you under a crypted form.
    And you can try several times, until you decode text (or until you abandon).
     
               For example : imTe si a vrire dan koobs aer aobts  --> Time is a river and books are boats.
            
    ''')

  elif(ch==2):
    ch2=int(input('''
Enter the difficulty level : 
  1-Easy
  2-Medium
  3-Hard 
'''))
    while(ch2 not in [1,2,3]):
      print("Entered invalid input! Please try again")
    
    pick()
    c1,c2=reorder()
    display(c1,c2)
    while(1):
      if(check()):
        print("Correct!")
        break
      else:
        print("Wrong!")
      ch3=input("Do you want to contine[Y/N] ?")
      if(ch3.lower()=='n'):
        print()
        print('Answer :'+l)
        print()
        break        
      display(c1,c2)

  elif(ch==3): 
    print("Thank you!")
    break

  else:
    print('Entered invalid choice! Please try again...')




