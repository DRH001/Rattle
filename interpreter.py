# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 08:48:37 2020

@author: Daniel
@version: 1.1.1

Updated 2021-02-24 20:00 EST
"""



"""
to do:
    
    debug function! 
    make concat use value at pointer if arg is blank (and take argflags to concat backwards)
    make loops get value of ~ before going inside loop!
    function to go from char to int and vice-versa
    
    
    make a function to automatically store an array in memory and move the pointer to the next value
    make else statements? or maybe just not statements? <-- which can act as else statements (make it use an argflag?)
"""


"""
quick programs:
    
    Fizz&Buzz|!I[g+R1bs%3[0b0b^0]g%5[0b1b^0]B]100 is FizzBuzz - alternatively:  Fizz&Buzz|!sSs1S1s2P3[g+R1bs%3[0b1b^0]g%5[0b2b^0]B]100
    w is hello world
    |[1=q]!-s+>s[g<%~[0=pq]g-s>]~=1p checks to see if input is prime https://codegolf.stackexchange.com/questions/57617/is-this-number-a-prime
    |[0q][p]0 does this: https://codegolf.stackexchange.com/questions/62732/implement-a-truth-machine
    | cat https://codegolf.stackexchange.com/questions/62230/simple-cat-program (note: |p is NOT a cat program, because the input gets parsed when main is not empty)
    B&b&uffalo& |I=[b0[2b^b1]b2b3b1b2[3q]b3+]4 does this: https://codegolf.stackexchange.com/questions/218284/output-buffalo-buffalo-buffalo-buffalo-buffalo-buffalo-buffalo-buffalo
    |IP0[gpP~]0 does this: https://codegolf.stackexchange.com/a/218879/95671
    i+R`c0c0$[+i]~ does this: https://codegolf.stackexchange.com/a/219748/95671
    
    
    better prime number checker: |f0;[1=f]-s+>s[g<%~[0=f]g-s>]~=1 <- better because you can actually add code after f0
    
    
    
    
    
    
    |s>s[0+q][g-s<*~s>]~ or |I2<[0+q][g-s<*~s>]~   ->  factorial (old:   |s>-s[0+q][<*~s>g-s]~<g     )


"""

"""
For input:
    input must come before the | (might not have any |'s)
    if you want multiple inputs, use an & as a separator (it will automatically create an array and parse what type everything should be)
    if you want to concatenate hard-coded input with user input (or just take only some items as user input), use a \
        example: \&potato\&2\ hard-coded and yes&2, es, 4 as user inputs, will give ["yes", 2, "potatoes", 24]
    NOTE: there are no escape characters (e.g. \n) or quotation marks (",') that can be taken as input in any way unless you double them.
        ^if doubled, you can always trim a string by reformatting using R21 to get rid of the excess quotation marks <- e.g. ""test""|R21 --> "test"




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
    global printBuffer
    global argFlag2
    global functions
    global commands
    global currentCommandIndex
    global skipTo
    global endFunctionFlag
    global inFunction
    global functionCommandList
    global currentCommandIndexF
    global currentFunction
    global commandsCopyF
    global pieces
    global intoLoopArgs
    
    intoLoopArgs = []
    
    currentFunction = -1
    currentCommandIndexF = []
    functionCommandList = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #this is the limit for no. of fns
    commandsCopyF = functionCommandList
    
    inFunction = False
    
    endFunctionFlag = False
    
    skipTo = []
    
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
    argFlag2 = False
    printBuffer = []
    
    
    outputAtEnd = True
    commandsCopy = None

    #don't handle errors for now
    
    
    
    '''
    input|main;function1;function2......functionN; [then add arguments here which are stored to a local storage with max of 100 values] <-- NOT pushed to stack, separated by ,
    if | is the first character, input is taken through input(). If there is a "|", then whatever comes before it is pushed to stack. Otherwise, no input
    
    if the first character in main is a number, then the main method will be repeated that many times (i.e 1main will run twice) -> special case, 0 -> repeats 10 additional times (for 11 times total)
    
    '''

    #code = code.replace(" ","")
    pieces = code.split(";")

    main = pieces[0]
    
    
    if("|" in main):
        
        if(main.split("|")[0] == ""):
            topOfStack = input()
          
        else:
            topOfStack = main.split("|")[0]
            
        main = main.split("|")[1].replace(" ","").replace("\n","")
        if(main == ""):
            print(topOfStack)
            return
        
        for char in topOfStack:
            if(char == '\\'):
                topOfStack = topOfStack.replace("\\", input(),1)
                
    else:
        outputAtEnd = False


    


    temp1 = []#auto-parses the input as what it should be
    temp2 = None
    try:
        topOfStack = topOfStack.split("&")
        for elem in topOfStack:
            try:
                exec("a = " + str(elem))
                temp2 = locals()["a"]
            except:
                temp2 = elem
            temp1.append(temp2)
        topOfStack = temp1
        
        if(len(topOfStack) == 1):
            topOfStack = topOfStack[0]
    except:
        try:
            exec("a = " + str(topOfStack))
            topOfStack = locals()["a"]
        except:
            pass

    

    functions = pieces[1::]

    for i in range(len(functions)):
        functions[i] = functions[i].replace(" ","")

        
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
        
    from time import perf_counter as currentTime 
    start = currentTime()    
        
    
    while(currentCommandIndex < len(commands)):
        runCommand(commands[currentCommandIndex])
        currentCommandIndex += 1
        
        if(currentCommandIndex % 100 == 0):
            if(currentTime() > start + 5):
                print("Program timed out. Did you forget your exit condition?")
                break
        
  
    
    #check for end flags: no output, output last character, etc
    
    if(outputAtEnd):
        if(printBuffer != []):
            print("".join(printBuffer))
        else:    
            print(topOfStack)





def getCommandList(f,rep):
    
    possibleArgs = "0123456789~`@&^?."# & represents a spacer in case some functions need lots of arguments
    #^ and ? are argument flags
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
    global argFlag2
    
    func = c[0]
    
    arg = c[1::]
    
    if("^" in arg):
        arg = arg.replace("^","")
        argFlag = True
    else:
        argFlag = False
    
    if("?" in arg):
        arg = arg.replace("?","")
        argFlag2 = True
    else:
        argFlag2 = False
    
    
    if(arg != ""):
        try:
            if("." in arg):
                arg = float(arg)
            else:
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
            try:
                arg[i] = int(arg[i])
            except:
                pass
           
    #print(arg, type(arg))

    
    
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
            "m":matrixInitFunctions,
            "S":selectFromArray,
            "b":concatToPrintBuffer,
            "B":printAndResetBuffer,
            "i":printInteger,
            "q":quitProgram,
            "I":storeInput,
            "f":executeFunction,
            "d":debugIndex
            
            }
    
    #exec(functionDict(func) + "(" +str(arg)+")")
    (functionDict[func])(arg)
    
    
    
    #maybe make a function run inside a VM - call parser again?
    #(still partially under construction)
    #add a flag which can order a function to run locally - i.e. not affecting main memory
    #calling 'f' without an argument ends the current function
def executeFunction(functionIndex):
    global inFunction
    global functions
    global commands
    global skipTo
    global currentCommandIndex
    global endFunctionFlag
    global commandsCopyF
    global functionCommandList
    global currentCommandIndexF
    global currentFunction
    global loopList
    
    inFunction = True
    
    #print("function: ", functionIndex)
    
    if(functionIndex == None):
        endFunctionFlag = True
        
        while(currentCommandIndexF[-1] < len(functionCommandList[currentFunction])):
            if(functionCommandList[currentFunction][currentCommandIndexF[-1]][0] == "]"):
                del loopList[-1]
            if(functionCommandList[currentFunction][currentCommandIndexF[-1]][0] == "]"):
                loopList.append(0)
                
            currentCommandIndexF[-1] += 1       
        #currentCommandIndex = skipTo.pop(-1)
        #print("skipTo after pop: ", skipTo)
    else:
        currentFunction = functionIndex
        functionCommandList[currentFunction] = getCommandList(functions[functionIndex],1)
        commandsCopyF[currentFunction] = getCommandList(functions[functionIndex],1)
        
        
        
        from time import perf_counter as currentTime 
        start = currentTime() 
    
        currentCommandIndexF.append(0)
        while(currentCommandIndexF[-1] < len(functionCommandList[currentFunction])):
            
            if(endFunctionFlag):
                endFunctionFlag = False
                break
                
            inFunction = True
            runCommand(functionCommandList[currentFunction][currentCommandIndexF[-1]])
            currentCommandIndexF[-1] += 1
        
            if(currentCommandIndexF[-1] % 100 == 0):
                if(currentTime() > start + 5):
                    print("Program timed out. Did you forget your exit condition?")
                    break
            
            currentFunction = functionIndex
            
        #print("done function: ", functionIndex)
        #print(functionCommandList, currentCommandIndexF)
        currentCommandIndexF.pop(-1)
        #for i in range(len(skipTo)):
        #    skipTo[i] += len(functionCommandList)
        
        #skipTo.append(currentCommandIndex + len(functionCommandList))
        #print("skipTo: ", skipTo)
            
            
        #for i in range(len(functionCommandList)):
        #    commands.insert(currentCommandIndex + 1 + i, functionCommandList[i])
    
    #print(commands)
    
    #don't parse a function - insert its operations into queue         
    inFunction = False
    
def debugIndex(arg):
    print("d" + str(arg) + " has been executed")
    
    
def reformat(arg):
    fmt = str(arg)
    #first digit is type, next is arg to pass to sub-function
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
    if(arg == 0 or arg == None):
        topOfStack = str(topOfStack) 
    else:
        topOfStack = topOfStack[arg:-(arg)]
    
def mfloat(sigdigs=0):
    global topOfStack
    if(sigdigs == 0):
        topOfStack = float(topOfStack)   
    else:
        topOfStack = round(float(topOfStack), sigdigs)
    
    
    
    
    
    
def helloWorld(arg):#hello, world with variants
    if(argFlag):#given ^ as arg
        print("Hello world")
    elif(argFlag2):#given ? as arg
        print("Hello world!")
    elif(arg == None):
        print("Hello, World!")
    elif(arg == 0):
        print("hello world")
    else:    
        print("Hello, World!"*(arg+1))    
    
    
def add(arg):#add arg to stack
    #adds 1 to top of stack
    #given arg, adds arg to top of stack
    global topOfStack
    mfloat()
    if(arg==None):
        topOfStack += 1
    else:
        topOfStack += arg
    if(topOfStack == int(topOfStack)):
        topOfStack = int(topOfStack)
    
def subtract(arg):#subtract arg from stack
    #subtracts 1 from top of stack
    #given arg, subtracts arg from top of stack
    global topOfStack
    mfloat()
    if(arg==None):
        topOfStack -= 1
    else:
        topOfStack -= arg  
    if(topOfStack == int(topOfStack)):
        topOfStack = int(topOfStack)
    
def divide(arg):#divide stack/arg
    #divides the top of stack by 2
    #given 0 as arg, divides top of stack by 10
    #given other arg, divides top of stack by arg
    global topOfStack
    mfloat()
    if(arg==None):
        topOfStack /= 2
    elif(arg == 0):
        topOfStack /= 10
    else:
        topOfStack /= arg
    if(topOfStack == int(topOfStack)):
        topOfStack = int(topOfStack)    
    
def multiply(arg):#stack*=arg
    #multiplies the top of stack by 2
    #given 0 as arg, multiplies top of stack by 10
    #given other arg, multiplies top of stack by arg
    global topOfStack
    #mfloat()
    if(arg==None):
        topOfStack *= 2
    elif(arg == 0):
        topOfStack *= 10
    else:
        topOfStack *= arg  
    if(type(topOfStack) != str and topOfStack == int(topOfStack)):
        topOfStack = int(topOfStack)
     
    
def store(arg):#if the arg is None, it should instead use the current pointer
    #stores the top of the stack at the current pointer
    #given an arg, stores the top of the stack at arg in storage
    global storage
    global topOfStack
    if(arg != None):
        storage[arg] = topOfStack
    else:
        storage[pointer] = topOfStack

def get(arg):
    #sets the top of the stack to the value at the pointer
    #given an arg, sets the top of the stack to the value at arg
    global storage
    global topOfStack
    if(arg != None):
        topOfStack = storage[arg]
    else:
        topOfStack = storage[pointer]
    
def pointerUp(arg):
    #moves the pointer up
    #given an arg, moves the pointer up arg places
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
    #moves the pointer down
    #given an arg, moves the pointer down arg places
    global pointer
    if(arg == None):
        if(pointer != 0):
            pointer -= 1
        else:
            pointer = 99
    else:
        for i in range(arg):
            if(pointer != 0):
                pointer -= 1
            else:
                pointer = 99

            
def setPointer(arg):
    #sets the pointer to the arg
    global pointer
    
    if(arg == None):
        pointer = 0
    else:
        pointer = int(arg)            
            
            
def prnt(arg):
    #prints the value at the top of the stack
    #given an arg, prints the value at the arg in storage
    global topOfStack
    global storage
    global pointer
    #print(arg)
    if(arg == None):
        print(topOfStack)
    else:
        print(storage[arg])
        
def flag(arg):
    #used to define special flags:
    #  ! turns off the implicit output at the EOF (which is only turned on if input is taken)
    global outputAtEnd
    if(arg==None):
        outputAtEnd = False
        
        
def concat(arg):
    #concatenates the value at arg to the top of the stack
    global storage
    global topOfStack
    global pointer
    
    if(arg == None):
        topOfStack = str(topOfStack) + str(storage[pointer])
    else:
        topOfStack = str(topOfStack) + str(storage[arg])   


import copy
def startLoop(arg):
    #starts the loop - given an arg, only runs what's inside the loop iff the value on the stack is equal to the arg
    #if argFlag (i.e. ^) then it's an inverted if statement
    global currentCommandIndex
    global storage
    global loopList
    global commands
    global currentCommandIndex
    global argFlag
    global inFunction
    global currentCommandIndexF
    global functionCommandList
    #loopStart = currentCommandIndex
    global intoLoopArgs
    global topOfStack
    global pointer
    
    try:
        intoLoopArgs.append([topOfStack, storage[pointer], pointer, copy.deepcopy(storage)])
    except:
        try:
            intoLoopArgs.append([0, storage[pointer], pointer, copy.deepcopy(storage)])
        except:
            print("Unhandled error. Please send your code to rattleinterpreter@gmail.com and a fix will be issued soon!")
    
    
    if(not(inFunction)):
        loopList.append(currentCommandIndex)###
        if(arg == None): #case where the other bracket has an argument
            pass
        elif(argFlag):
            if(arg == topOfStack):
                #skip until the closing bracket
                while(commands[currentCommandIndex] != "]"):
                    currentCommandIndex += 1
                currentCommandIndex -= 1
        else:
            #print(arg, topOfStack)
            if(not(arg == topOfStack)):
                #skip until the closing bracket
                while(commands[currentCommandIndex] != "]"):
                    currentCommandIndex += 1
                currentCommandIndex -= 1
            #if statement..... based on stuff in storage (with a flag or something)
    else:
        loopList.append(currentCommandIndexF[currentFunction])        
        if(arg == None): #case where the other bracket has an argument
            pass
        elif(argFlag):
            if(arg == topOfStack):
                #skip until the closing bracket
                while(functionCommandList[currentFunction][currentCommandIndexF[-1]] != "]"):
                    currentCommandIndexF[-1] += 1
                currentCommandIndexF[-1] -= 1
        else:
            #print(arg, topOfStack)
            if(not(arg == topOfStack)):
                #skip until the closing bracket
                while(functionCommandList[currentFunction][currentCommandIndexF[-1]] != "]"):
                    currentCommandIndexF[-1] += 1
                currentCommandIndexF[-1] -= 1        
                
                
    
def endLoop(arg):
    #ends the loop - given an arg, this will loop arg times
    #given a ^, will loop the number of times specified by the value at arg in storage
    global loopEnd
    global currentCommandIndex
    global commands
    global commandsCopy
    global pointer
    global storage
    global topOfStack
    global inFunction
    global currentCommandIndexF
    global functionCommandList
    global commandsCopyF
    global loopList
    global intoLoopArgs
    #print("test ", commands[currentCommandIndex])
    #print("test ", loopList, commands[currentCommandIndex])
    #print(commands)
    
    if(inFunction == False):
        '''
        if("`" in commands[currentCommandIndex]):
            commands[currentCommandIndex] = commands[currentCommandIndex].replace("`", str(int(topOfStack) + 1))
        elif("~" in commands[currentCommandIndex]):
            commands[currentCommandIndex] = commands[currentCommandIndex].replace("~", str(int(storage[pointer])))
        elif("@" in commands[currentCommandIndex]):
            commands[currentCommandIndex] = commands[currentCommandIndex].replace("@", str(int(pointer)))    
        elif("^" in commands[currentCommandIndex]):
            commands[currentCommandIndex] = "]" + str(int(storage[arg]))      
        '''
        
        
        
        if("`" in commands[currentCommandIndex]):
            commands[currentCommandIndex] = commands[currentCommandIndex].replace("`", intoLoopArgs[-1][0])
        elif("~" in commands[currentCommandIndex]):
            commands[currentCommandIndex] = commands[currentCommandIndex].replace("~", intoLoopArgs[-1][1])
        elif("@" in commands[currentCommandIndex]):
            commands[currentCommandIndex] = commands[currentCommandIndex].replace("@", intoLoopArgs[-1][2])    
        elif("^" in commands[currentCommandIndex]):
            commands[currentCommandIndex] = "]" + str(int(intoLoopArgs[-1][3][arg]))
        
        
        
        
        
        if(arg == None): #case where the other bracket has arg (i.e. if statement)
            del loopList[-1]
        elif(arg == 1):
            
            commands[currentCommandIndex] = commandsCopy[currentCommandIndex]
            #print(commands)
            del loopList[-1]
            del intoLoopArgs[-1]
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
        
    else:
        
        if("`" in functionCommandList[currentFunction][currentCommandIndexF[-1]]):
            functionCommandList[currentFunction][currentCommandIndexF[-1]] = functionCommandList[currentFunction][currentCommandIndexF[-1]].replace("`", intoLoopArgs[-1][0])
        elif("~" in functionCommandList[currentFunction][currentCommandIndexF[-1]]):
            functionCommandList[currentFunction][currentCommandIndexF[-1]] = functionCommandList[currentFunction][currentCommandIndexF[-1]].replace("~", intoLoopArgs[-1][1])
        elif("@" in functionCommandList[currentFunction][currentCommandIndexF[-1]]):
            functionCommandList[currentFunction][currentCommandIndexF[-1]] = functionCommandList[currentFunction][currentCommandIndexF[-1]].replace("@", intoLoopArgs[-1][2])    
        elif("^" in functionCommandList[currentFunction][currentCommandIndexF[-1]]):
            functionCommandList[currentFunction][currentCommandIndexF[-1]] = "]" + intoLoopArgs[-1][3][arg] 
        
        '''
        if("`" in commands[currentCommandIndex]):
            commands[currentCommandIndex] = commands[currentCommandIndex].replace("`", intoLoopArgs[-1][0])
        elif("~" in commands[currentCommandIndex]):
            commands[currentCommandIndex] = commands[currentCommandIndex].replace("~", intoLoopArgs[-1][1])
        elif("@" in commands[currentCommandIndex]):
            commands[currentCommandIndex] = commands[currentCommandIndex].replace("@", intoLoopArgs[-1][2])    
        elif("^" in commands[currentCommandIndex]):
            commands[currentCommandIndex] = "]" + str(int(intoLoopArgs[-1][3][arg]))
        '''
       
        
        
        
        
        if(arg == None): #case where the other bracket has arg (i.e. if statement)
            del loopList[-1]
        elif(arg == 1):
            
            functionCommandList[currentFunction][currentCommandIndexF[-1]] = commandsCopyF[currentFunction][currentCommandIndexF[-1]]
            #print(commands)
            del loopList[-1]
            del intoLoopArgs[-1]
            #commands = commandsCopy##
            
            #print("here")
            #return
            #commands.pop(currentCommandIndex)
        else:
            #print(commands[currentCommandIndex][0] + str(int(commands[currentCommandIndex][1::])))
            functionCommandList[currentFunction][currentCommandIndexF[-1]] = functionCommandList[currentFunction][currentCommandIndexF[-1]][0] + str(int(functionCommandList[currentFunction][currentCommandIndexF[-1]][1::]) -1)
            #currentCommandIndex = loopStart##
            currentCommandIndexF[-1] = loopList[-1]##
                
    
def modulo(arg):
    #sets the top of the stack to the modulo of the arg (i.e. modulo(3) gives topOfStack % 3)
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
    #swaps the top of the stack and the pointed value
    #given an arg, swaps the top of the stack and the value at arg in storage
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
    #sets the second argument to the arg
    global secondArg
    secondArg = arg        
    

def topOfStackEquals(arg):
    #sets the top of the stack to the arg (or 0, given no arg)
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
    #given no arg, prints the char of the int at the top of the stack
    #given an arg, prints the char at the pointer
    global topOfStack
    global storage
    global pointer
    if(argFlag):
        if(arg == None):
            print(chr(int(topOfStack)))
            return
        print(chr(int(storage[pointer])))
    else:    
        if(arg == None):
            print(chr(int(topOfStack)), end="")
            return
        print(chr(int(storage[pointer])), end="")
    
    
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
        



def arrayOperations(arg):#unfinished
    #might use second arg
    #cycle, shift, reverse, +-*/%, RREF, linearly independant, max/min, max/min per each column/row, average/mode, sum
    
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
    
                
            
def selectFromArray(arg):
    global storage
    global pointer
    global topOfStack

    if(arg == None):
        topOfStack = storage[pointer][0]
    else:
        topOfStack = storage[pointer][arg]
        
        
def concatToPrintBuffer(arg):
    #adds to a string buffer for printing later
    #if argFlag (i.e. ^), it will eliminate the last item or a given argument
    #if argFlag2 (i.e. ?), it will delete the last item or the specified item
    #if neither argFlag, will append the top of the stack
    #if given an arg, will append the storage at the pointer
    
    global printBuffer
    global topOfStack
    global storage
    global pointer
    global argFlag
    global argFlag2
    #print("here1", arg, argFlag, argFlag2)
    
    if(argFlag):
        if(arg == None):
            printBuffer[-1] = ""
        else:
            printBuffer[arg] = "" 
    elif(argFlag2):
        #print("here")
        if(arg == None):
            del printBuffer[-1]
        else:
            del printBuffer[arg]
    elif(arg == None):
        printBuffer.append(str(topOfStack))    
    else:
        printBuffer.append(str(storage[arg]))


def printAndResetBuffer(arg):
    #prints the stored string buffer all on one line
    global printBuffer
    if(arg == None):
        if(printBuffer != []):
            print("".join(printBuffer))
            printBuffer = []
    else:
        print(("".join(printBuffer)) * arg)
        printBuffer = []
        
def printInteger(arg):
    #given no arg, prints the top of the stack as an int
    #given an arg, prints the storage at arg as an int
    global topOfStack
    global storage
    global pointer
    #print(arg)
    if(arg == None):
        print(int(topOfStack))
    else:
        print(int(storage[arg]))
    
        
def quitProgram(arg):
    global currentCommandIndex
    if(arg == None):
        currentCommandIndex += 2147483647
        
       
def storeInput(arg):
    global topOfStack
    global pointer
    global argFlag
    global storage
    
    try:
        oldTopOfStack = topOfStack
        #topOfStack = [topOfStack]
    except:
        pass
    if(argFlag):
        if(arg == None):
            for elem in topOfStack:
                storage[pointer] = elem
                pointer -= 1
        else:
            for i in range(arg):
                for elem in topOfStack:
                    storage[pointer] = elem
                    pointer -= 1
    elif(arg == None):
        for elem in topOfStack:
            storage[pointer] = elem
            pointer += 1
    else:
        for i in range(arg):
            for elem in topOfStack:
                storage[pointer] = elem
                pointer += 1
                
    topOfStack = oldTopOfStack            
    #stores top of stack starting at current pointer [if an array, stores each item in individual memory slots], sets pointer to slot after and gets value in this slot 
    #given an arg, does the same thing but arg times
    
def getArray(arg):
    pass
    #gets the next arg memory slots and creates an array with them    
        

