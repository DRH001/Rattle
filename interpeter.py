# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 08:48:37 2020

@author: Daniel
@version: 0.1.0
"""







def parse(code):
    
    global main
    global functions
    global repeat
    global outputAtEnd
    global topOfStack
    global storage
    global pointer
    global loopCounter
    #global loopStart
    global currentCommandIndex
    global loopEnd
    global commands
    global loopList
    global commandsCopy
    global storedArray
    global secondArg
    global argFlag
    
    currentCommandIndex = 0
    #loopStart = 0
    #loopCounter = 0
    pointer = 0
    storage = [0] * 100
    topOfStack = 0
    loopList = []
    storedArray = []
    secondArg = None
    argFlag = False
    
    
    outputAtEnd = True
    commandsCopy = None

    #don't handle errors for now
    
    
    
    '''
    input|main;function1;function2......functionN; [then add arguments here which are stored to a local storage with max of 100 values] <-- NOT pushed to stack, separated by ,
    if | is the first character, input is taken through input(). If there is a "|", then whatever comes before it is pushed to stack. Otherwise, no input
    
    if the first character in main is a number, then the main method will be repeated that many times (i.e 1main will run twice) -> special case, 0 -> repeats 10 additional times (for 11 times total)
    
    '''

    pieces = code.split(";")

    main = pieces[0]
    
    
    if("|" in main):
        
        if(main.split("|")[0] == ""):
            topOfStack = input()
          
        else:
            topOfStack = main.split("|")[0]
            
        main = main.split("|")[1]    
    else:
        outputAtEnd = False
        
    try:#auto-parses the input as what it should be
        exec("a = " + topOfStack)
        topOfStack = locals()["a"]
        
        
    except:
        pass    



    functions = pieces[1::]


        
    try:
        repeat = int(main[0])
        main = main[1::]
        if(repeat == 0):
            repeat = 10
        repeat = repeat + 1
    except:
        repeat = 1
        
    commands = getCommandList(main,repeat)    
    commandsCopy = getCommandList(main, repeat)
        
    #print(topOfStack, main, functions, repeat, commands)
    
    
    #run commands.......
    
    #for command in commands: #swap commented lines later
        #try:
        #    runCommand(command)
        #except:
        #    pass
        #runCommand(command)
        
        
    while(currentCommandIndex < len(commands)):
        runCommand(commands[currentCommandIndex])
        currentCommandIndex += 1
        
  
    
    #check for end flags: no output, output last character, etc
    
    if(outputAtEnd):
        print(topOfStack)





def getCommandList(f,rep):
    
    possibleArgs = "0123456789~`@&^"# & represents a spacer in case some functions need lots of arguments
    tempList = []
    
    last = ""
    
    for i in range(len(f)):
        if(not(f[i] in possibleArgs)):
            tempList.append(f[i])
            last = f[i]
        else:
            tempList[-1] = last + f[i]
            last = tempList[-1]
            
    return(tempList * rep)        
    
    
    
    
def runCommand(c):
    global storage
    global pointer
    global argFlag
    
    func = c[0]
    
    arg = c[1::]
    
    if("^" in arg):
        arg.remove("^")
        argFlag = True
    else:
        argFlag = False
    
    if(arg != ""):
        try:
            arg = int(float(arg))
        except:
            pass
    
    if(arg == ""):
        arg = None
        
    if(arg == "~"):
        arg = int(storage[pointer])    
        
    if(arg == "`"):
        arg = int(topOfStack)
    
    if(arg == "@"):
        arg = int(pointer)  
        
    if("&" in str(arg)):#changes arg to a list
        arg = arg.split("&")
        for i in range(len(arg)):
            arg[i] = int(arg[i])
        print(arg)    
 

    
    
    functionDict = {
            "+":add,
            "-":subtract,
            "*":multiply,
            "/":divide,
            "w":helloWorld,
            "R":reformat, #arg 000000... where the first digit is type (1=int, 2=string, 3=float) - see below for details about remaining digits
            "s":store,
            "g":get,
            "<":pointerDown,
            ">":pointerUp,
            "P":setPointer,
            "p":prnt,
            "!":flag,
            "c":concat,
            "[":startLoop,
            "]":endLoop,
            "%":modulo,
            "$":swap,
            "r":secondArgument,
            "=":topOfStackEquals,
            "_":pointedValueInStorageEquals,
            "t":stringFunction,
            ",":printCharAt,
            "a":arrayInitFunctions,
            "A":arrayOperations,#array operations (maybe for matrices too)
            "m":matrixInitFunctions
            
            }
    
    #exec(functionDict(func) + "(" +str(arg)+")")
    (functionDict[func])(arg)
    
def reformat(arg):
    fmt = str(arg)
    #first digit is type, next is arg
    #for int, arg is sig digs #except zero case
    #for float, arg is digits after decimal (rounded) #except zero case
    #for string, arg is no. of characters trimmed from each end
    
    if(len(fmt) == 1):
        fmt += "0"
    
    if(fmt[0] == "1"):
        mint(int(fmt[1::]))
    elif(fmt[0] == "2"):
        mstr(int(fmt[1::]))
    elif(fmt[0] == "3"):
        mfloat(int(fmt[1::]))
    
    
def mint(sigdigs=0):
    global topOfStack
    if(sigdigs == 0):
        topOfStack = int(float(topOfStack)) 
        return
    else:
        from math import log
        b = int(log(float(topOfStack),10))
        topOfStack = int(float(topOfStack)/10**(b+1-sigdigs)) *10**(b+1-sigdigs)
 
def mstr(arg=0):
    global topOfStack
    if(arg == 0):
        topOfStack = str(topOfStack) 
    else:
        topOfStack = topOfStack[arg:(-arg+1)]
    
def mfloat(sigdigs=0):
    global topOfStack
    if(sigdigs == 0):
        topOfStack = float(topOfStack)   
    else:
        topOfStack = round(float(topOfStack), sigdigs)
    
    
    
    
    
    
def helloWorld(arg):#hello, world#fix this
    print("Hello, World!"*(arg+1))    
    
    
def add(arg):#add arg to stack
    global topOfStack
    mfloat()
    if(arg==None):
        topOfStack += 1
        return
    topOfStack += arg

    
def subtract(arg):#subtract arg from stack
    global topOfStack
    mfloat()
    if(arg==None):
        topOfStack -= 1
        return
    topOfStack -= arg  
    
    
def divide(arg):#divide stack/arg
    global topOfStack
    mfloat()
    if(arg==None):
        topOfStack /= 2
        return
    if(arg == 0):
        topOfStack /= 10
        return
    topOfStack /= arg    
    
def multiply(arg):#stack*=arg
    global topOfStack
    mfloat()
    if(arg==None):
        topOfStack *= 2
        return
    if(arg == 0):
        topOfStack *= 10
        return
    topOfStack *= arg  
     
    
def store(arg):#if the arg is None, it should instead use the current pointer
    global storage
    global topOfStack
    if(arg != None):
        storage[arg] = topOfStack
    else:
        storage[pointer] = topOfStack

def get(arg):
    global storage
    global topOfStack
    if(arg != None):
        topOfStack = storage[arg]
    else:
        topOfStack = storage[pointer]
    
def pointerUp(arg):
    global pointer
    if(arg == None):
        if(pointer != 99):
            pointer += 1
        else:
            pointer = 0
    else:
        for i in range(arg):
            if(pointer != 99):
                pointer += 1
            else:
                pointer = 0
            
            
def pointerDown(arg):
    global pointer
    if(arg == None):
        if(pointer != 0):
            pointer -= 1
        else:
            pointer = 99
    else: 
        if(pointer != 0):
            pointer -= 1
        else:
            pointer = 99

            
def setPointer(arg):
    global pointer
    pointer = int(arg)            
            
            
def prnt(arg):
    global topOfStack
    if(arg == None):
        print(topOfStack)
    elif(arg == 0):
        mint()
        print(chr(topOfStack))
    else:
        pass
        #what to make it do?
        
def flag(arg):
    global outputAtEnd
    if(arg==None):
        outputAtEnd = False
        
        
def concat(arg):
    global storage
    global topOfStack
    topOfStack = str(topOfStack) + str(storage[arg])   


def startLoop(arg):#unfinished
    #global loopStart
    global currentCommandIndex
    global storage
    global loopList
    global commands
    global currentCommandIndex
    #loopStart = currentCommandIndex
    loopList.append(currentCommandIndex)###
    if(arg == None): #case where the other bracket has an argument
        pass
    else:
        if(not(arg == topOfStack)):
            #skip until the closing bracket
            while(commands[currentCommandIndex][0] != "]"):
                currentCommandIndex += 1
        
        #if statement..... based on stuff in storage
        pass
    
def endLoop(arg):#unfinished?
    #global loopStart
    global loopEnd
    global currentCommandIndex
    global commands
    global commandsCopy
    global pointer
    global storage
    global topOfStack
   
    #print("test ", commands[currentCommandIndex])
    #print("test ", loopList, commands[currentCommandIndex])
    #print(commands)
    

    
    if("`" in commands[currentCommandIndex]):
        commands[currentCommandIndex] = commands[currentCommandIndex].replace("`", str(int(topOfStack) + 1))
    elif("~" in commands[currentCommandIndex]):
        commands[currentCommandIndex] = commands[currentCommandIndex].replace("~", str(int(storage[pointer])))
    elif("@" in commands[currentCommandIndex]):
        commands[currentCommandIndex] = commands[currentCommandIndex].replace("@", str(int(pointer)))    
    
    if(arg == None): #case where the other bracket has arg (i.e. if statement)
        pass
    elif(arg == 1):
        
        commands[currentCommandIndex] = commandsCopy[currentCommandIndex]
        #print(commands)
        del loopList[-1]
        #commands = commandsCopy##
        
        #print("here")
        #return
        #commands.pop(currentCommandIndex)
    else:
        #print(commands[currentCommandIndex][0] + str(int(commands[currentCommandIndex][1::])))
        commands[currentCommandIndex] = commands[currentCommandIndex][0] + str(int(commands[currentCommandIndex][1::]) -1)
        #currentCommandIndex = loopStart##
        currentCommandIndex = loopList[-1]##
        
    #print("test ",loopList,  commands[currentCommandIndex], "\n")   
                
    
def modulo(arg):
    global topOfStack
    mfloat()
    if(arg == None):
        topOfStack = topOfStack % 2
    elif(arg == 0):
        topOfStack = topOfStack % 10
    elif(arg == 1):
        topOfStack = topOfStack % 100
    else:
        topOfStack = topOfStack % arg
    
    
    
    
def swap(arg):   
    global topOfStack
    global pointer
    global storage
    if(arg == None):
        tempSwap = storage[pointer]
        storage[pointer] = topOfStack
        topOfStack = tempSwap
    else:
        tempSwap = storage[arg]
        storage[arg] = topOfStack
        topOfStack = tempSwap
        
        
def secondArgument(arg):
    global secondArg
    secondArg = arg        
    

def topOfStackEquals(arg):
    global topOfStack
    if(arg == None):
        topOfStack = 0 
        return
    topOfStack = arg    
    
def pointedValueInStorageEquals(arg):
    global storage
    global pointer 
    if(arg == None):
        storage[pointer] = 0
        return
    storage[pointer] = arg
    
def stringFunction(arg):
    pass#define string functions here: flip/reverse, bin/hex (or make new fns for these), decompress (e.g. 126 bit compression), caesar shift


def printCharAt(arg):
    global topOfStack
    global storage
    global pointer
    if(arg == None):
        print(chr(int(topOfStack)))
        return
    print(chr(int(storage[pointer])))
    
    
def arrayInitFunctions(arg):
    # a1 stores array of zeroes of length topOfStack at the pointer
    # a1_ pushes an array of the bottom arg to stack
    # a2 pushes an array of alternating ones and zeroes - secondarg is none, it starts at 1. secondarg is 0, it starts at 0. Else, it gives an array of secondArray's value and zeroes that alternate, starting with non-zero
    # to add: range, linspace, 
    global topOfStack
    global storedArray
    global storage
    global pointer
    global secondArg
    
   
    bottomArg = None
    topArg = int(str(arg)[0])
    try:
        bottomArg = int(str(arg)[1::])
    except:
        pass
    
    #print(topArg, bottomArg)
    
    if(topArg == 1):
        mint()
        if(bottomArg == None):
            storage[pointer] = [0] * topOfStack
            return
        
        topOfStack = [bottomArg] * topOfStack

    if(topArg == 2):
        #might need 2nd arg
        if(secondArg == None):
            tempSwitch = 1
            tempArray = []
            for i in range(bottomArg):
                tempArray.append(tempSwitch)
                if(tempSwitch):
                    tempSwitch = 0
                else:
                    tempSwitch = 1
            topOfStack = tempArray

        elif(secondArg == 0):
            tempSwitch = 0
            tempArray = []
            for i in range(bottomArg):
                tempArray.append(tempSwitch)
                if(tempSwitch):
                    tempSwitch = 0
                else:
                    tempSwitch = 1
            topOfStack = tempArray
            
        else:
            tempSwitch = secondArg
            tempArray = []
            for i in range(bottomArg):
                tempArray.append(tempSwitch)
                if(tempSwitch):
                    tempSwitch = 0
                else:
                    tempSwitch = secondArg
            topOfStack = tempArray
        



def arrayOperations(arg):
    #might use second arg
    #cycle, shift, reverse, +-*/%, RREF, linearly independant, max/min, max/min per each column/row, average/mode,
    
    global topOfStack
    global secondArg
    
    if(arg == None):
        #reverse array
        pass
    
    if(len(arg) == 1):
        if(arg==None):
            pass
    
    
    
    pass

    
    
    
            
            
def matrixInitFunctions(arg):
    #uses the second argument!!!!!
    global secondArg
    global topOfStack
    
                
            
    
    
        
    

