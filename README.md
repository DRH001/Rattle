# Rattle (version 1.4.0)
A new imperative programming language designed to have no necessary boilerplate

[Click here](https://rattleinterpreter.pythonanywhere.com/) to try out some code of your own!


This interpreted language is developed to be easy to use and hard to mess up. To acheive this, all commands are a single character and their arguments follow - for example, you would simply do `+2` to add 2 to the current value.

Rattle is a very versatile language - it works on a 100-slot circular data tape, where you can move the pointer to whichever slot you want, and manipulate data in that slot and at the top of the stack at the same time. Rattle is an imperative programming language, like C++.

Basics
=

To take input or declare variables, your code simply needs the `|` character - data types are recognised automatically. If you want to take multiple inputs or create lists, you can separate them with `&`. In order to use different functions in your code, you simply have to use the following format and call functions with `f0`, `f1`, etc.:
            `VARIABLES (or leave blank to prompt for input) | MAIN_METHOD; FUNCTION_0; FUNCTION_1; FUNCTION_2 ...`

To call commands in Rattle, you need to use one of the single-letter commands (the single character seen inside quotation marks in the long list below). Many commands have functionality without arguments, but arguments can be added by placing the argument immediately after the command (for example, `+2`, `=5`, `%3`, `p` are all valid commands). To use more than one command, simply string them together (e.g. `=5 %3 p` would set the current value to 5, take mod(3) of the value, and print the value to output `2`). Whitespace is optional.

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
            "f":executeFunction,                #executes functions - when used without an argument, acts as a return statement
            "d":debugIndex                      #prints "d(arg) has been executed" - useful for debugging code
            "n":getInteger                      #converts value to int






Sample program
=

Here's a [sample program](https://rattleinterpreter.pythonanywhere.com/?flags=&code=%7Cf0%3B%5B1%3Df%5D-s%2B%3Es%5Bg%3C%25~%5B0%3Df%5Dg-s%3E%5D~%3D1&inputs=13) which takes the user's input and determines whether it is a prime number:

            |f0;[1=f]-s+>s[g<%~[0=f]g-s>]~=1
            
Here's the program split into its individual commands:

            | f0; [1 = f ] - s + > s [ g < %~ [0 = f ] g - s > ]~ =1
            
Going from left to right,


    | takes the user's input and parses it
     f0; calls function 0 (which is everything after the semicolon)
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

Randomness

Want to see your ideas implemented? Email [rattleinterpreter@gmail.com](mailto:rattleinterpreter@gmail.com)
