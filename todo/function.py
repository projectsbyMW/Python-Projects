FP = 'file.txt'

def gettodo (file_path = FP):
    with open(file_path,'r') as file:
        return file.readlines()
    
def writetodo(todo,file_path = FP):
    with open(file_path,'w') as file:
        file.writelines(todo)