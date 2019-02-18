speech = ""
name = input("Tell Aunty your name young one...\n")

while speech != 'I love you aunty, I have to go now':
    speech = input(f"Come {name} speak to Aunty, tell her your darkest secrets\n")

    if speech == speech.lower():
        print ('WHAT? SPEAK UP!')

    elif speech == speech.upper():
        print ('YOU ARE VERY RUDE!')

    elif speech == speech and speech != 'I love you aunty, I have to go now':
        print ('SHOW SOME RESPECT!')

    elif speech == 'I love you aunty, I have to go now':
        print ('ok. Goodbye!')
        print (f"{name} are you still there?")
        speech2 = "  "
        speech3 = "  "
        while speech2 != "" and speech3 != "":
            speech2 = input('')
            if speech2 == speech2.lower() and speech2 != "":
                print ('WHAT? SPEAK UP!')
            elif speech2 == speech2.upper() and speech2 != "":
                print ('YOU ARE VERY RUDE!')
            elif speech2 == speech2 and speech2 != "":
                print ('SHOW SOME RESPECT!')
            elif speech2 == "":
                while speech3 != "":
                    speech3 = input('')
                    if speech3 == speech3.lower() and speech3 != "":
                        print ('WHAT? SPEAK UP!')
                    elif speech3 == speech3.upper() and speech3 !="":
                        print ('YOU ARE VERY RUDE!')
                    elif speech3 == speech3 and speech3 !="":
                        print ('SHOW SOME RESPECT!')

