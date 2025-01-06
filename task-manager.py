#Initial tasks list
tasks = []
descriptions = {}

#Auxiliary functions
def displayTasks(all_tasks):
    print('\nYour tasks: ')

    if len(all_tasks) <= 0:
        print('\nNo tasks')
    else: 
        for index, task in enumerate(all_tasks):
            print(f'{index+1}: {task}')

def newOperation(all_tasks):
    operation = input("Press 'A' add a new task, 'E' to edit a task, 'R' to remove a task or 'F' to quit the application: ")
    
    if operation == 'A':
        addTask(all_tasks)
    elif operation == 'E':
        editTask(all_tasks)
    elif operation == 'R':
        removeTask(all_tasks)
    elif operation == 'F':
        return
    else: 
        newOperation(all_tasks)

def validTaskNumber(all_tasks, operation):
    task_number = input(f'Enter the number of the task you want to {operation}: ')

    valid = False
    while not valid:
        try:
            number = int(task_number)
            valid = True
        except:
            task_number = input('Please provide a valid task number: ')
    
    if not (0 < task_number < len(all_tasks)):
        print('Task not found !')
        validTaskNumber(all_tasks, operation)
    else:
        return number

#Operations
def addDescription(task, descriptions):
    description = input('Add a description: ')
    descriptions [task] = description

    return descriptions

def editTask(all_tasks):
    task_number = validTaskNumber(all_tasks, 'edit')

    new_task = input('Edit task: ')
    all_tasks[task_number-1] = new_task

    print(f'Item {task_number} edited!')

    displayTasks(all_tasks)
    newOperation(all_tasks)

def removeTask(all_tasks):
    task_number = validTaskNumber(all_tasks, 'remove')

    all_tasks.remove(all_tasks[task_number-1])

    print(f'\nItem {task_number} removed!')   

    displayTasks(all_tasks)    
    newOperation(all_tasks) 

def addTask(all_tasks):
    new_task = input('Add a task: ')
    all_tasks.append(new_task)

    displayTasks(all_tasks)

    newOperation(all_tasks)    

#Start application
addTask(tasks)