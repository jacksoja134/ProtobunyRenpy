# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Emily")
define d = Character("Dad")
define f = Character("Mr.Fiskers")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene  background_solo

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show dad_sprite at left

    # These display lines of dialogue.



    d "Hey kiddo, I got you this new game."
    show girlsprite at right
    e "Oh cool! Never heard of this one before."
    show dad_sprite at left
    show girlsprite at right
    d "Try it out!"
    hide dad_sprite
    show gamebox at left
    e "...ProtoBunny...hrm..."
    e "Thanks Dad"

    scene day1cg

    e "Alright lets try this sucker out"

    scene bgblue
    show sadbunny:
        xalign 1.0
        yalign 0.0

    e "Ahw! How cute! It looks like...hm..."

    "What would you like to do with Bunny?"
################################################start choice 1
    menu:

        "Wash Bunny":
            jump choice1_wash

        "Play with Bunny":
            jump choice1_play

    label choice1_wash:

        $ menu_flag = True
        show wetbunny
        "The Bunny is washed but is angry."

        jump choice1_done



    label choice1_play:

        $ menu_flag = False

        "The Bunny is dirty but happy"

        jump choice1_done

    label choice1_done:

        # ... the game continues here.

###############################################################first choice done
scene bgblue
show sadbunny:
    xalign 1.0
    yalign 0.0
    "What would you like to do with Bunny?"
    menu:

            "Wash Bunny":
            jump choice2_wash

            "Play with Bunny":
            jump choice2_play

    label choice2_wash:

        $ menu_flag = True

        "The Bunny is washed but is angry."

        jump choice2_washdone

    label choice2_play:

        $ menu_flag = False

        "The Bunny is dirty but happy"
        e"Bunny is so cute when it's happy but, I guess I have to wash it now."

        jump choice2_playdone

    label choice2_done:

##################################################end of second choices

menu:

    "This is pretty fun!":
        jump choice3_yes

    "This is kind of lame...":
        jump choice3_no

label choice3_yes:

    $ menu_flag = True
    show dad_sprite

    d "Emily? How are you enjoying your game?"

    e "It's great Dad! Thank you!"

    d "Oh, you bet sugar plum! I thought maybe it'd make you feel better after...I mean...Glad you like it!"

    e" Feel better? What is he talking about?. "





    e "Why do I have this strange feeling i've seen this Bunny somewhere before?"

    "What would you like to do with Bunny today, Emily?"

    e "Whoa, WHAT? did this thing just say my name?"

    menu:

        "WASH BUNNY":
            jump choice3a_yes

        "PLAY WITH BUNNY":
            jump choice3a_no

    label choice3a_yes:

        $ menu_flag = True
        ##CHANGE THIS IMAGE
        show wetbunny

        "SYSTEM ERROR: Bunny does not want to take a bath right now, Emily. Bunny wants to play"
        e "UHM... okay? Is this thing broken?"
        e "DAD!"
        d "Yes, sweetheart?"
        e "How?...Where did you get this game? "
        d "I swung by Arcade Vault where we always get your games. I thought you'd like it. Actually the guy who sold it to me said he'd never seen it there before, It wasn't even in their inventory but he sold it to me anyway."
        e "Okay well this game knows my name and it's doing strange things. Look."

        scene wetbunny
        "You have given the bunny a bath and it is now clean. It does not like the water and is now unhappy."
        d " Looks like it's working fine but, if you don't like it we can bring it back tomorrow."

        e"yeah, okay. it's weird, I feel like i've played this before..."
        f "Emily, it's me, Mr. Fiskers! Don't you remember me?"
        e"Huh? What's happening? Mr. Fiskers?..."
        f" You don't remember, you took me outside to play even though, your dad warned you against it."
        e"I don't believe this"
        f"I got so excited that I ran off, You chased after me and fell, and hit your head on the sidewalk"
        e"MR. FISKERS! I REMEMBER NOW"
        f" After you fell, I stopped to see if you were still chasing me, but then suddenly everything went dark. Your Dad buried me in the back yard. I was so sad I would never get to play with you again. I'm sorry for running off. "
        e" No, Mr. Fiskers. I'm sorry for not taking better care of you, I shouldn't have let you out..."
        e" ...but now we can play every day! "
        f"Actually, Emily, I just came to say good bye. It was fun playing with you again these last ten minutes, but I need you to beat this game to set my soul free."

        "What would you like to do with Bunny?"
        menu:

                "Beat the game":
                    jump choice2_beat

                "Keep playing":
                    jump choice2_keep

        label choice2_beat:

                $ menu_flag = True

                "You have Beat the game and set Mr. Fiskers free."
                f "Thank you, Emily. I love you"
                jump choice2_playdone

        label choice2_keep:

                $ menu_flag = False

                e "But now we can play forever, and ever and ever..."

                jump choice2_playdone

        label choice2_keepdone:

label choice3a_no:

    $ menu_flag = False
    ##CHANGE THIS IMAGE
    show dirtybunny
    "SYSTEM ERROR: Bunny does not want to play right now, Emily."
    e "UHM... okay? Is this thing broken?"
    e "DAD!"
    d "Yes, sweetheart?"
    e "How?...Where did you get this game? "
    d "I swung by Arcade Vault where we always get your games. I thought you'd like it. "
    d "Actually the guy who sold it to me said he'd never seen it there before, It wasn't even in their inventory but he sold it to me anyway."
    e "Okay well this game knows my name and it's doing strange things. Look."

##insert evil bunny
    scene dirtybunny
    "You have given physical stimulation to the bunny. It is now happy but requires cleanliness."
    d " Looks like it's working fine but, if you don't like it we can bring it back tomorrow."

    jump choice3a_done



    label choice3a_done:





label choice3_no:

    e "Yikes. I have to play with the bunny so it's happy, but then I have to wash it so it's not dirty but then it gets mad. What's the deal with this game?"
d "Emily? How are you enjoying your game?"

e "Uh, it's...real swell dad..."

d "Oh, you bet sugar plum! I thought maybe it'd make you feel better after, you know..."

e" Right...Mr. Fiskers. I can't believe he's gone. "

e"Now I just have this lameo game to remind me of him."

"What do you want to do with Bunny?"

menu:

        "WASH BUNNY":
            jump choice5_yes



label choice5_yes:

        $ menu_flag = True
        ##CHANGE THIS IMAGE
        show wetbunny

        "SYSTEM ERROR: Bunny does not want to take a bath right now, Emily. Bunny wants to play"
        e "UHM... okay? Is this thing broken?"
        e "DAD!"
        d "Yes, sweetheart?"
        e "How?...Where did you get this game? "
        d "I swung by Arcade Vault where we always get your games. I thought you'd like it. Actually the guy who sold it to me said he'd never seen it there before, It wasn't even in their inventory but he sold it to me anyway."
        e "Okay well this game knows my name and it's doing strange things. Look."

        scene wetbunny
        "You have given the bunny a bath and it is now clean. It does not like the water and is now unhappy."
        d " Looks like it's working fine but, if you don't like it we can bring it back tomorrow."

        e" Yeah. Sure.  "

        f "Emily, it's me, Mr. Fiskers! "
        e"Huh? What's happening? Mr. Fiskers?..."
        f" You brought me outside to play and I ran so you would chase me. "
        e"I...I don't believe this!"
        f" You ran after me and fell. You hit your head on the sidewalk"
        e"THIS IS INSANE!"
        f" After you fell, I stopped to see if you were still chasing me, but then suddenly everything went dark. Your Dad buried me in the back yard. "
        e" Mr. Fiskers. I'm SO sorry for not taking better care of you, I shouldn't have let you out..."
        f" It's okay Emily. Because now... now we can play every day. you see my soul is trapped in this game. The only way to set me free is to beat the game but, I won't let you do that. "
        e" Mr. Fiskers, I'm not always going to play this game with you"
        f" Why? don't you miss me?"
        e"I'm sorry Mr. Fiskers"
        f"..."
        e"AAAAAAAAAAAHHHHHH!!"
##show blubackground
        "What would you like to do with Emily?"
        menu:

                "Wash Emily":
                    jump choice2_emily1

                "Play with Emily":
                    jump choice2_emily2

















        # ... the game continues here.





    # This ends the game.

return
