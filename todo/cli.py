from functions import *
todo = []

while True:
    prompt = input('Type add, edit, show or exit to edit your to-do list. \n')
    todo = gettodo()
    
    
    if prompt.startswith('add'):
        todo.append (prompt[4:] + '\n')
        writetodo(todo)
    elif 'edit' in prompt:
        try:
            n = int(input('Enter the number of to-do you wish to edit: '))
            todo[n-1] = input('Enter new to-do: ') + '\n'
            writetodo(todo)
        except ValueError:
            print('Your command is not valid. Try Again\n')
            continue
    elif 'show' in prompt:
        todo = gettodo('file.txt')
        newtodo = [i.strip('\n') for i in todo]
        for n,i in enumerate(newtodo):
            print(f'{n+1} : {i}')
    elif 'complete' in prompt:
        try:
            r = int(input('Number of the task you completed: \n'))
            print (f'{r} : {todo[r]} has been removed from your to-do list.')
            todo.remove(todo[r])
            writetodo(todo)
        except:
            print ('There is no task with that number. Try again \n')
            continue

    elif 'exit' in prompt:
            break
    else: 
        print('Not a valid input. Try Again.')

print('Bye')