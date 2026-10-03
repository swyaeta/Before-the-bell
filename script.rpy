# defining all of the characters
define s = Character("sasha")
define e = Character("ethan")
define c = Character("chloe")
define v = Character("viven")
define t =Character("mrs.Carter")
define m =Character("mom")
define f =Character("ms.Aundrey")
define r =Character("Sham")

# these are for the sprites of the characters
image sasha_normal = "images/sasha_normal.png"
image sasha_sad = "images/sasha_sad.png"
image sasha_shocked ="images/sasha_shocked.png"
image sasha_angry ="images/sasha_angry.png"
image sasha_annoyed="images/sasha_annoyed.png"
image chloe_smile ="images/chloe_smile.png"
image chloe_normal="images/chloe_normal.png"
image viven_annoyed="images/viven_annoyed.png"
image viven_shocked="images/viven_shocked.png"
image viven_smug ="images/viven_smug.png"
image viven_laugh ="images/viven_laugh.png"
image msaundrey_normal="images/msaundrey_normal.png"
image msaundrey_angry="images/msaundrey_angry.png"
image mrscarter_normal="images/mrscarter_normal.png"
image mrscarter_angry="images/mrscarter_angry.png"
image mom="images/mom.png"
image ethan_smrik="images/ethan_smrik.png"
image ethan_shocked="images/ethan_shocked.png"
image ethan_annoyed="images/ethan_annoyed.png"
image sham ="normalboy.png"

# this are the background that will be used there
image bedroom ="images/bedroom.png"
image class ="images/class.png"
image hallway="images/hallway.png"
image gym="images/gym.png"
image nightroom="images/nightroom.png"

# Scene 1: Starting
label start:
    scene bedroom with fade
    m "Honey get up, I have made your fav pancakes."

    show sasha_normal at right:
        zoom 0.7
    s "yeaaa mom I'm awake and what time is it now?"

    show mom at left:
        zoom 0.7
    m "Its 8:45 honey"
    hide sasha_normal 
    hide mom

    show sasha_shocked at center:
        zoom 0.7
    s "shit!!! i'm gonna be late again and mrs.carter is gonna kill me today."
    hide sasha_shocked

    show sasha_shocked at right:
        zoom 0.7
    s "and Mommmm!!!! didn't we have pancakes monday morning??"
    show mom at left:  
        zoom 0.7
    m "What are you dreaming sasi, today is Monday."    
    m "Go freshen up again and come on down for breakfast."

    hide mom
    s "Wasn't Monday yesterday?"
    s "Shit.....I have ms.aundrey's class then."
    hide sasha_shocked

#Scene 2 : School hallway
    scene hallway with fade
    show sasha_sad at left:
        zoom 0.7
    show chloe_normal at right:
        zoom 0.7
    c "What's wrong sasi? U seem off today."
    s "Idk everything feels so weird today."
    hide chloe_normal
    hide sasha_sad

    show sham at center:
        zoom 0.6
    r "Please leave me and I'm sorry!!! I'll do it tmrw."
     
    show ethan_smrik at left :
        zoom 0.6
    e "Shutup loser!!! ms.aundrey is gonna check it today not tmrw."

    show viven_smug at right :
        zoom 0.6
    v "Yes!! You're so dead now." 
    hide viven_smug
    hide ethan_smrik

    menu:
        "Save him":
            hide sham
            show sasha_angry at center:
                zoom 0.6
            s "Stop bulling him, viven!!! "
            s "And didn't Ms.aundrey tell you yesterday to stay away from him."
            show viven_annoyed at left:
                zoom 0.6
            v "Why do you care loser!! "
            v "And ofc, you won't say anthing to ethan cuz you have a fat crush on him."
            hide sasha_angry 
            show sasha_annoyed at center:
                zoom 0.6
            show ethan_annoyed at right:
                zoom 0.6
            e "Shutup!! vivi." 
            hide viven_annoyed
            show viven_laugh at left:
                zoom 0.6   
            v "lol, he thinks you're ugly. "    
            hide viven_laugh
            hide ethan_annoyed
            show chloe_normal at left:
                zoom 0.6
            c "let's go sasha" 
            show sham at right:
                zoom 0.6
            r "Thank you sasha"
            hide chloe_normal
            s "I can't save you everyday, sham."
            s"Maybe you should inform Ms.aundrey, didn't she give them last warning yesterday?"
            r "What? No, The twins were absent yesterday."
            r "I'll go home and tell my parents today."
            hide sham
            hide sasha_annoyed
            show sasha_shocked at center:
                zoom 0.7
            s "Absent??"    
            hide sasha_shocked
            "Good job!! "


        "Leave them":
            hide sham
            show sasha_annoyed at left:
                zoom 0.6
            s "The twins were warned yesterday and they have started again today"
            show chloe_normal at right:
                zoom 0.6    
            c "What are you saying ? It was their birthday yesterday and they were absent"
            hide chloe_normal
            hide sasha_annoyed
            show sasha_shocked at center:
                zoom 0.6
            s "Absent??"
            hide sasha_shocked


# Scene-3:Classroom


            