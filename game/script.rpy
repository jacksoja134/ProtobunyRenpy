# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Emily")
define d = Character("Dad")
define f = Character("Mr.Fiskers")
define m = Character("Mom")
define b = Character("Boy")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    scene  title_screen

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show dad_sprite at left

    # These display lines of dialogue.

    d "Hey kiddo, I got you this new game."
    play music "sounds/doopbedoop.mp3"
    show girlsprite at right
    e "Oh cool! Never heard of this one before."
    show dad_sprite at left
    show girlsprite at right
    d "Try it out!"
    hide dad_sprite
    show gamebox at left
    e "...ProtoBunny...hrm..."
    e "Thanks Dad"

    show day1cg2:



    e "Alright lets try this sucker out"

    scene bgblue2
    show sadbunny at right:
        yalign 0.5


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
        show wetbunny2 at top
        "The Bunny is washed but is angry."

        jump choice1_done



    label choice1_play:

        $ menu_flag = False
        scene dirtybunny2
        "The Bunny is dirty but happy"

        jump choice1_done

    label choice1_done:

        ##### ... the game continues here.

scene bgblue2
show sadbunny:
    xalign 1.0
    yalign 0.5


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
    show day1cg2
    e "It's great Dad! Thank you!"

    scene bgblue2
    show dad_sprite
    show sadbunny at right:
        yalign 0.5
    d "Oh, you bet sugar plum! I thought maybe it'd make you feel better after...I mean...Glad you like it!"

    show day1cg2
    hide dad_sprite
    e" Feel better? What is he talking about?. "





    e "Why do I have this strange feeling i've seen this Bunny somewhere before?"
    scene bgblue2
    show sadbunny
    "What would you like to do with Bunny today, Emily?"
    scene day1cg2
    e "Whoa, WHAT? did this thing just say my name?"

    menu:

        "WASH BUNNY":
            jump choice3a_yes

        ##"PLAY WITH BUNNY":
            jump choice3a_no

    label choice3a_yes:

        $ menu_flag = True
        ##CHANGE THIS IMAGE

        scene bgblue2
        show sadbunny at right
        "SYSTEM ERROR: Bunny does not want to take a bath right now, Emily. Bunny wants to play"
        e "UHM... okay? Is this thing broken?"
        scene day1cg2
        e "DAD!"
        show dad_sprite
        d "Yes, sweetheart?"
        scene bgblue2
        show sadbunny at right:
           yalign 0.5

        show girlsprite at left
        e "How?...Where did you get this game? "
        show dad_sprite at right
        d "I swung by Arcade Vault where we always get your games. I thought you'd like it. Actually the guy who sold it to me said he'd never seen it there before, It wasn't even in their inventory but he sold it to me anyway."
        e "Okay well this game knows my name and it's doing strange things. Look."

        scene wetbunny2
        "You have given the bunny a bath and it is now clean. It does not like the water and is now unhappy."
        show dad_sprite at left
        d " Looks like it's working fine but, if you don't like it we can bring it back tomorrow."
        show girlsprite at right
        e"yeah, okay. it's weird, I feel like i've played this before..."
        scene bgblue2
        show sadbunny
        f "Emily, it's me, Mr. Fiskers! Don't you remember me?"
        scene day1cg2
        e"Huh? What's happening? Mr. Fiskers?..."
        scene bgblue2
        show sadbunny
        f" You don't remember, you took me outside to play even though, your dad warned you against it."
        show girlsprite at left
        e"I don't believe this"
        show sadbunny at right
        f"I got so excited that I ran off, You chased after me and fell, and hit your head on the sidewalk"
        e"MR. FISKERS! I REMEMBER NOW"
        f" After you fell, I stopped to see if you were still chasing me, but then suddenly everything went dark. Your Dad buried me in the back yard. I was so sad I would never get to play with you again. I'm sorry for running off. "
        e" No, Mr. Fiskers. I'm sorry for not taking better care of you, I shouldn't have let you out..."
        e" ...but now we can play every day! "
        f"Actually, Emily, I just came to say good bye. It was fun playing with you again these last ten minutes, but I need you to beat this game to set my soul free."
        scene bgblue2
        show sadbunny
        "What would you like to do with Bunny?"
        menu:

                "Beat the game":
                    jump choice2_beat

                "Keep playing":
                    jump choice2_keep

        label choice2_beat:

                $ menu_flag = True
                scene bgblue2
                "You have Beat the game and set Mr. Fiskers free."
                f "Thank you, Emily. I love you"
                jump choice2_playdone

        label choice2_keep:

                $ menu_flag = False
                scene goodendcg2
                e "But now we can play forever, and ever and ever..."

                jump choice2_playdone

        label choice2_keepdone:

label choice3a_no:

    $ menu_flag = False
    ##CHANGE THIS IMAGE
    scene bgblue
    show sadbunny at right
    "SYSTEM ERROR: Bunny does not want to play right now, Emily."
    scene day1cg2
    e "UHM... okay?? Is this thing broken?"
    scene bgblue
    e "DAD!"
    show dad_sprite at right
    d "Yes, sweetheart?"
    show girlsprite at left
    e "How?...Where did you get this game? "
    d "I swung by Arcade Vault where we always get your games. I thought you'd like it. "
    d "Actually the guy who sold it to me said he'd never seen it there before, It wasn't even in their inventory but he sold it to me anyway."
    e "Okay well this game knows my name and it's doing strange things. Look."


##insert evil bunny
    scene dirtybunny2
    "You have given physical stimulation to the bunny. It is now happy but requires cleanliness."
    d " Looks like it's working fine but, if you don't like it we can bring it back tomorrow."

    jump choice3a_done



    label choice3a_done:





label choice3_no:

    $menu_flag = False
    scene day1cg2

    e "Yikes. I have to play with the bunny so it's happy, but then I have to wash it so it's not dirty but then it gets mad. What's the deal with this game?"
    show dad_sprite
    d "Emily? How are you enjoying your game?"
    hide dad_sprite
    e "Uh, it's...real swell dad...thanks."
    show dad_sprite
    d "Oh, you bet sugar plum! I thought maybe it'd make you feel better after, you know..."
    hide dad_sprite
    e" Right...Mr. Fiskers. I can't believe he's gone. "

    e"Now I just have this lameo game to remind me of him."
    scene bgblue2
    show sadbunny
    "What do you want to do with Bunny?"

menu:

        "WASH BUNNY":
            jump choice5_yes

            $ menu_flag = True

label choice5_yes:
            jump choice5_done
label choice5_done:

        scene bgblue2
        show sadbunny at right


        "SYSTEM ERROR: Bunny does not want to take a bath right now, Emily. Bunny wants to play"
        scene day1cg2
        e "UHM... did this busted thing just say my name?"
        e "DAD!"
        show dad_sprite
        d "Yes, sweetheart?"
        hide dad_sprite
        e "How?...Where did you get this game? "



        show dad_sprite at left
        d "I swung by Arcade Vault where we always get your games. I thought you'd like it. Actually the guy who sold it to me said he'd never seen it there before, It wasn't even in their inventory but he sold it to me anyway."
        hide dad_sprite
        e "Okay well this game knows my name and it's doing strange things. Look."

        scene wetbunny2
        "You have given the bunny a bath and it is now clean. It does not like the water and is now unhappy."
        show dad_sprite
        d " Looks like it's working fine but, if you don't like it we can bring it back tomorrow."
        show girlsprite
        e " Yeah. Sure."

jump choice3_done
label choice3_done:
        scene bgblue2
        show evilbunny
        f "Emily, it's me, Mr. Fiskers! "
        scene day1cg2
        e"Huh? What's happening? Mr. Fiskers?..."
        scene bgblue2
        show evilbunny at right
        f" You brought me outside to play and I ran so you would chase me. "
        show girlsprite at left
        e"I...I don't believe this!"
        hide girlsprite
        show evilbunny
        f" You ran after me and fell. You hit your head on the sidewalk"
        scene day1cg2
        e"THIS IS INSANE!"
        scene bgblue2
        show evilbunny
        f" After you fell, I stopped to see if you were still chasing me, but then suddenly everything went dark. Your Dad buried me in the back yard. "
        show girlsprite
        e" Mr. Fiskers. I'm SO sorry for not taking better care of you, I shouldn't have let you out..."
        hide girlsprite
        f" It's okay Emily. Because now... now we can play every day. you see my soul is trapped in this game. The only way to set me free is to beat the game but, I won't let you do that. "
        e" Mr. Fiskers, I'm not always going to play this game with you"
        f" Why? don't you miss me?"
        scene day1cg2
        e"I'm sorry Mr. Fiskers"
        scene bgblue2
        show evilbunny
        f"..."
        hide evilbunny
        show badendcg2


        e"AAAAAAAAAAAHHHHHH!!"

        scene bgblue2



        b"OH COOL! A BUNNY GAME! Thanks Mom!"
        m"Go ahead and put it in, dear."
        "What would you like to do with Emily?"
        #menu:

        #        "Wash Emily":
        #            jump choice2_emily1

        #        "Play with Emily":
        #            jump choice2_emily2

















        # ... the game continues here.





    # This ends the game.

return
