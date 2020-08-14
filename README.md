# DENSE
A new esoteric programming language

`DENSE` is just a placeholder name - suggestions would be appreciated!

This language uses a very particular format:

Commands are single characters. Any integers (or \` ~ & ^) are arguments. All commands are called with their arguments - it is possible to call a command with no arguments, as well (some may not use arguments, others may default to a certain argument if none is given). You may also hard-code input or take input normally: if your code is preceded by either `input|` or `|`, respectively. If input is used, the program will implicitly print the top of the stack as the program finishes. As this is a work-in-progress, much better explanations for all of the commands are coming soon. 
            
A few example programs using some of the existing commands:

            `3.2|+3R1` which outputs `6`
            
            `[+p]10` which outputs the numbers 1 through 10
            
            `w` which outputs `Hello, World!`
            
            `[[+p]2++p]3` which outputs `1 2 4 5 6 8 9 10 12` (but with newlines instead of spaces)
            
            
Note: as of right now, you must run this language in python. You must run the interpreter code, then you can call `parse("[code]")` with your code replacing `[code]`

A more in-depth explanation of the list of commands and accepted formatting is coming soon..... for now, you can make use of some of the most basic functions:

            "+":add,
            "-":subtract,
            "*":multiply,
            "/":divide,
            "w":helloWorld,
            "R":reformat, #see interpreter for more info
            "s":store,
            "g":get,
            "<":pointerDown,
            ">":pointerUp,
            "P":setPointer,
            "p":prnt,
            "!":flag,
            "c":concat,
            "[":startLoop, #arguments for this act as an if statement (comparing the top of the stack to the argument)
            "]":endLoop, #arguments for this simply loop n times
            "%":modulo,
            "$":swap,
            "r":secondArgument,
            "=":topOfStackEquals,
            "_":pointedValueInStorageEquals,
            "t":stringFunction,
            ",":printCharAt,
            "a":arrayInitFunctions, #see arrayInitFunctions in the interpreter for more info
            "A":arrayOperations, #see arrayOperations in the interpreter for more info
            "m":matrixInitFunctions #as of right now, this has no function
