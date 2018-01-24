newStory = 0

while newStory != "q":

    print("Choose a Mad Lib. 1. Pizza, 2. Christmas, or 3. Frosty the Snowman")
    story = int(input())

    # If the user enters a number higher than 3, it will prompt the user to enter a number
    # lower than 3 and restart the loop.
    if story > 3:
        print("You must enter a number from 1-3")
        continue

    # This if block is a story about pizza
    if story == 1:
        # Displays the story to the user allowing them to read through and see where each word will go
        # as they enter them into the program.
        print("Pizza was invented by a (adjective),(nationality)")
        print("chef named (name). To make a pizza, you need")
        print("to take a lump of (noun) and make a thin, round (adjective) (noun).")
        print("Then cover it with (adjective) sauce (adjective) cheese, and fresh")
        print("chopped (Plural Noun). Next you have to bake it in a very")
        print("hot (noun). When it is done, cut it into (number) (shape).")
        print("Some kids like (food) pizza the best,")
        print("but my favorite is the (food) pizza. If i could,")
        print("i would eat pizza (number) times a day!")
        print("")

        # Will prompt the user to enter each individual word to be add to the story
        adjective1 = input("Enter an adjective")
        nationality = input("Enter a nationality")
        name = input("Enter a name")
        noun = input("Enter a noun")
        adjective2 = input("Enter another adjective")
        noun2 = input("Enter another noun")
        adjective3 = input("Enter another adjective")
        adjective4 = input("Enter another adjective")
        pluralNoun = input("Enter a plural noun")
        noun3 = input("Enter another noun")
        number = int(input("Enter a number"))
        shape = input("Enter a shape")
        food = input("Enter a food")
        food2 = input("Enter another food")
        number2 = int(input("Enter another number"))

        # After entering all the words, the words will be added to the story
        # and the new story will be printed out the screen for the user to see.
        print("Pizza was invented by a",adjective1,nationality)
        print("chef named",name,". To make a pizza, you need")
        print("to take a lump of",noun,", and make a thin, round",adjective2, noun2,".")
        print("Then cover it with",adjective3,"sauce,",adjective4,"cheese, and fresh")
        print("chopped",pluralNoun,". Next you have to bake it in a very")
        print("hot",noun3,". When it is done, cut it into",number,shape,".")
        print("Some kids like",food,"pizza the best,")
        print("but my favorite is the",food2,"pizza. If i could,")
        print("i would eat pizza",number2,"times a day!")
        print("")
        newStory = input("Press enter to play again, or enter q to quit")

    # this else if block is a story about christmas.
    elif story == 2:
        print("Every (month) we (verb) to a tree (place) far away.")
        print("Not just any (adjective) farm, a (adjective) tree (place).")
        print("My dad and i (verb) onto the (noun) to (verb)")
        print("for the perfect (noun). Some people like")
        print("them (adjective) and (adjective) and some like")
        print("them (color) and fat.  We are searching for a tall")
        print("and (adjective) one! 'Over There!' I exclaim,")
        print("'Dad it's over there!' Off we (verb), saw in hand")
        print("to (verb) this year's (noun) down.")
        print("(exclamation) it's (holiday) finally!")
        print("")

        month = input("Enter a month")
        verb = input("Enter a verb")
        place = input("Enter a place")
        adjective = input("Enter an adjective")
        adjective2 = input("Enter another adjective")
        place2 = input("Enter another place")
        verb2 = input("Enter another verb")
        noun = input("Enter a noun")
        verb3 = input("Enter another verb")
        noun2 = input("Enter another noun")
        adjective3 = input("Enter another adjective")
        adjective4 = input("Enter another adjective")
        color = input("Enter a color")
        adjective5 = input("Enter another adjective")
        verb4 = input("Enter another verb")
        verb5 = input("Enter another verb")
        noun3 = input("Enter another noun")
        exclamation = input("Enter an exclamation!")
        holiday = input("Enter a holiday")

        print("Every",month,"we",verb,"to a tree",place,"far away.")
        print("Not just any",adjective,"farm, a",adjective2,"tree",place2,".")
        print("My dad and i",verb2,"onto the",noun,"to",verb3)
        print("for the perfect",noun2,". Some people like")
        print("them",adjective3,"and",adjective4,"and some like")
        print("them",color,"and fat.  We are searching for a tall")
        print("and",adjective5,"one! 'Over There!' I exclaim,")
        print("'Dad it's over there!' Off we",verb4,", saw in hand")
        print("to",verb5,"this year's",noun3,"down.")
        print(exclamation,"it's",holiday,"finally!")
        print("")
        newStory = input("Press enter to play again, or enter q to quit")
    # This else block is a the frosty the snowman song.
    else:
        print("Frosty the Snowman was a (adjective), (adjective2) soul.")
        print("With a corncob (noun) and a button nose and two eyes made out of (noun2).")
        print("Frosty the Snowman is a fairy tale they say.")
        print("He was made of (noun3) but the children know how he came to life one day.")
        print("There must have been some magic in that (adjective3) hat they found.")
        print("For when they placed it on his head he began to (verb) around.")
        print("")

        adjective = input("Enter an adjective")
        adjective2 = input("Enter another adjective")
        noun = input("Enter a noun")
        noun2 = input("Enter another noun")
        noun3 = input("Enter another noun")
        adjective3 = input("Enther another adjective")
        verb = input("Enter a verb")

        print("Frosty the Snowman was a",adjective,",",adjective2,"soul.")
        print("With a corncob",noun,"and a button nose and two eyes made out of",noun2,".")
        print("Frosty the Snowman is a fairy tale they say.")
        print("He was made of",noun3,"but the children know how he came to life one day.")
        print("There must have been some magic in that",adjective3,"hat they found.")
        print("For when they placed it on his head he began to,",verb,"around.")
        print("")
        newStory = input("Press enter to play again, or enter q to quit")



