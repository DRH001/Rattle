# Rattle (version 1.3.0)
A new imperative programming language designed to have no necessary boilerplate

[Click here](https://rattleinterpreter.pythonanywhere.com/){:target="_blank"} to try out some code of your own!

What's New
=

Rattle has now officially been released! Rattle is now an imperative language - it's now actually useful for normal programming!

Version 1.2: List and array functions have been improved (see documentation). Improved utility for ASCII codes.

Version 1.1.1-1.1.5: small bug fixes and optimizations

In version 1.1.0, loops work slightly differently (they now work more like how loops work in normal languages - see the changelog for more details)

Description
=

This interpreted language is developed to be easy to use and hard to mess up. To acheive this, all commands are a single character and their arguments follow - for example, you would do `+2` to add 2 to the current value.

Rattle is a very versatile language - it works on a circular data tape, where you can move the pointer to whichever slot you want, and manipulate data in that slot and at the top of the stack at the same time. Rattle is an imperative programming language, like C++.

To take input, your code simply needs the | character - data types are recognised automatically. In order to use different functions in your code, you simply have to use the following format:
            `MAIN_METHOD; FUNCTION_0; FUNCTION_1; FUNCTION_2 ...`

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
            "_":pointedValueInStorageEquals,    #sets value in storage at the pointer to argument
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

You can also make use of arguments other than just numbers: You can use ~ to pass the value in storage at the current pointer, \` to pass the value at the top of the stack, and @ to pass the value of the pointer itself.




Sample program
=

Here's a [sample program](https://tio.run/##7T1rd9u2kt/1KxBqE4u2JIty0iRqnGeTsznnbtuTZO/9oCgtJUISbyhS4SOOu9789e4MHiQAgpQUJ9tt9/reOhYeA2BmMC8MoO1lvk7is9@7ZHA8IIskCOPVhBT5cnAPSzqO43SepdTPaUCSmLxZF@RJsSLeGRndm9y@Nzm7S8aj8ajTeewXACmdkB/8OKRR5/FHmmZhEk@INxwNzxgg@MF/8oQEyaRD4If9CugcQC6LeJFDhxukqql@bfz3lPhlIwIwYMBk4@fhwo@iS5LlSQotYuKnqX9Jwphs6CZJL6EoIJvkIyX5mpJtEsY5TbE7fozpp5x89KOCVoPQKKMADVa8oXGePSJJChWXc0r@WWQ5iZNcq30wGJCLdbhYkwUOvsiJn5kwSI9BDnNSZGKOq2Xkrx65Ai34@0MRLt6TbZqsUn@TKeh5Ef72262nxW@/Xd14OV2dvPLm2c2z6Wg@mr8bzVY378CfHv75dOaNRiTMWAdsTwbEj2C1MSDpI40uJxqs7HXmvfay8c9nKlCvAjougbJpXCDoNY2ihFwkaRSwwqupd/5hdmOQnTzMpqsHNz9PR@fbD7PVIHs4@3zubcliTRfvM8R3RgEDSyDMtsgR1DYNN5Ss83ybTU5PgfPoKomWQ8Da4j39tFj78YoOF8nm9ENBM6R5dnrn7nfe3dMwG@Rr@BUXmzlNB/6AQRLTGX2YTbezETAYhVGh2eSwIb4b3z0bn4abbcRIB9DzFBh7sPEX6zAWowCp80PBjs9GpxmDO4DeA0Fn0gN@ohNytUWU/PjTG@BxBC6q@2ROFz4yDXIrR92KAkNt/TSDHXmxpsDnPjA79EbOpJttfumyWT69Nb9VLJd@lNwiwDmr0WK8OMserjz273R@e35nNp7fgf/dBqqPvxhjY@/e@N7t06TIYXaDOR/yS/@tuH5Oc9yonEs4qTkzUZAxV8vR98B5y5nGeMuS72BXSgASgZdJIXdowQSGHwQo72A/LrHdcmQTO8avqwxGG50Aj8FID44/42goH65ejh/UygkZPCRkCQMmaehHpJdEwYQDGQgorCl0mX1@sEL4xBXCgP16AZAZzbkw4OTfoBACClBY2RJFHnLGFUiYcLXm0mntf0Qhc0mujjLOCrDtcPkXfoz9ozwELuTgsr4USbdQbvmwS4G1fJgx6YG4ugijyJCzC6YMKkGL4pVxIzAjMG5@uQURCrIf9AqoEpKtkyIKYK71mYBMWCQxcDuNEeLaT4MBEiQQK70I8zXOTiAB8JdyEZyjME1iFPqIhxCkbIazr9q6YlnkLRsVf@gnHzffhLy9tU1AMidvb43fqoPiQi5pdmvcJxTQcluHCCUMGSuQpGTqQEOnT6Cpw4Hxj7dnbDjYxs8nSBdUSPBfnADEhQ@IgQ2UAj@AZiQ9OlwNydvYRf75UCAU1GsbPwVx2XP6Ry5AAIQiz4LuwTXHOCUhP2NG4QsgQBFHNMsYWoOkmEeMIzbDcuHvAOe8IuhXuyCCrrDdYXch0eFfoNX8kqTIU0DsHD8XGf5@NfaQVCB2SBqCEbBkHAfCAEc1Jw77jq3LcXKQD45zhb0HsA/45440AXBDwU9Al5x5ekgDV1F6qyiZw55B2aZ@lvo/UwtTugWeVEu4MHqSP48DtThPtj8tX6MsU0vRcvBXVC0SZoJaFCXJ9llSlMVdpRxAptr4iyJNQXs8SzYbYKuXcUA/mbCMqS1408xs9rcwy23tniXbS3MRNHiCW1IrprDFoHilFoL18QKsD23BwAD5U5DB@qJFy/FOEtimvwMJ2ftw@yZRS2gcvBDAzfmFsayxTUUMUcNVfQIvLPU2yCqatT7bkALj23SDAY2ck4GnVmjTgNopFxaWNWDldNa/9v9npIv6HG0D3LJRuAGRDvsbBNIQ9/FS0FBbLAzehFahhZQVvvDB0K3qDALWG3CaV4tvwg@04Oq4W24vvUjsxLJQ2vXys9jTONJoRo6JNGIrCVA2lbusmpWyl5RCuZOg6MdEWIJif2gLlXtGK1T2l7F69kuRV1D9JhX@iEoYOSzHQZDER6jp4wDkPU3TBDQKp@yFjTePjo4qE@IKher3kshe@dd4yH7kxx@/J9Mc7Us0lGBRBXdlmFbjDg/qNo4r5o4BJheVOOXqe@N/Qk5Dx4S5WdmMOUxo6G6LbM17MuuyL00PKANF1JfmwpVk32WYouUjNWi/8iS4bszXaVKs1ry45w7Jy6XQwSEaNs4VaGi2HrRT0EJhVlQmzaiQOyX6pIbkJwRxEWa0j2qcwVb2wtI2M@Z7CpvcF6arGBpbs6oNBWc54CYFaHeuwXBgVPkbVO15iJPrhUNKPNaFtU0LAHIRLqiLxmW2pQu0LBc@zm@ERRxSBhhHuoVISFR8HBhyiOeJTzlo7sjVeYQzF7OKz5lxPAR4kb@gPYc4fcfhzbkMlC2ybRTmPed7qBROdIiigTeC3WewYrjsASkkjoTKL2tFC6ySgK8cF/fw@TkYFUrz2m4WdFcaVLYfbMOWnvXRtLblB7Eys7k3s2JJWYp18kwk9KqJuFptSvMijevIQRIipyECq746ZBiVNYFRj96@PTLGrS2/@lCt4@1bpy8x2vfcGoBOHa26DOOij3OE@AfM9K3HpF8XXYoBM/wyxbMF65b5ELAVS7eh7DlW5W6eXlYDNy1GkOiWQg/EHgXPvg17GuzKe6CLnuPDAA45QXu5h2DcOmLkVJkszHru1PEdnZ3Qct7mk8aeCLhjVnhDf7sF9dpjrdyGtWND636KaKxyGnKG17aXqg9yM5izrmGpjiFlQLd5KDuibEja@lkmGUq1nLJK2niTyUxUou@MZE4xZMEQULZ3laWXhdNwppg@@LG2q3XUahjgYpdJoZxtecCbaxMcfIoKaWRPMEcMipQwvVF9HPHHCfGs5Kn66pOWFgXUgEOnGHhs0n3eza01FwaIrYsYytXH6ZrSrU946xLBsmO/HMQ1NEUXlZ2s5LbJUKllkpDXIp1lwwnpZhf@ln0GgwV0ahTGIGYiX3purLdGvS5DWSEN3p6AVa2pa@K3WzJkWdLWn7NkmmyY7iXhZpuARbul6fKXhbBkQfgJQ/gNNhGGKDd8lYqeq@3tCh9gkkXgRlts6QcEub/EssJl9SlnUwsEhZNt8E9qXCaVkKXxTWYLWri9ai@W@VAs/4TcsWgwzl/OzyKMimgNUAUNyQ9hwMIcwB8Ys4A/QeZ/CjFoFnOD6JFTl9vzlPrv1VUonMbCjlx3AK9h4B64DKxBrvH64l/gMN0@pflCM3sUBaksCCpU5@AG6kerpeA4w3@Cl6O2VuQq08UaAew2RkeGXYy9vMS9rwZgtkmWhfOIgseD0sIZeeOz23e@u3vv/udfH99692jodMkt3MMpzZhj4IM5CtKSWSZokPLgXCWkY4p7MYGW4BCU/gTH8DsWfXvEPApZxRFd6n/dReOem8@KeDiJNIp9V8d2nMBqUdpDK3WRrqkQxaBS82IfnW/E@FjRZmoKONOBhxqGdTrROynA1NZ1K5Rbhb0SH8dIALcuDJRfSGt1n4tVHhT7sgSMtMhQqY5RVmkmv8/85UWl9Uof4B3zAaBeQTtvDb8r1ftON6grh7t0knWM2zzycsxH@435yDrmeOeg4/qocmgc5YbhBNRMKJzi0DJFfarLKPFzBKgzY53xqi4oBKpu7m4ry5y66b/4ehjE1vxzvT1OQzDcVHDZzKLOFCC/2oGYTpPZ7bG9mxjTtQwIXgLiHc1WhqJJl591Zaw7j27IMJjONQ1ehiGEONDdfga044Yozpd/cPfyHjRbxLDCAE6fHcwI8hvsKUX0D@ECJdB/abCdE2fiB0FfLxw4k6yY56jpjJpjZyJOmC6NmlNnEoQfw4Aa5RfOhJ0q/wMPlY26V85Enkj0SReRPmI/YAni2ac4/eLxlyBc8RgOO4Lqeeew9D4Zn/PDjT45O2dbwCUDdhQ9p1FywUgV0NwPI6D0HDQ0CFQ0VPHggwHM9AllsHCMeBnzXDkT0KdG4QNnIjjuh@QiNioflpX/uTWqfoYxaP4zrzXqttAtjc2RbjgTVJZG6cKZ8PM1o3yKawDL6m9JYg49cyag6iwVN4GsSVBEiVH@bwALrG2jNMUViHAp0@VG/bkzqbbw8w8FyEyjxS8SPcHfMWz4Mn7N5Ya1cY4LQiLL4LNR30ekAbBnYJs9MefiA39jpPdlHJaxe3OAJ6LNT2Cx@7xBl59@JmUJ5nhgksiSpYvAdBYsxpbo29fZACKx9lPbeK8RfxFd5C/AZWBxaKPBXJL2TfJzZQ4ajZ6KZT@Jg1dgo9kbhaLRS8D1qlb7wZl8KMJcWNlG5UuxF15i8MaoWwIjfaKLIqcNNAlAGmDaT3UsVPMg8Oe/FTOcRRhUYcU@uGBMOeCin0jZfeK4QhZrjaf4YeZWitP0Njn5zDwj9EHDOAsxT4D8/T9AeOAxOD@0BKdtBbLiEe8Pqi3kNXnITsoLWBq6qDHMrGDQ@MBdFlBn5q2SOZSk2FrPcMLBWXwEoA1IOKRDdsDvAx0X7IRWxJIxz0m4KtAWK46WRywAjxKN5xtxm5qi748yU/ha5XDMTjRIVuKPEUk3HNsP5HaeDdYP/3acFracDTae1X2740HtZLZ@LFaaiaoWduR0JiCRiI5azYrRqtCeQTtLMR7qp2zleNr@aYwIvGCuCA8LWHA0NRY@c@uu@j7dpk1Dz2Q8f@ZYrNyAVviteUHfdmg5rHT5Rg2B75ZoCMcthkTMDl37OSffCcNtsu0NlEC7ZBpxYspzlKARYx5e6Fo8kfohtMZNtbBnGxLrAb8qOqpBnaknBNpu/EowW/44PKjWHFjraJBtxLUwxjfbZSbfG9vewr5tx@/NsS77eFZxZokbXm83uvtvp04TXhp7NYYavyDc@C1CjnZS2DCyczvrgkZMNAC1QXYpHaWDhZR9K03c9j1SE2UWf1hIMNeIqPNi9ICB5A0bxyIWukKIit1pDVI3gmuSuTVJa6VQ6yqtwxlLLg84wMqkad4weQ/@C/tWsS0jBKqtYTlSESkjPFVTMTMHhA9MQozMVu4MgEnIh4IWVF9rU/4P2o@VRd@rIliSG@WxINagzU7WPiZf0FianYHjmnFL4fsr0JYblNsSjjgJqvv/fZ7aH5bxG4yPsLSOYj5YqhYdpxuGCrAldMhC5vpn8tCH/EbThEW0q/YsklD24IECoaMDugg3mO2bJugABG4bHBmbEIBEXpaSJYoJmihmmJqjPvgKVOQNdpSjXUBK7UwXEXWCcXtHNy43uTSBPNUE2iCRmBSABhitdaV5oXcaa52QDnt0OtM68UikpVtFeDYbIATS4Xykex5GEieMJBqaot7IDpEhUPVYmnQs@Ra6RcUwDzy4lgZGlKzKyrmADGV16H1v5LoHzObUGx0f9@Yn3kAsCOZ3XCvrCAyJLbAbOyIoOsI8Y/G34VBoUzNO7m2ZHk2pAgB9MmD7cqaQkq/zqxKzhjp7RorWh21HC5FIhdjW9H9cSxWn5BKpywr6/D4MT3j76KehL8@1OPa5tdbFzPGYvGNp9mnFQkI8/nt1scZRNpE8WSj7P9rd/4YBwEJxtVOf/KOp16jeZW2Zp3nyaIV@jEBPPNe14NUPJEJFrmGZgFcGTDLCstCBcighlTqOFhbiZs1E71pDO8MJ7nQVcp2fN28PzRBVRIbeBMlTLU4GysUK5Uc2USZclMXISlwt92za1lu1LmF9m2UPdi97wJZdoyyP@Iul8w98cqeSh0Upj0qp08cs0LG65pFg/T4puxjNRaKMaJ9g6mZ7B19PjL8elk7PxXwNLNn3k95RS/Gx4fdU4FfTkuKgRXIWNjw@LxErqsPDcKv22he9LX2@KoaPvxTDx3tg@FjlYAXLLMYtUCwSfoW5hhPtK9mKYEjn1A@IvK8nY6zqiXqXgdMogn9yfOH9qaZ@Yt/Lrd8OhU0wtp3uW4rsJsONmtKQR7dQO9MUv0X1mse8enuZgKLY9d0MrzVa1yPu6rL8cYmiNtTsDcjgzWugxrCgKjztskpMPFVsV54OqkjCe8yZdpG52NpwYGvHmIJlOGRN6R6N9gImKQlAsPj7980EJVGnqcd6QoJ5ScMwtHX/uZ4CsWMSjRNpzo4wJ2T38BVq4EFuOz0CaLEfRbDl16PJqIEkg31Jcv/@9WkyaiHJ4FCSwITqdKgOxq2yw7jeb2xwFa3VOCJDwt0d4qm4IY012cUM3qwupUwJZGOMpr7NIvyLbjFWqSBuO1vZryXoxOJtVDmnBOUQQXi2qSKoyPilGqgLY1reW@GplB0RC7tBUC1jeiBHGV6WDxegXkV@pUDM859ekB4/NwUdzK4BYz/@PoX6wAC7FuS2XQttsDhsNxnqJxC4Tn4Ir65UudGc1bSN5EsrX@ythVrddR5j00jDb2BwU0akfWibBwvFDUGoIgOiMyjDcFrE/HLGUSaPw8sOoaAXX2kSKxoXqEAxY8PckGhIyUy9HjvXfufyG1IhjuDjmftHmmL2drisHtI45HZpHY1t12kPgGxJhrQfhu86X246ntbuPDZNpqNks1bDq9Fl8zDTAsntdruqPtEkAiYTsFv9Ms2KG/zzFJ@CyFn0Vsks6DQmo6lxjLr2EEMqLFzXCSy8T4o4DyNuH0cJu5kuplJrL47k2jLaWTKm9Qx4ryz3toY7NK6Wk9dw@UvQtY6bvxZypCQo9ze74kHmfsaFeZYXy6WiBEHsY4hNpM5g@DzBe5SwWpuS2oP/6@fTru0ew19qW1zvwPZg1rAc4O5s/afYQX8SPFqN2OYCngbGU0BVI6HMG7OaCOyVAXY/mVUzSwfvGGv2LnnXV9qw17f4qz5oCbEbycwsXIb8AnjNdrIbw7anNNr1t1XlN7yqYbkLsbdB/nWNgl25bppxIw@y8c0VPMXe43KX2UXCO6Sz5dQZ9qF6YCysafWekUzA/9VRb/HZB9N3S7sOO2@vr257/IrH/OIcU7ekPe1@FU7y8x81yc/KJGtXKGrTfPxHTfOxMk1528J1jbv41e2frzlDkKbC@an5pm5T8tiX6PZUeiyq4aIrn8YMRvVszWtL99qXHCgGrG1sClPfnnulW3aV@8LqmIrbUJt7tzwpTKmR9dQ1XjXQhmB5QzYnZbcp0IouTEKoGKO9KU9GcL/e1jh4cDIwXltoSBstfUSDFM2tJYGbaGdogEoBtK@wT5y3sePW9pdOrErCXzNhUKf/NY2w82sCuI4S@Wvi4Uv01F8TEweqwv9bSGhVpn8iPXptRLRnszd3/Zf@/Wr69w/e0fr0rwnrW6n4F/JxgWY9b6SOsMucB52/8y6yqtq/AtSZy4ICmXo8cZOcuYdlf@zKTtSAj1sT1pr7eaNOmxRp6zjaPx0S2svjDlsuIV6b5fgvM7SxqCmnIw6UA85AebPczH7YDWOPqIo9orEjGtJMQbrZvsY3eRryHXYnjDQ@d4VgbSSpj1hmY@xOZWkfqX4KqN91tm4q3qS6h2k/oNZfa1VfnBS5XxULsYHNS9QH7We2g5OUjPoimhcnpDwe3pVN3LZHR2RHppUlla3lsreyqJ1H3aR9mhYms2aFWdqVW5mfo6q3zdW7Dn6WdeUhN39UuXoABxXyhCyjcHua4vuT@GbjPIxP1yDte@zW@Hv8RoILfJeVZV4AlTLq9vFKQbLBd3bkq9He@DvoyZ4BZ8V48tcnC59mfkqydbjM5dvK1bV3lTdUemsZCOzZQMEsUPiFeQwMiiVR6zr5CzvyFRbrmu@lmBEKafXmTS6KkppcextARSTxPZmKJ94DWLJrHpQ9chTReJWvVc63Za8BjF/4u6NZ9aq6wPY8yfNkY8mIJv7Y1qf8ugdgvCRmlYGc0EAIlPKuiUxe5Of/MDVvqDcZGfWjIXkeZbwX1/Xq2FJcwcejTCqZanj2sqmcH@1zsDhPdqYHsxlgQ7E6fHAlCCY87aiPL7ixt6X6ZD8@sj2EvddDR7oA7pTfRcDIYLz9C8M/UZ614QlJ5bN/2usuan@tNbMHrQ/46c/wVM/pPcG9VsLTI@1yRro5w@7SaE@SKtOpbacG8cdfUbboyba3SjWRPy1HNSDVZz9W78iJ7zXAx8PGXIOqS1F0pHUpXHOH@WJNzKMzrDLeeG5Ie6vQbX@1k0FRH@jkI7q2S6dKtf3sT5vxqH7H15o1t2uppjHDt4fuT2uoHLXhcfQvPGp4tLri9ofgSsC6pPl/gcuGJbfjVD5XaLy/I/LxixhMrRCf7O4owgLz7yuDW@TlXS4i1DpoHOHTo8L@Ohkcn97sk1evnr9gaob6aYRfHhVQRJyP10I3/qfTDT5dKv7AFwb4VcxFEhWb@DRNLvrEB4AgM0/BG8Zhik3tqywa1FVN4zSbOl0xbY6MTuOLbfLBMVMTNKQ71mEor0BWb@7qv5qTYy3PGxmpoFaX6Ab@7PzqCgOJ7VkNwjnTHlI6xJtoGPgAV8jUpOVryvvfCNAdV1v6qfYGlIpqdh@OvV0nv@CFvzGKooQZFFhWvYtrS8pkth7L2qD49RHsi3pYGgi@VolfvMNulZLyUlqV9KRAGwtwjxRwAZDFBotxRpkHgqUltJiG8soRQhXZJFzEtbgp0FP3VMxuMrvMYpzv8RUp1/lOmV3vaqqhXM/pi1uOcvnl3VBTdBgpZY2sWvpDfFUihiieU224L6A0F8ETxyG2@6qdHfHo1llhUNyYWcukzNbKxZt2t5G3l1rSfLO84Sizoad@SKL63/r7aw33BsT3aOgbFV8aS2L05JhuauPG1msiX@F9YWPllX1iIAefWejybwLDb3lkQY9HFS7EM3N7BSPqAUyRGZ7viD8oGxpxonf7X7xEYQYkGm9S1A/ZOnVhrzzEV1diTTlvjTNsyOIde7fv3r539t3tuzWVU12GZA/@1eewd9DYIvZUxNf95yQK3tiD7MqD7pqzWX2atbvXh0vMfb5DosGLrn21wwE3tXZexTpkbofMzzrHFsm6zxz2Gbt2l@/Aq2nfik7WHNx6iFvn2drLvPICr3pdugyJ4df@6XeAyRTNKRFtK6//Mi@EWU74bUMxu@WOt23EN99m@Nr6TNyIVa7GYbl4rQYDdOwLRXm8DlGFubyshU3Kii8JBRnrb9B648oqN1J@5f1e0@Iud113JU8n2DM92FudM5sW/6JJJcbIAoX43Ya6bOwo38vRwae3nvGvL3Ic5@3vV2Q5@p5M8WtnlmSGMVBygk99kSlZkQfk5mcyHYm6Fat9SGafybn3O/sSTgWa/HM6QVukw7@0UBaCuv/9/v27/wM) which takes the user's input and determines whether it is a prime number:

            |f0;[1=f]-s+>s[g<%~[0=f]g-s>]~=1
            
In a more expanded, human-readable form, this looks like this:

            | f0; [1 = f ]  - s + > s  [ g < %~  [0 = f ]  g - s > ]~ =1
            
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

Raising exceptions!

Randomness

Want to see your ideas implemented? Email [rattleinterpreter@gmail.com](mailto:rattleinterpreter@gmail.com)
