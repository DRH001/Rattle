# Rattle (version 1.6.3)
A new imperative programming language designed to have no necessary boilerplate

Note that the online interpreter has been moved to [www.drh001.com](www.drh001.com). All links to the old interpreter will now redirect to the new page.

[Click here](https://rattleinterpreter.pythonanywhere.com/) to try out some code of your own!

Want to see how to write a programming language in Rattle? Check out a [Brainf*** interpreter written in Rattle!](https://rattleinterpreter.pythonanywhere.com/?flags=&code=%5C%26%5B0%5D*555%26222%26%5C%7C!I%0A%0A%0A%0A%5B%0A%20%20g0%20P4%20I~n%0A%0A%20%20%5B62%20g2%20%2B%20s2%5D%0A%20%20%5B60%20g2%20-%20s2%5D%0A%20%20%5B43%20g1%20P2%20I~%20%2B%20r%60%20g1%20l%28~%2C%5C%29%5D%0A%20%20%5B45%20g1%20P2%20I~%20-%20r%60%20g1%20l%28~%2C%5C%29%5D%0A%20%20%5B46%20g1%20P2%20I~%20%2C%5D%0A%20%20%5B91%20g1%20P2%20I~%20%5B0%20f0%5D%5D%0A%20%20%5B93%20g1%20P2%20I~%20%5B%5E0%20f1%5D%5D%0A%20%20%5B44%20g3%20P5%20I~%20n%20r%60%20g1%20P2%20l%28~%2C%5C%29%20g5%20%2B%20s5%5D%0A%0A%20%20g4%20%2B%20s4%0A%20%20g0%20I%5E%20P4%20%5B~q%5D%0A%20%20P4g%0A%5D0%0A%0A%0A%3Bg6%20%3D%2B%20s6%20%5Bg4%20%2B%20s4%20g0%20P4%20I~%20n%20s8%20%5B91%20g6%20%2B%20s6%5D%20g8%20%5B93%20g6%20-%20s6%20%5B0%20f%5D%5D%5D0%0A%3Bg7%20%3D%2B%20s7%20%5Bg4%20-%20s4%20g0%20P4%20I~%20n%20s8%20%5B93%20g7%20%2B%20s7%5D%20g8%20%5B91%20g7%20-%20s7%20%5B0%20f%5D%5D%5D0%0A%0A%0A%3A%0Adata%20tape%20values%3A%0A0%20-%20code%0A1%20-%20code%20data%20tape%0A2%20-%20code%20pointer%0A3%20-%20input%0A4%20-%20code%20command%20index%0A5%20-%20input%20character%20index%0A6%20-%20open%20loop%20counter%0A7%20-%20close%20loop%20counter%0A8%20-%20temp&inputs=%2C-------------------------%5B%3E%2B%2B%2B%2B%5B%3E%2B%2B%3E%2B%2B%2B%3E%2B%2B%2B%3E%2B%3C%3C%3C%3C-%5D%3E%2B%3E%2B%3E-%3E%3E%2B%5B%3C%5D%3C-%5D%3E%3E.%3E---.%2B%2B%2B%2B%2B%2B%2B..%2B%2B%2B.%3E%3E.%3C-.%3C.%2B%2B%2B.------.--------.%3E%3E%2B.%3E%2B%2B.%0A!)


This interpreted language is developed to be easy to use and hard to mess up. To acheive this, all commands are a single character and their arguments follow - for example, you would simply do `+2` to add 2 to the current value.

Rattle is a very versatile language - it works on a 100-slot circular data tape, where you can move the pointer to whichever slot you want, and manipulate data in that slot and at the top of the stack at the same time. Rattle is an imperative programming language, like C++.

Basics
=

To take input or declare variables, your code simply needs the `|` character - data types are recognised automatically. If you want to take multiple inputs or create lists, you can separate them with `&`. In order to use different functions in your code, you simply have to use the following format and call functions with `fN` where N is an integer for global functions and `FN` for local functions:
            `VARIABLES (or leave blank to prompt for input) | MAIN_METHOD; GLOBAL_FUNCTION_0; GLOBAL_FUNCTION_1; ...GLOBAL_FUNCTION_N: LOCAL_FUNCTION_0: LOCAL_FUNCTION_1: ...LOCAL_FUNCTION_N`

To call commands in Rattle, you need to use one of the single-letter commands (the single character seen inside quotation marks in the long list below). Many commands have functionality without arguments, but arguments can be added by placing the argument immediately after the command (for example, `+2`, `=5`, `%3`, `p` are all valid commands). To use more than one command, simply string them together (e.g. `=5 %3 p` would set the current value to 5, take mod(3) of the value, and print the value to output `2`). Whitespace is optional, and you can even pass strings as arguments to a lot of functions.

You can also make use of arguments other than just numbers: You can use `~` to pass the value in storage at the current pointer, ``` ` ``` to pass the value at the top of the stack, and `@` to pass the value of the pointer itself.

In Rattle, there are many commands you can use:

            "+":add,                            #adds argument to top of the stack
            "-":subtract,                       #subtracts argument from top of the stack
            "*":multiply,                       #multiplies top of the stack by argument
            "/":divide,                         #divides top of the stack by argument
            "w":helloWorld,                     #prints "Hello, World!"
            "R":reformat                        #used to format data types
            "s":store,                          #stores top of the stack onto the data tape at the current pointer
            "g":get,                            #puts value at current pointer onto the top of the stack
            "<":pointerDown,                    #moves pointer down (or to the left)
            ">":pointerUp,                      #moves pointer up (or to the right)
            "P":setPointer,                     #sets pointer to argument
            "p":prnt,                           #prints item at the top of the stack
            "!":flag,                           #disables implicit output
            "c":concat,                         #concatenates value at argument's pointer in storage to the top of the stack
            "[":startLoop,                      #this is the start of a loop structure - any argument here acts as an if statement
            "]":endLoop,                        #this is the end of a loop structure - any argument here acts as a for loop
            "%":modulo,                         #takes the modulo of the top of the stack with respect to the argument
            "$":swap,                           #swaps the top of the stack with the item in storage at the current pointer
            "r":secondArgument,                 #(used internally)
            "=":topOfStackEquals,               #sets top of stack to argument
            "v":pointedValueInStorageEquals,    #sets value in storage at the pointer to argument NOTE: in versions pre-1.4, this was "_"
            "t":stringFunction,                 #(currently in development)
            ",":printCharAt,                    #prints the character of an int value
            "a":arrayInitFunctions,             #array functions (currently in development)
            "A":arrayOperations                 #array operations (currently in development)
            "m":matrixInitFunctions,            #matrix functions (currently in development)
            "S":selectFromArray,                #selects n-th item from an array
            "b":concatToPrintBuffer,            #adds argument to a buffer
            "B":printAndResetBuffer,            #prints buffer and resets buffer
            "i":printInteger,                   #prints value as int
            "q":quitProgram,                    #force-stops execution
            "I":storeInput,                     #parses and stores input
            "f":executeFunction,                #executes global functions - when used without an argument, acts as a return statement
            "d":debugIndex,                     #prints "d(arg) has been executed" - useful for debugging code
            "n":getInteger,                     #converts value to int
            "e":exponentiate,                   #exponential functions
            "F":executeLocalFunction,           #executes local functions - when used without an argument, acts as a return statement
            "l":listOperation                   #initiates and manipulates lists


New in 1.6: Local functions (and much more)! Local functions can be used to perform complex tasks without changing anything in the main data tape. For example, a local function could take the top of the stack and return a value based on whether that value is prime, without changing any pre-existing variables in memory. This makes development of larger programs significantly easier. Also new: better list/array handling, randomness, 0b and 0x conversion support.

New in 1.5: Better arguments! Now, round brackets "(", ")" can be used to pass more complex arguments to functions. Example: `=(2*4/3)` will set the top of the stack to 2.66...
                  Note that special characters can be used in the round-bracket arguments - you can use `~`,``` ` ```,`@`, etc.



Sample program
=

Here's a [sample program](https://rattleinterpreter.pythonanywhere.com/?flags=&code=%7Cf0%3B%5B1%3Df%5D-s%2B%3Es%5Bg%3C%25~%5B0%3Df%5Dg-s%3E%5D~%3D1&inputs=13) which takes the user's input and determines whether it is a prime number:

            |f0;[1=f]-s+>s[g<%~[0=f]g-s>]~=1
            
Here's the program split into its individual commands:

            | f0; [1 = f ] - s + > s [ g < %~ [0 = f ] g - s > ]~ =1
            
Going from left to right,


    | takes the user's input and parses it
     f0; calls global function 0 (which is everything after the semicolon). A local function here would work too
        [1 checks to see if the input is equal to one. If it is, then the code inside the square brackets will execute
           = sets the value at the top of the stack to zero
             f returns to the main method, the top of the stack is printed implicitly
               ] ends the if statement
                 - subtracts one from the top of the stack
                   s saves the top of the stack at the current pointer (0)
                     + adds one to the top of the stack
                       > moves the pointer right
                         s saves the top of the stack at the current pointer (1)
                           [ starts a for loop (it's a for loop because the argument, ~ is on the closing bracket
                              g gets the value at the current pointer (1)
                                < moves the pointer left
    %~ takes the modulo of the top of the stack with respect to the value in storage at the current pointer
       [0 checks to see if the result of this calculation is zero. If it is, then the code inside the square brackets will execute
           = sets the value at the top of the stack to zero
             f returns to the main method, the top of the stack is printed implicitly
               ] ends the if statement
                 g gets the value at the current pointer (0)
                   - subtracts one from the top of the stack
                     s saves the top of the stack at the current pointer (0)
                       > moves the pointer right
                         ]~ ends the for loop (it executes the number of times of the value in storage at the current pointer)
                            =1 sets the value on top of the stack to one - function 0 returns, the top of the stack is printed implicitly
                            


Upcoming releases
=



Want to see your ideas implemented? Email [rattleinterpreter@gmail.com](mailto:rattleinterpreter@gmail.com)
