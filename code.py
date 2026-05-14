import random
import json

def reader():
    try:
        with open('tasks.json','r') as f: # f is json file
            data = json.load(f) # f got converted from json to python object
            return [A(d['task'],d['duedate'],d['uniqueid'],d['done']) for d in data]
    except:
        return []

def save(tasks):
    data=[]
    for obj in tasks:
        data.append({
            "task":obj.task,
            "duedate":obj.duedate,
            "uniqueid":obj.uniqueid,
            "done":obj.done
        })
    with open("tasks.json",'w') as f:
        json.dump(data, f, indent=4) #write data in file f, indent means indentation for readability

def uniqueid(length):
    id=''
    characters='abcdefghijklmnopqrstuvwxyz1234567890'
    for i in range(0,length):
        id=id+random.choice(characters)
    return id

def display():
    print('All Tasks: -')
    for i,obj in enumerate(tasks):
        print(f"Index:{i} | Task:{obj.task} | Duedate:{obj.duedate} | {'Done' if obj.done else'Not Done'}")

class A:
    def __init__(self,task,duedate,uniqueid,done):
        self.task=task
        self.duedate=duedate
        self.uniqueid=uniqueid
        self.done=done        
tasks=[]
while True:
    tasks=reader()
    print("----------------------")
    print("1 - Create new Tasks")
    print("2 - View All Tasks")
    print("3 - Delete a Task")
    print("4 - Edit a Task")
    print("5 - Mark as Done/Undone")
    print("6 - Exit")
    inp=int(input("Choose Flow :"))
    print("----------------------")
    
    if inp==1:
        print("Creating new task")
        inptask=input("Enter Task :")
        inpduedate=input("Enter Due Date :")
        newobj=A(inptask,inpduedate,uniqueid(10),False)
        tasks.append(newobj)
        save(tasks)
    
    elif inp==2:
        display()
    
    elif inp==3:
        print("Deleting a Task")
        display()
        ind=int(input('Enter index of task to delete :'))
        if 0<=ind<len(tasks):
            tasks.pop(ind)
        else:
            print('Invalid index')
            continue
        save(tasks)
    
    elif inp==4:
        print('Editing a Task')
        display()
        ind=int(input('Enter index of task to edit :'))
        objtoedit={}
        if 0<=ind<len(tasks):
            objtoedit=tasks[ind]
        else:
            print('Invalid index')
            continue
        print(f'Object to edit Task:{objtoedit.task} | Duedate:{objtoedit.duedate}')
        newtask = input('Enter modified Task :')
        newduedate = input('Enter modified duedate :')
        if(newtask!=''):
            objtoedit.task=newtask
        if(newduedate!=''):
            objtoedit.duedate=newduedate
        tasks[ind]=objtoedit
        save(tasks)

    elif inp==5:
        print("Marking a task as done/undone")
        display()
        ind=int(input('Enter index of task to mark as done/undone :'))
        if 0<=ind<len(tasks):
            tasks[ind].done= not tasks[ind].done
        save(tasks)
    
    elif inp==6:
        break
    
    else:
        print("Invalid Choice")