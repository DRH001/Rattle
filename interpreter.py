# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 08:48:37 2020

@author: Daniel

Updated 2022-02-06 13:00 EST
"""
version_ = "1.6.0"

"""
to do:
    
    make an arg of zero for a for loop stay at zero instead of going negative. [...]_n should loop n times but count backwards
    
    make commands operate on every item in a list if they otherwise don't support lists
    i.e. [1,2,3]| +1 p -> [2,3,4]
    ^     +,-,*,/,e
    make f^0 create a virtual machine which is passed the top of the stack and returns the virtual top of the stack, does not affect anything else


"""



"""
new:
    better arguments in brackets - (2/3) can now be an argument (including the brackets)
    
    exponentials [done]
    iterator in loop!!!!!!!!!!!!!!!!!!!!!!!! [done]
    list sum (numerical or string)
    negatives (_) (in args as well) (NEEDS TESTING)
    strings (take "" as args) [done]
    
    
    
    

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


    |P3 I I^ s =2 s0 [ g0 + s0 g` P2 s =1 /~  s2 g1 P2 +~ s1 ]~ P s =1 /~
    ^takes a list of resistances in parallel, returns total resistance (AKA harmonic sum)
    ^example input: [6,3,6]



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


import random




#import os
errout_ = ""
output_ = ""


def errorout(str_, end="\n"):
    global errout_

    errout_ += str(str_) + end


def getError():
    global errout_
    return(errout_)


def printout(str_, end="\n"):
    global output_

    output_ += str(str_) + end


class variables():
    pass

class localVariables():
    pass


class newLocalVariables():
    pass


classList = []


v = variables

def parse(code, topLevel = True):
    global v
    global classList
    if(topLevel):
        v = variables
    else:
        #localVariables = copy.deepcopy(newLocalVariables)
        #classList.append(copy.deepcopy(localVariables))
        classList.append(newLocalVariables())
        v = classList[-1]
        #v = localVariables
        #print(code)
    
    
    
    
    v.loopOrIf = []

    v.intoLoopArgs = []
    v.loopIterator = []

    v.currentFunction = -1
    v.currentCommandIndexF = []
    v.functionCommandList = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #this is the limit for no. of fns
    #localFunctionCommandList = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #this is the limit for no. of fns
    v.commandsCopyF = v.functionCommandList
    
    v.localFunctions = []
    
    
    
    v.inFunction = False

    v.endFunctionFlag = False

    v.skipTo = []

    v.currentCommandIndex = 0
    #loopStart = 0
    #loopCounter = 0
    v.pointer = 0
    v.storage = [0] * 100
    v.topOfStack = 0
    v.loopList = []
    v.storedArray = []
    v.secondArg = None
    v.argFlag = False
    v.argFlag2 = False
    v.printBuffer = []


    v.outputAtEnd = True
    v.commandsCopy = None

    #don't handle errors for now



    '''
    input|main;function0;function1......functionN:Function0:Function1.....FunctionN [then add arguments here which are stored to a local storage with max of 100 values] <-- NOT pushed to stack, separated by ,
    if | is the first character, input is taken through input(). If there is a "|", then whatever comes before it is pushed to stack. Otherwise, no input

    if the first character in main is a number, then the main method will be repeated that many times (i.e 1main will run twice) -> special case, 0 -> repeats 10 additional times (for 11 times total)

    '''

    #code = code.replace(" ","")
    
    #split code into input, main, functions, localFunctions:
    
    v.code = code
    if(":" in v.code):
        temp = v.code.split(":")
        v.localFunctions = temp[1:]
        v.code = temp[0]
    
    v.pieces = v.code.split(";")
    
    #import re
    #pieces = re.split(";|:", code)
    #pieces = code.split(";:",str)

    v.main = v.pieces[0]

    global inputs
    try:
        if("|" in v.main):

            if(v.main.split("|")[0] == ""):
                v.topOfStack = inputs.pop(0)

            else:
                v.topOfStack = v.main.split("|")[0]

            v.main = v.main.split("|")[1]#.replace(" ","").replace("\n","")
            
            openString = False
            newMain = ""
            for char in v.main:
                if(char == "\""):
                    if(not(openString)):
                        openString = True
                    else:
                        openString = False
                        
                if((char == " " or char == "\n") and not(openString)):
                    pass
                else:
                    newMain = newMain + char
            v.main = newMain
            
            #print(main)
            
            
            if(v.main == ""):
                printout(v.topOfStack)
                return

            for char in v.topOfStack:
                if(char == '\\'):
                    v.topOfStack = v.topOfStack.replace("\\", inputs.pop(0),1)

        else:
            v.outputAtEnd = False
            #v.main = v.main.replace(" ","").replace("\n","")
    except:
        errorout("Input error. Please ensure you have given the program the correct number of inputs!")
        return




    temp1 = []#auto-parses the input as what it should be
    temp2 = None
    try:
        v.topOfStack =v. topOfStack.split("&")
        for elem in v.topOfStack:
            try:
                exec("a = " + str(elem))
                temp2 = locals()["a"]
            except:
                temp2 = elem
            temp1.append(temp2)
        v.topOfStack = temp1

        if(len(v.topOfStack) == 1):
            v.topOfStack = v.topOfStack[0]
    except:
        try:
            exec("a = " + str(v.topOfStack))
            v.topOfStack = locals()["a"]
        except:
            pass

    cleanTopOfStack()

    v.functions = v.pieces[1::]

    #for i in range(len(v.functions)):
        #v.functions[i] = v.functions[i].replace(" ","")


    try:
        repeat = int(v.main[0])
        v.main = v.main[1::]
        if(v.repeat == 0):
            v.repeat = 10
        v.repeat = v.repeat + 1
    except:
        v.repeat = 1

    v.commands = getCommandList(v.main,v.repeat)
    v.commandsCopy = getCommandList(v.main, v.repeat)

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


    v.firstError = True

    while(v.currentCommandIndex < len(v.commands)):
        try:
            runCommand(v.commands[v.currentCommandIndex])
        except Exception as error:
            error_string = str(error)
            errorout("Error: " + error_string + " at command index " + str(v.currentCommandIndex) + " [" + str(v.commands[v.currentCommandIndex]) + "]")
            if(running):
                global output_
                global errout_
                print(output_)
                print(errout_)
                raise(error)
            return
        v.currentCommandIndex += 1
        #print("HERE!!!")

        if(currentTime() > start + 4):
            printout("Program timed out. Did you forget your exit condition?")
            errorout("timeout")
            return



    if(topLevel):
        #check for end flags: no output, output last character, etc
        if(v.printBuffer != []):
            printout("".join(v.printBuffer))
        elif(v.outputAtEnd):
            printout(v.topOfStack)





def getCommandList(f, rep):

    #f.replace("\n","")
    
    possibleArgs = "0123456789~`@&^?._#()"# & represents a spacer in case some functions need lots of arguments
    
    #^ and ? are argument flags
    tempList = []

    last = ""
    closed = True
    closedRoundBracket = True
    for i in range(len(f)):
        if(f[i] == "\"" and closed): #let strings exist as args
            closed = False
        elif(closed == False):
            if(not(f[i] == "\"")):
                tempList[-1] = last + f[i]
            last = tempList[-1]
            if(f[i] == "\""):
                closed = True
                #tempList[-1] = tempList[-1][:-1]#remove this
        elif(f[i] == "(" and closedRoundBracket): #let args exist in round brackets
            closedRoundBracket = False
        elif(closedRoundBracket == False):
            tempList[-1] = last + f[i]
            last = tempList[-1]
            if(f[i] == ")"):
                closedRoundBracket = True
                tempList[-1] = tempList[-1][:-1]    
                
                
        elif(not(f[i] in possibleArgs)):
            tempList.append(f[i])
            last = f[i]
        else:
            tempList[-1] = last + f[i]
            last = tempList[-1]

    return(tempList * rep)



def solveArg(arg):
    #global argRaw
    try:
        l = locals()
        
        arg2 = "x="+ str(arg)
        exec(arg2, locals())
        arg = l["x"]
        v.argRaw = arg
    except:
        pass
    
    return(arg)




def runCommand(c):
    #global storage
    #global pointer
    #global argFlag
    #global argFlag2
    #global argRaw
    #global loopIterator

    func = c[0]
    if(func == " " or func == "\n"):
        return

    arg = c[1::]
    v.argRaw = arg
    
    inLoop = func == "]" and arg != None and arg != "" and (v.loopOrIf == [] or v.loopOrIf[-1])

    if("^" in arg):
        arg = arg.replace("^","")
        v.argFlag = True
    else:
        v.argFlag = False

    if("?" in arg):
        arg = arg.replace("?","")
        v.argFlag2 = True
    else:
        v.argFlag2 = False
        
        
    if("_" in arg):
        arg = arg.replace("_","-")
        v.argRaw = arg
        
    

    if("~" in arg):
        if(inLoop):
            arg = arg.replace("~",str(v.intoLoopArgs[-1][1]))
            v.argRaw = v.storage[v.pointer]
        else:    
            arg = arg.replace("~",str(int(v.storage[v.pointer])))
            v.argRaw = v.storage[v.pointer]
            
            
        #ADD CASE FOR inFunction as well!!!!!!!!!!!!!!!!!!! @todo

    if("`" in arg):
        if(inLoop):
            arg = arg.replace("`",str(v.intoLoopArgs[-1][0]))
            v.argRaw = v.topOfStack
        else:    
            arg = arg.replace("`",str(int(v.topOfStack)))
            v.argRaw = v.topOfStack

    if("@" in arg):
        if(inLoop):
            arg = arg.replace("@",str(v.intoLoopArgs[-1][2]))
        else:    
            arg = arg.replace("@",str(int(v.pointer)))
        
        
    if("#" in arg): #NEEDS TO BE REPLACED LAST
        if("#" == arg):
            arg = str(int(v.loopIterator[-1]))
            v.argRaw = arg
        else:
            
            import re
            
            #pieces = arg.split("+").split("-").split("*").split("/").split("\"").split("%").split("==")
            pieces = re.split("\+|-|\*|/|\"|%|==|\*\*", arg)
            import copy
            piecesCopy = copy.deepcopy(pieces)
            
            for i in range(len(pieces)):
                if("#" in pieces[i]):
                   coarg = int(pieces[i].replace("#",""))
                   pieces[i] = v.loopIterator[-(1+coarg)]
                   arg = arg.replace(str(piecesCopy[i]), str(pieces[i]), 1)
                   
            
            
            #coarg = int(arg.replace("#",""))
            #arg = loopIterator[-(1+coarg)]  
            #argRaw = arg

    
    #print(arg, type(arg))

    arg = solveArg(arg)
    if(type(arg) == tuple):
        arg = list(arg)

    #print("here3", arg)

    if(arg != ""): #PARSE ARG AS INT OR FLOAT IF POSSIBLE
        try:
            v.argRaw = float(v.argRaw)
            if("." in arg):
                arg = float(arg)
            else:
                arg = int(float(arg))
        except:
            pass
      

    if(arg == ""):
        arg = None

    
    
    if("&" in str(arg)):#changes arg to a list
        arg = arg.split("&")
        for i in range(len(arg)):
            try:
                if("." in arg[i]):
                    arg[i] = float(arg[i])
                else:
                    arg[i] = int(float(arg[i]))
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
            "v":pointedValueInStorageEquals,
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
            "d":debugIndex,
            "n":getInteger,
            "e":exponentiate,
            "F":executeLocalFunction,
            "l":listOperation

            }

    #exec(functionDict(func) + "(" +str(arg)+")")
    (functionDict[func])(arg)



    #maybe make a function run inside a VM - call parser again?
    #(still partially under construction)
    #add a flag which can order a function to run locally - i.e. not affecting main memory
    #calling 'f' without an argument ends the current function
def executeFunction(functionIndex):
    #global inFunction
    #global functions
    #global commands
    #global skipTo
    #global currentCommandIndex
    #global endFunctionFlag
    #global commandsCopyF
    #global functionCommandList
    #global currentCommandIndexF
    #global currentFunction
    #global loopList
    #global firstError

    v.inFunction = True

    #print("function: ", functionIndex)

    if(functionIndex == None):
        v.endFunctionFlag = True

        while(v.currentCommandIndexF[-1] < len(v.functionCommandList[v.currentFunction])):
            if(v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]][0] == "]"):
                del v.loopList[-1]
            if(v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]][0] == "]"):
                v.loopList.append(0)

            v.currentCommandIndexF[-1] += 1
        #currentCommandIndex = skipTo.pop(-1)
        #print("skipTo after pop: ", skipTo)
    else:
        v.currentFunction = functionIndex
        v.functionCommandList[v.currentFunction] = getCommandList(v.functions[functionIndex],1)
        
        
        
        v.commandsCopyF[v.currentFunction] = getCommandList(v.functions[functionIndex],1)
        
        '''try:
            v.functionCommandList[v.currentFunction].remove("\n")
            v.commandsCopyF[v.currentFunction].remove("\n")
        except:
            pass'''


        from time import perf_counter as currentTime
        start = currentTime()

        v.currentCommandIndexF.append(0)
        while(v.currentCommandIndexF[-1] < len(v.functionCommandList[v.currentFunction])):

            if(v.endFunctionFlag):
                v.endFunctionFlag = False
                break

            v.inFunction = True
            try:
                runCommand(v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]])
            except Exception as error:
                error_string = str(error)
                if(v.firstError):
                    errorout("Error: " + error_string + " in function " + str(v.currentFunction) + " at function command index " + str(v.currentCommandIndexF[-1]) + " [" + str(v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]]) + "]")
                    v.firstError = False
                else:
                    errorout("Error: " + error_string + " at function command index " + str(v.currentCommandIndexF[-1]) + " [" + str(v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]]) + "]")


                v.currentCommandIndexF.pop(-1)
                v.currentFunction = functionIndex
                raise(Exception("error in function " + str(v.currentFunction)))
            v.currentCommandIndexF[-1] += 1

            if(currentTime() > start + 5):
                printout("Program timed out. Did you forget your exit condition?")
                return

            v.currentFunction = functionIndex

        #print("done function: ", functionIndex)
        #print(functionCommandList, currentCommandIndexF)
        v.currentCommandIndexF.pop(-1)
        #for i in range(len(skipTo)):
        #    skipTo[i] += len(functionCommandList)

        #skipTo.append(currentCommandIndex + len(functionCommandList))
        #print("skipTo: ", skipTo)


        #for i in range(len(functionCommandList)):
        #    commands.insert(currentCommandIndex + 1 + i, functionCommandList[i])

    #print(commands)

    #don't parse a function - insert its operations into queue
    v.inFunction = False

def debugIndex(arg):
    printout("d" + str(arg) + " has been executed")


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
    #global topOfStack
    if(sigdigs == 0):
        v.topOfStack = int(float(v.topOfStack))
        return
    else:
        from math import log
        b = int(log(float(v.topOfStack),10))
        v.topOfStack = int(float(v.topOfStack)/10**(b+1-sigdigs)) *10**(b+1-sigdigs)

def mstr(arg=0):
    #global topOfStack
    if(arg == 0 or arg == None):
        v.topOfStack = str(v.topOfStack)
    else:
        v.topOfStack = v.topOfStack[arg:-(arg)]

def mfloat(sigdigs=0):
    #global topOfStack
    if(sigdigs == 0):
        v.topOfStack = float(v.topOfStack)
    else:
        v.topOfStack = round(float(v.topOfStack), sigdigs)



def cleanTopOfStack():
    #makes any values in the top of the stack into an int if possible without loss of precision
    #global topOfStack
    
    if(type(v.topOfStack) == tuple):
        v.topOfStack = list(v.topOfStack)
    
    
    if(type(v.topOfStack) != list):
        try:
            if(v.topOfStack == int(v.topOfStack)):
                v.topOfStack = int(v.topOfStack)
        except:
            pass
        return
    
    for i in range(len(v.topOfStack)):
        try:
            if(v.topOfStack[i] == int(v.topOfStack[i])):
                v.topOfStack[i] = int(v.topOfStack[i])
        except:
            pass
        


def helloWorld(arg):#hello, world with variants
    if(v.argFlag):#given ^ as arg
        printout("Hello world")
    elif(v.argFlag2):#given ? as arg
        printout("Hello world!")
    elif(arg == None):
        printout("Hello, World!")
    elif(arg == 0):
        printout("hello world")
    else:
        printout("Hello, World!"*(arg+1))


def add(arg):#add arg to stack
    #adds 1 to top of stack
    #given arg, adds arg to top of stack
    #global topOfStack
    #global argRaw
    
    #print(arg, type(arg))
    if(type(v.topOfStack) == str or type(arg) == str):
        v.topOfStack = str(v.topOfStack) + str(arg)
        return
    
    
    
    
    if(type(v.topOfStack) == list):
        if(arg==None):
            v.topOfStack = [elem + 1 for elem in v.topOfStack]
        else:
            v.topOfStack = [elem + v.argRaw for elem in v.topOfStack]
        cleanTopOfStack()
        return()
    
    mfloat()
    
    if(arg==None):
        v.topOfStack += 1
    else:
        v.topOfStack += v.argRaw
    cleanTopOfStack()

def subtract(arg):#subtract arg from stack
    #subtracts 1 from top of stack
    #given arg, subtracts arg from top of stack
    #global topOfStack
    
    if(type(v.topOfStack) == str or type(arg) == str):
        v.topOfStack = v.topOfStack.replace(arg, "")
        return
    
    
    if(type(v.topOfStack) == list):
        if(arg==None):
            v.topOfStack = [elem - 1 for elem in v.topOfStack]
        else:
            v.topOfStack = [elem - v.argRaw for elem in v.topOfStack]
        cleanTopOfStack()
        return()
    
    
    
    mfloat()
    if(arg==None):
        v.topOfStack -= 1
    else:
        v.topOfStack -= v.argRaw
    cleanTopOfStack()

def divide(arg):#divide stack/arg
    #divides the top of stack by 2
    #given 0 as arg, divides top of stack by 10
    #given other arg, divides top of stack by arg
    #global topOfStack
    
    if(type(v.topOfStack) == list):
        if(arg==None):
            v.topOfStack = [elem / 2 for elem in v.topOfStack]
        else:
            v.topOfStack = [elem / v.argRaw for elem in v.topOfStack]
        cleanTopOfStack()
        return()
    
    
    mfloat()
    if(arg==None):
        v.topOfStack /= 2
    #elif(argRaw == 0):
    #    topOfStack /= 10
    else:
        v.topOfStack /= v.argRaw
    if(v.topOfStack == int(v.topOfStack)):
        v.topOfStack = int(v.topOfStack)

def multiply(arg):#stack*=arg
    #multiplies the top of stack by 2
    #given 0 as arg, multiplies top of stack by 10
    #given other arg, multiplies top of stack by arg
    #global topOfStack
    #mfloat()
    
    if(type(v.topOfStack) == list):
        if(arg==None):
            v.topOfStack = [elem * 2 for elem in v.topOfStack]
        else:
            v.topOfStack = [elem * v.argRaw for elem in v.topOfStack]
        cleanTopOfStack()
        return()
    
    
    
    if(arg==None):
        v.topOfStack *= 2
    #elif(argRaw == 0):
    #    topOfStack *= 10
    else:
        v.topOfStack *= v.argRaw
    if(type(v.topOfStack) != str and v.topOfStack == int(v.topOfStack)):
        v.topOfStack = int(v.topOfStack)


def store(arg):#if the arg is None, it should instead use the current pointer
    #stores the top of the stack at the current pointer
    #given an arg, stores the top of the stack at arg in storage
    #global storage
    #global topOfStack
    
    if(type(arg) == str):
        v.storage[v.pointer] = arg    
    elif(arg != None):
        v.storage[arg] = v.topOfStack
    else:
        v.storage[v.pointer] = v.topOfStack

def get(arg):
    #sets the top of the stack to the value at the pointer
    #given an arg, sets the top of the stack to the value at arg
    #global storage
    #global topOfStack
    if(arg != None):
        v.topOfStack = v.storage[arg]
    else:
        v.topOfStack = v.storage[v.pointer]

def pointerUp(arg):
    #moves the pointer up
    #given an arg, moves the pointer up arg places
    #global pointer
    if(arg == None):
        if(v.pointer != 99):
            v.pointer += 1
        else:
            v.pointer = 0
    else:
        for i in range(arg):
            if(v.pointer != 99):
                v.pointer += 1
            else:
                v.pointer = 0


def pointerDown(arg):
    #moves the pointer down
    #given an arg, moves the pointer down arg places
    #global pointer
    if(arg == None):
        if(v.pointer != 0):
            v.pointer -= 1
        else:
            v.pointer = 99
    else:
        for i in range(arg):
            if(v.pointer != 0):
                v.pointer -= 1
            else:
                v.pointer = 99


def setPointer(arg):
    #sets the pointer to the arg
    #global pointer

    if(arg == None):
        v.pointer = 0
    else:
        v.pointer = int(arg)


def prnt(arg):
    #prints the value at the top of the stack
    #given an arg, prints the value at the arg in storage
    #global topOfStack
    #global storage
    #global pointer
    #print(arg)
    if(type(arg)==str):
        printout(arg)
    elif(arg == None):
        printout(v.topOfStack)
    else:
        printout(v.storage[arg])

def flag(arg):
    #used to define special flags:
    #  ! turns off the implicit output at the EOF (which is only turned on if input is taken)
    #global outputAtEnd
    if(arg==None):
        v.outputAtEnd = False


def concat(arg):
    #concatenates the value at arg to the top of the stack
    #global storage
    #global topOfStack
    #global pointer

    if(type(arg)==str):
        v.topOfStack = str(v.topOfStack) + arg
    elif(arg == None):
        v.topOfStack = str(v.topOfStack) + str(v.storage[v.pointer])
    else:
        v.topOfStack = str(v.topOfStack) + str(v.storage[arg])


import copy
def startLoop(arg):
    #starts the loop - given an arg, only runs what's inside the loop iff the value on the stack is equal to the arg
    #if argFlag (i.e. ^) then it's an inverted if statement
    '''global currentCommandIndex
    global storage
    global loopList
    global commands
    global argFlag
    global inFunction
    global currentCommandIndexF
    global functionCommandList
    #loopStart = currentCommandIndex
    global intoLoopArgs
    global topOfStack
    global pointer
    global loopIterator
    global loopOrIf'''

    
    v.loopIterator.append(0)
    #printout("LOOP")

    try:
        if (arg == None):#FOR LOOP!
            #loopIterator.append(0)
            v.loopOrIf.append(True)
            v.intoLoopArgs.append([v.topOfStack, v.storage[v.pointer], v.pointer, copy.deepcopy(v.storage)])
        else: #IF STATEMENT
            v.loopOrIf.append(False)
    except:
        try:
            if (arg == None):
                v.intoLoopArgs.append([0, v.storage[v.pointer], v.pointer, copy.deepcopy(v.storage)])
        except:
            print("Unhandled error. Please send your code to rattleinterpreter@gmail.com and a fix will be issued soon!")

    #print(arg == topOfStack, argFlag)

    if(not(v.inFunction)):
        v.loopList.append(v.currentCommandIndex)###
        if(arg == None or arg == ""): #case where the other bracket has an argument
            pass
        elif(v.argFlag):
            if(str(arg) == str(v.topOfStack)):
                #print("HERE!")
                #skip until the closing bracket
                
                closed = False
                opens = 1
                while(not(closed)):
                    v.currentCommandIndex += 1
                    if(v.commands[v.currentCommandIndex][0] == "["):
                        opens += 1
                    if(v.commands[v.currentCommandIndex][0] == "]"):
                        opens -= 1
                        if(opens == 0):
                            closed = True
                v.currentCommandIndex -= 1
                #print("HERE!", commands[currentCommandIndex])
        else:
            #print(arg, topOfStack)
            if(not(str(arg) == str(v.topOfStack))):
                #skip until the closing bracket
                
                closed = False
                opens = 1
                while(not(closed)):
                    v.currentCommandIndex += 1
                    if(v.commands[v.currentCommandIndex][0] == "["):
                        opens += 1
                    if(v.commands[v.currentCommandIndex][0] == "]"):
                        opens -= 1
                        if(opens == 0):
                            closed = True
                v.currentCommandIndex -= 1
            #if statement..... based on stuff in storage (with a flag or something)
    else:
        v.loopList.append(v.currentCommandIndexF[v.currentFunction])
        if(arg == None or arg == ""): #case where the other bracket has an argument
            pass
        elif(v.argFlag):
            if(str(arg) == str(v.topOfStack)):
                #skip until the closing bracket
                closed = False
                opens = 1
                while(not(closed)):
                    v.currentCommandIndexF[-1] += 1
                    if(v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]][0] == "["):
                        opens += 1
                    if(v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]][0] == "]"):
                        opens -= 1
                        if(opens == 0):
                            closed = True
                v.currentCommandIndexF[-1] -= 1
                
            
        else:
            #print(arg, topOfStack)
            if(not(str(arg) == str(v.topOfStack))):
                #skip until the closing bracket
                closed = False
                opens = 1
                while(not(closed)):
                    v.currentCommandIndexF[-1] += 1
                    if(v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]][0] == "["):
                        opens += 1
                    if(v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]][0] == "]"):
                        opens -= 1
                        if(opens == 0):
                            closed = True
                v.currentCommandIndexF[-1] -= 1




def endLoop(arg):
    #ends the loop - given an arg, this will loop arg times
    #given a ^, will loop the number of times specified by the value at arg in storage
    '''global loopEnd
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
    global loopIterator
    global loopOrIf'''
    
    v.loopIterator[-1] += 1

    if(v.inFunction == False):
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



        if("`" in v.commands[v.currentCommandIndex]):
            v.commands[v.currentCommandIndex] = v.commands[v.currentCommandIndex].replace("`", str(v.intoLoopArgs[-1][0]))
        elif("~" in v.commands[v.currentCommandIndex]):
            v.commands[v.currentCommandIndex] = v.commands[v.currentCommandIndex].replace("~", str(v.intoLoopArgs[-1][1]))
        elif("@" in v.commands[v.currentCommandIndex]):
            v.commands[v.currentCommandIndex] = v.commands[v.currentCommandIndex].replace("@", str(v.intoLoopArgs[-1][2]))
        elif("^" in v.commands[v.currentCommandIndex]):
            v.commands[v.currentCommandIndex] = "]" + str(int(v.intoLoopArgs[-1][3][arg]))





        if(arg == None or arg == ""): #case where the other bracket has arg (i.e. if statement) #END OF LOOP
            #printout("LOOPX")
            del v.loopList[-1]
            del v.loopIterator[-1]
            del v.loopOrIf [-1]
            
        elif(v.commands[v.currentCommandIndex][1:] == "1"): #END OF LOOP

            v.commands[v.currentCommandIndex] = v.commandsCopy[v.currentCommandIndex]
            #print(commands)
            #printout("LOOPX")
            del v.loopList[-1]
            del v.intoLoopArgs[-1]
            del v.loopIterator[-1]
            del v.loopOrIf [-1]
            
            #commands = commandsCopy##

            #print("here")
            #return
            #commands.pop(currentCommandIndex)
        else:

            #print(commands[currentCommandIndex][0] + str(int(commands[currentCommandIndex][1::])))
            l = locals()
            code_ = "x=" + str(v.commands[v.currentCommandIndex][1::])
            exec(code_, locals())
            newArg = l["x"]
            
            
            
            v.commands[v.currentCommandIndex] = v.commands[v.currentCommandIndex][0] + str(int(newArg) -1)
            #currentCommandIndex = loopStart##
            v.currentCommandIndex = v.loopList[-1]##

        #print("test ",loopList,  commands[currentCommandIndex], "\n")

    else: #IN FUNCTION

        if("`" in v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]]):
            v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]] = v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]].replace("`", str(v.intoLoopArgs[-1][0]))
        elif("~" in v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]]):
            v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]] = v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]].replace("~", str(v.intoLoopArgs[-1][1]))
        elif("@" in v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]]):
            v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]] = v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]].replace("@", str(v.intoLoopArgs[-1][2]))
        elif("^" in v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]]):
            v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]] = "]" + v.intoLoopArgs[-1][3][arg]

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





        if(arg == None or arg == ""): #case where the other bracket has arg (i.e. if statement) #END FUNCTION LOOP
            del v.loopList[-1]
            del v.loopIterator[-1]
            del v.loopOrIf [-1]
        elif(v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]][1:] == "1"): #END FUNCTION LOOP

            v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]] = v.commandsCopyF[v.currentFunction][v.currentCommandIndexF[-1]]
            #print(commands)
            del v.loopList[-1]
            del v.intoLoopArgs[-1]
            del v.loopIterator[-1]
            del v.loopOrIf [-1]
            #commands = commandsCopy##

            #print("here")
            #return
            #commands.pop(currentCommandIndex)
        else:
            #print(commands[currentCommandIndex][0] + str(int(commands[currentCommandIndex][1::])))
            l = locals()
            code_ = "x=" + str(v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]][1::])
            exec(code_, locals())
            newArg = l["x"]
            
            
            v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]] = v.functionCommandList[v.currentFunction][v.currentCommandIndexF[-1]][0] + str(int(newArg) -1)
            #currentCommandIndex = loopStart##
            v.currentCommandIndexF[-1] = v.loopList[-1]##



def modulo(arg):
    #sets the top of the stack to the modulo of the arg (i.e. modulo(3) gives topOfStack % 3)
    #global topOfStack
    mfloat()
    if(arg == None):
        v.topOfStack = v.topOfStack % 2
    elif(arg == 0):
        v.topOfStack = v.topOfStack % 10
    elif(arg == 1):
        v.topOfStack = v.topOfStack % 100
    else:
        v.topOfStack = v.topOfStack % arg
    if(v.topOfStack == int(v.topOfStack)):
        v.topOfStack = int(v.topOfStack)




def swap(arg):
    #swaps the top of the stack and the pointed value
    #given an arg, swaps the top of the stack and the value at arg in storage
    #global topOfStack
    #global pointer
    #global storage
    if(arg == None):
        tempSwap = v.storage[v.pointer]
        v.storage[v.pointer] = v.topOfStack
        v.topOfStack = tempSwap
    else:
        tempSwap = v.storage[arg]
        v.storage[arg] = v.topOfStack
        v.topOfStack = tempSwap


def secondArgument(arg):
    #sets the second argument to the arg
    #global secondArg
    v.secondArg = arg


def topOfStackEquals(arg):
    #sets the top of the stack to the arg (or 0, given no arg)
    #global topOfStack
    
    
    if(v.argFlag2): #randomness
        
        if(arg==None):
            v.topOfStack = random.random()
        else:
            v.topOfStack = random.randint(0,arg-1)
        
        
        
        return
    
    
    
    if(arg == None):
        v.topOfStack = 0
        return
    v.topOfStack = arg
    
    
    
    

def pointedValueInStorageEquals(arg):
    #global storage
    #global pointer
    if(arg == None):
        v.storage[v.pointer] = 0
        return
    v.storage[v.pointer] = arg

def stringFunction(arg):
    #global topOfStack
    if(arg == None): #flip topOfStack
        v.topOfStack = str(v.topOfStack)[::-1] 
        
    pass#define string functions here: flip/reverse, bin/hex (or make new fns for these), decompress (e.g. 126 bit compression), caesar shift


def printCharAt(arg):
    #given no arg, prints the char of the int at the top of the stack
    #given an arg, prints the char at the pointer
    #global topOfStack
    #global storage
    #global pointer
    if(v.argFlag):
        if(arg == None):
            printout(chr(int(v.topOfStack)))
            return
        printout(chr(int(v.storage[v.pointer])))
    elif(v.argFlag2):
        v.topOfStack = chr(int(v.topOfStack))
        return
    else:
        if(arg == None):
            #print("HERE!")
            printout(chr(int(v.topOfStack)), end="")
            return
        printout(chr(int(v.storage[v.pointer])), end="")


def arrayInitFunctions(arg):
    # a1 stores array of zeroes of length topOfStack at the pointer
    # a1_ pushes an array of the bottom arg to stack
    # a2 pushes an array of alternating ones and zeroes - secondarg is none, it starts at 1. secondarg is 0, it starts at 0. Else, it gives an array of secondArray's value and zeroes that alternate, starting with non-zero
    # to add: range, linspace,
    #global topOfStack
    #global storedArray
    #global storage
    #global pointer
    #global secondArg


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
            v.storage[v.pointer] = [0] * v.topOfStack
            return

        v.topOfStack = [bottomArg] * v.topOfStack

    if(topArg == 2):
        #might need 2nd arg
        if(v.secondArg == None):
            tempSwitch = 1
            tempArray = []
            for i in range(bottomArg):
                tempArray.append(tempSwitch)
                if(tempSwitch):
                    tempSwitch = 0
                else:
                    tempSwitch = 1
            v.topOfStack = tempArray

        elif(v.secondArg == 0):
            tempSwitch = 0
            tempArray = []
            for i in range(bottomArg):
                tempArray.append(tempSwitch)
                if(tempSwitch):
                    tempSwitch = 0
                else:
                    tempSwitch = 1
            v.topOfStack = tempArray

        else:
            tempSwitch = v.secondArg
            tempArray = []
            for i in range(bottomArg):
                tempArray.append(tempSwitch)
                if(tempSwitch):
                    tempSwitch = 0
                else:
                    tempSwitch = v.secondArg
            v.topOfStack = tempArray




def arrayOperations(arg):#unfinished
    #might use second arg
    #cycle, shift, reverse, +-*/%, RREF, linearly independant, max/min, max/min per each column/row, average/mode, sum

    #global topOfStack
    #global secondArg

    if(arg == None):
        #reverse array
        pass

    if(len(arg) == 1):
        if(arg==None):
            pass



    pass






def matrixInitFunctions(arg):
    #uses the second argument!!!!!
    #global secondArg
    #global topOfStack
    pass



def selectFromArray(arg):
    #global storage
    #global pointer
    #global topOfStack

    if(arg == None):
        v.topOfStack = v.storage[v.pointer][0]
    else:
        v.topOfStack = v.storage[v.pointer][arg]


def concatToPrintBuffer(arg):
    #adds to a string buffer for printing later
    #if argFlag (i.e. ^), it will eliminate the last item or a given argument
    #if argFlag2 (i.e. ?), it will delete the last item or the specified item
    #if neither argFlag, will append the top of the stack
    #if given an arg, will append the storage at the pointer

    #global printBuffer
    #global topOfStack
    #global storage
    #global pointer
    #global argFlag
    #global argFlag2
    #print("here1", arg, argFlag, argFlag2)

    if(arg != None):
        try:
            arg = int(arg)
        except:
            v.printBuffer.append(arg)
            return

    if(v.argFlag):
        if(arg == None):
            v.printBuffer[-1] = ""
        else:
            v.printBuffer[arg] = ""
    elif(v.argFlag2):
        #print("here")
        if(arg == None):
            del v.printBuffer[-1]
        else:
            del v.printBuffer[arg]
    elif(type(arg)==str):
        v.printBuffer.append(arg)        
    elif(arg == None):
        v.printBuffer.append(str(v.topOfStack))
    else:
        v.printBuffer.append(str(v.storage[arg]))


def printAndResetBuffer(arg):
    #prints the stored string buffer all on one line
    #global printBuffer
    if(arg == None):
        if(v.printBuffer != []):
            printout("".join(v.printBuffer))
            v.printBuffer = []
    else:
        printout(("".join(v.printBuffer)) * arg)
        v.printBuffer = []

def printInteger(arg):
    #given no arg, prints the top of the stack as an int
    #given an arg, prints the storage at arg as an int
    #global topOfStack
    #global storage
    #global pointer
    #print(arg)
    if(arg == None):
        if(type(v.topOfStack)==str or type(v.topOfStack)==chr):
            printout(ord(str(v.topOfStack)))
        else:
            printout(int(v.topOfStack))
    elif(type(v.topOfStack)==int):
        printout(int(v.storage[arg]))
    elif(type(v.topOfStack)==str or type(v.topOfStack)==chr):
        printout(ord(str(v.storage[arg])))


def getInteger(arg):
    #global topOfStack
    #global storage
    #global pointer
    #print(arg)
    if(arg == None):
        if(type(v.topOfStack)==str or type(v.topOfStack)==chr):
            v.topOfStack = (ord(str(v.topOfStack)))
        else:
            v.topOfStack = (int(v.topOfStack))
    elif(type(v.topOfStack)==int):
        v.topOfStack = (int(v.storage[arg]))
    elif(type(v.topOfStack)==str or type(v.topOfStack)==chr):
        v.topOfStack = (ord(str(v.storage[arg])))


def quitProgram(arg):
    #global currentCommandIndex
    if(arg == None):
        v.currentCommandIndex += 2147483647
    else:
        printout(v.storage[arg])
        v.currentCommandIndex += 2147483647


def storeInput(arg):
    #global topOfStack
    #global pointer
    #global argFlag
    #global storage

    try:
        oldTopOfStack = v.topOfStack
        #topOfStack = [topOfStack]
    except:
        pass
    
    if(arg != None):
        arg = int(arg)
        

    if(arg == None and not(v.argFlag or v.argFlag2)):
        #no args: stores list at top of stack in consecutive memory slots
        for elem in v.topOfStack:
            v.storage[v.pointer] = elem
            v.pointer += 1
        v.topOfStack = oldTopOfStack


    if(v.argFlag2):
        # "?" arg (argFlag2)
        if(arg == None):
            #stores list at top of stack in consective memory slots, but in reverse
            for i in range(len(v.topOfStack)):
                v.storage[v.pointer] = v.topOfStack[-(i+1)]
                v.pointer += 1
            v.topOfStack = oldTopOfStack

    if(arg != None and not(v.argFlag or v.argFlag2)):
        #with numerical arg: gets value at index arg
        v.topOfStack = v.topOfStack[arg]

    if(arg != None and v.argFlag and not(v.argFlag2)):
        #argFlag and numerical arg: make list from arg number of values in consecutive memory slots starting at pointer
        v.topOfStack = []
        for i in range(arg):
            v.topOfStack.append(v.storage[v.pointer + i])

    if(arg == None and v.argFlag and not(v.argFlag2)):
        #given ^ only, gets length of top of stack
        if(type(v.topOfStack) == int):
            v.topOfStack = len(str(v.topOfStack))
        elif(type(v.topOfStack) == float):
            #make this return no. of decimal points instead? str(topOfStack).split(".")[1]
            v.topOfStack = len(str(v.topOfStack))
        else:
            v.topOfStack = len(v.topOfStack)



    #topOfStack = oldTopOfStack
    #stores top of stack starting at current pointer [if an array, stores each item in individual memory slots], sets pointer to slot after and gets value in this slot


def getArray(arg):
    pass
    #gets the next arg memory slots and creates an array with them




def exponentiate(arg):
    #global topOfStack
    #global argRaw
    
    
    
    if(type(v.topOfStack) == list):
        if(arg==None):
            v.topOfStack = [elem ** 2 for elem in v.topOfStack]
        else:
            v.topOfStack = [elem ** v.argRaw for elem in v.topOfStack]
        cleanTopOfStack()
        return()
    
    
    
    
    mfloat()
    if(arg==None):
        v.topOfStack **=2
    else:
        v.topOfStack **= v.argRaw
    if(v.topOfStack == int(v.topOfStack)):
        v.topOfStack = int(v.topOfStack)



def listOperation(arg):
    
    
    if(type(v.topOfStack) != list):
        if(arg == None):
            if(v.argFlag):
                v.topOfStack = [v.topOfStack, v.storage[v.pointer]]
            else:
                v.topOfStack = [v.topOfStack] #convert to list
    
        elif(v.argFlag):
            v.topOfStack = [v.topOfStack, v.storage[arg]]
        else:
            v.topOfStack = [v.topOfStack, arg]
    
    elif(type(arg) == list): #given [x,y] set element x of the top of the stack to y
        v.topOfStack[arg[0]] = arg[1]
    
    else:
        if(arg == None):
            if(v.argFlag):
                v.topOfStack.append(v.storage[v.pointer])
            else:
                v.topOfStack = v.topOfStack[0] #convert from list to what's inside the list (e.g. [0] -> 0)
    
        elif(v.argFlag):
            v.topOfStack.append(v.storage[arg])
        else:
            v.topOfStack.append(arg)
        
        
        
    
    






def executeLocalFunction(arg):
    global v
    global classList
    #localFunctionToExecute = localFunctions[arg]
    
    
    if(arg == None): #end local function
        quitProgram(None)
        return
        #del classList[-1]
        
    
    
    #v = localVariables
    if(v.argFlag): #pass all current data....
        #v = copy.deepcopy(variables)
        pass
    
    
    exec("parse(str(v.topOfStack) + \"|!\" + variables.localFunctions[arg], topLevel = False)")
    temp = v.topOfStack
    
    #print(v)
    
    #v = variables
    #v.topOfStack = temp
    #print("testing")

    #print(classList[0].code, classList[1].code)
    #print([elem.code for elem in classList])
    #print("here%d",classList[-1].currentCommandIndex)
    del classList[-1]
    if(classList != []):
        v = classList[-1]
    else:
        v = variables
        #print("hereeee")

    v.topOfStack = temp











#THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
#file = os.path.join(THIS_FOLDER, fileName)

running = False
def execute(code, flags, input_list, output_var):
    global out
    global online
    global inputs
    global errout_
    global running



    out = output_var

    flags = flags
    online = True
    inputs = input_list.split("\n")

    global output_
    output_ = ""
    #printout(str(inputs))

    temp=""
    try:
        parse(code)
        if(not(running)):
            temp = """Code exited successfully.

For documentation: https://github.com/DRH001/Rattle

Try an example program which checks to see if the input is prime:
https://rattleinterpreter.pythonanywhere.com/?flags=&code=%7CF0%3A%5B1%3DF%5D-s%2B%3Es%5Bg%3C%25~%5B0%3DF%5Dg-s%3E%5D~%3D1&inputs=137""" + "\n\nRattle version " + str(version_)
        if(getError() != ""):
            temp = getError()

    except Exception as error:
        errorout("Error: " + str(error))
        if(running):
            raise(error)
        temp = getError()
        
    
    if(output_ != ""):
        if(output_[-1] == "\n"):
            output_ = output_[:-1]
        
    out[1] += output_#[:-1]
    out[2] = temp
    #print(out)
    
    if(running):
        print(out[1])
        if(temp != ""):
            print("debug: ", temp)



def run2(code, input_list=""):
    global running
    global errout_
    
    errout_ = ""
    running = True
    
    execute(code, None, input_list, ["","",""])
    
    
def run():
    global running
    global errout_
    
    errout_ = ""
    running = True
    
    code = input("Code:\n")
    input_list = input("Input:\n")
    print("Output:")
    
    
    execute(code, None, input_list, ["","",""])
    
    
    

    







