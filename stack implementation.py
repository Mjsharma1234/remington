#stack development using list#
stk =[]                        # to check wheather the stack is empty or not
top =None
def isEmpty(stk):             
    if(stk==[]):
        return True
    else: 
        return False

def enqueue(stk,item):          #to add itmes in stack
    stk.append(item)
    if len(stk)==1:
        front=rear=0
    else:
        rear =len(stk)-1

def dequeue(stk):             #to delete items from stack
    if(isEmpty(stk)):
        return ('underflow')
    else:
        item=stk.dequeue(0)
    if len(stk)==0:
        front =rear =None 
        return item
       

def peek(stk):             # to chech the values stored in the stack
    if(isEmpty(stk)):
            return('underflow')
    else:
        front=0
    return stk[front]
       

#display the itmes that are in the stack

def display(stk): 
    if isEmpty(stk):
        print("empty stack")
    elif len(stk)==1:
        print(stk[0],"<==front,rear")
    else:
        front = 0
        rear = len(stk)-1
        print(stk[front],"<-front")
        for a in range(1,rear):
            print(stk[a])
        print(stk[rear],"<-rear")

    


# main code #
stk=[]
front=None

while True:

    print('Stack Implementation:')
    print('1.enqueue')
    print('2.dequeue')
    print('3.Peek')
    print('4.Display')
    print('5.Exit')
    ch=int(input('Enter your choices(1-5):'))
    if(ch==1):
        item=int(input('enter the items'))
        enqueue(stk,item)
        print('%d added succesfully'%item)
        input('press any key to continue:')

    elif(ch==2):
        item=dequeue(stk)
        if(item=='underflow'):
            print('underflow! Stack is Empty!')
        else:
            print('%d is popped' %item)
        input('press any key to continue...')

    elif(ch==3):
        item=peek(stk)
        if(item=='underflow'):
            print(' Stack is Empty!')
        else:
            print('%d is at the top' %item)
            input('press any key to continue...')
    elif(ch==4):
        display(stk)
        input('Press any key to continue...')

    elif(ch==5):
        break
    else:
        print(' abe Andhe 1-5 tak dalna tha')
        print('bilkul besharam ho kya ')
        print('agar class UKG dhang se padhi hoti toh ye n dekhna padta')
        print("chlo ab besharmo ki tarah dba do 1-5 tak kuch bhi ")
        print("agli baar yaad rakhio aur zayada neta mat banio ")
        print('press any key to continue')
        print('or else just fuck off')


        

   
 









