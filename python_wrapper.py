
#usage
#  wrapper()
#   
#  filename : os.path.realpath(__file__) use it to get the path
#  functionname : 'class' , 'if', ...
#  linenumber : line to be edited

hints = {
        "def()":0,'def':0,
        'while()':1,'while': 1,
        'if()': 2,'if':2,
        'elif()':3,'elif':3,
        'else()':4,'else':4,
        'for()':5,'for':5,
        'class()':6,'class':6,
    }
usage = {
    0:"def name():",
    1:"while():",
    2:"if():",
    3:"elif():",
    4:"else():",
    5:"for():",
    6:"class Name:",
}


def wrapper(filename :str,functionname: str,linenumber:int):
    #filename = str(os.path.realpath(__file__))  #to get the current file path
    file = open(filename)                       # open it in 'read mode'

    #print(hints[functionname])

    lines = file.readlines()                   # stores all the lines in a list for future
    #print(lines[7])

    file = open(filename,'w')                  # open the file in 'write mode'

    for i in range(linenumber-1):              # rewritting
        file.write(lines[i])
    
    file.write(usage[hints[functionname]]+"\n")  #start editing from specified line

    for i in range(linenumber-1,len(lines)):     #using loop to complete editing
        file.write("    "+lines[i])
    
    print("##################################################")   # alert
    print("***** Wrapping Completed *******")

    exit()   #prevents users code from running
    
    
