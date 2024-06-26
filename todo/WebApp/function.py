import os 

if not os.path.exists("file.txt"):
     with open("file.txt","w") as file:
          pass

FP = 'file.txt'

def gettodo (file_path = FP):
    with open(file_path,'r') as file:
        return file.readlines()
    
def writetodo(todo,file_path = FP):
    with open(file_path,'w') as file:
        file.writelines(todo)