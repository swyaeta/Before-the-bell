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
image chloe_back ="images/chloe_back.png"
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
image sham ="images/normalboy.png"
image sham_scared ="images/sham_scared.png"

# this are the background that will be used there
image bedroom ="images/bedroom.png"
image class ="images/class.png"
image hallway="images/hallway.png"
image gym="images/gym.png"
image nightroom="images/nightroom.png"

# Scene 1: Starting
label start:
    play music "audio/calm.mp3"
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

    show sasha_angry at right:
        zoom 0.7
    s "and Mommmm!!!! didn't we have pancakes monday morning??"
    show mom at left:  
        zoom 0.7
    m "What are you dreaming sasi, today is Monday."    
    m "Go freshen up again and come on down for breakfast."

    hide mom
    hide sasha_angry
    show sasha_shocked at center:
            zoom 0.7
    
    s "Wasn't Monday yesterday?"
    s "Shit.....I have ms.aundrey's class then."
    hide sasha_shocked
    stop music

#Scene 2 : School hallway
    
    scene hallway with fade
    play music "audio/calm.mp3"
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
    stop music
    play music "audio/calm.mp3"
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
play music "audio/calm.mp3"
scene class with fade 
"Ms.aundrey's period starts"
show msaundrey_normal at center:
        zoom 0.6
f "Everyone keep your homework ahead of you"
hide msaundrey_normal

show sasha_normal at left:
        zoom 0.6
s "What homework??"      
show chloe_normal at right:
        zoom 0.6
c "The one she gave yesterday"
hide sasha_normal
show sasha_shocked at left:
        zoom 0.6
s "Wasn't yesterday mrs.carter's period???"
hide chloe_normal
hide sasha_shocked
show msaundrey_normal at left:
        zoom 0.6
f "What's the fuss girls any problem?"      
show sasha_sad at right:
        zoom 0.6
s "No...... ms.aundrey, I was just telling chloe that you forgot that yesterday was mrs.carter's period!"
hide msaundrey_normal
show msaundrey_angry at left:
        zoom 0.6
f "What are you saying sasha, are u fine?"
f "You kids are making up too many lies nowdays"
hide sasha_sad
menu:
    "Ask for foregivness ":
        show sasha_annoyed at right:
            zoom 0.6
        s "I'm not lying ask Mrs.carter, she taught us about the law of voting"
        f " Check the rountie, TODAY IS MONDAY!!"
        f "Today you have Mrs.carter's class after lunch"
        hide sasha_annoyed
        hide msaundrey_angry


    "Go to Mrs.carter's":
        scene gym with fade
        show msaundrey_angry at left:
                zoom 0.6
        show sasha_annoyed at right:
                zoom 0.6
        f "Mrs.carter could you come there for a while"          
        show mrscarter_normal at center:
                zoom 0.6      
        t "Yes ms.aundrey, everything fine?"
        f "Sasha did'nt do my homework and now she's saying that it was your class yesterday and you were discussing on the topic law of voting"
        hide mrscarter_normal

        show mrscarter_angry at center:
                zoom 0.6  
        t "NO...Today they have my class after lunch and then i'll teach about law of voting"
        t "I didn't expect this from you sasha"
        hide sasha_annoyed
        show sasha_annoyed at right:
                zoom 0.6
        s "No you taught us about different elections and house of representative"
        t "Stop lyingg.. Sasha, it's better if you just ask for forgiveness"
        s "I'm not lying"          
        f "Stop it and go to the class"
        hide sasha_annoyed
        hide msaundrey_angry
        hide mrscarter_angry

stop music
#Scene4 : Cafertia
play music "audio/calm.mp3"
scene hallway with fade
show msaundrey_angry at center:
        zoom 0.6
f "Ethan and Viven come there!!!!!!!"   
show ethan_shocked at left:
        zoom 0.6

e "vivi, come here!!"
show viven_shocked at right:
        zoom 0.6
v "what's wrong teacher??"
f "Aren't you ashamed to bully someone and act all innocent???"
hide viven_shocked
hide ethan_shocked
show viven_smug at left:
        zoom 0.6
v "No... we're just........ asking for academic help"
f "Stop lying and go apologize to sham and this is your last warning"
hide viven_smug
hide msaundrey_angry

show sasha_shocked at left:
        zoom 0.6
s " Didn't she say the same thing last monday" 

show chloe_normal at center:
        zoom 0.6       
c "What are you saying sasha?? Today is monday "

show sham at right:
        zoom 0.6 
r "Yes, I just told my parents over the phone on lunch"

menu:
    "Explain to them":
        hide sasha_shocked
        show sasha_annoyed at left:
                zoom 0.6
        s "What are you guys saying??? No,No..... I remember this...... This has happened!!!!!"
        r "Let's go chloe, she's acting so strange"
        s"No wait......"
        hide sasha_annoyed
        hide sham
        hide chloe_normal

        "Flashbackes NO,no no let's go....let's go....let's go"
        scene class with fade 
        play music "audio/fire.mp3"
        show chloe_back at left 
        show sham_scared at right
        c "NOooo.....Let's go somewhere....please save us "

        hide chloe_back
        hide sham_scared
        stop music
        play music "audio/calm.mp3"
    "Leave it":
        show sasha_sad at left:
                zoom 0.6  
        s "maybe yess.... maybe it's all in my head"
        show chloe_normal at center:
                zoom 0.6       

        show sham at right:
                zoom 0.6 
        c "yes....let's go.. we have mrs.carter now"

        hide sham
        hide sasha_sad
        hide chloe_normal

scene gym with fade 
show sasha_sad 
s"sham...?? chloe....???"
hide sasha_sad
show viven_smug at left:
        zoom 0.6
show ethan_smrik at center:
        zoom 0.6        
v "Yea...hahha...that will be so funnnn "
e "yeaa hahahhahahaha"

menu:
    "Eavesdrop on them":
        v "You noticed how that stupid sham, chloe and sasha were smiling????"
        e "We should do something to get back at them"
        v "Let's pretend to be sick and go home"
        e "Huh,, wot.... how will we get back at them this way"
        v "Don't forgot, I'm your elder by 5 mins"
        v "WE'LL SET MRS.CARTER'S CLASS ON FIREE AND THEN GOOOO.....hahahahhahaha"
        e "HHAHHAHAHAHHAHAHAHHAHAH"
        hide ethan_smrik
        hide viven_smug

        show sasha_shocked at left:
                zoom 0.6
        s "NOnoooo wayyyy......what????"
        hide sasha_shocked
        "Flashbackes NO,no no let's go....let's go....let's go"
        scene class with fade 
        play music "audio/fire.mp3"
        
        show chloe_back at left 
        show sham_scared at right
        c "NOooo.....Let's go somewhere....please save us someone"
        hide chloe_back
        hide sham_scared       
        stop music
        scene class with fade
        play music "audio/calm.mp3"
        show mrscarter_normal at center:
                zoom 0.7
        t "Good evening everyone!!"
        t "Today we're gonna read about laws of voting"
        t "In the US gov......."
        show chloe_back at right:
                    zoom 0.6
        c "TEACHERRRRR!!!!!!"
        stop music
        play music "audio/fire.mp3"
        show sasha_angry  at right:
                    zoom 0.6
        s "everyone!!!!!!!!!!! run!!!!!!!!!! there's fireeeee"
        hide sasha_angry
        hide chloe_back
        hide mrscarter_normal

        scene gym with fade 
        show mrscarter_angry at center:
                zoom 0.7   
        t "You were right sweetheart... we didn't believe you"

        show msaundrey_angry at left:
                zoom 0.7   
        f "We'll banned them from this school now!!!!!!!!!"
        hide msaundrey_angry
        hide mrscarter_angry
        stop music
        play music "audio/calm.mp3"
        scene bedroom with fade
        m "Honey get up, I have made your fav pancakes."
        show sasha_angry at right:
                    zoom 0.7
        s "MOMMM!!!!!! "
          
        show mom at left:
                    zoom 0.7
        m "What happened sweetheart??"
        m " Go freshen up again and come on down for breakfast."
        hide sasha_angry
        show sasha_shocked at center:
                    zoom 0.8
        s "NOO....mom.....wait"
        s "What day is it?"
        m "It's tuesday, baby"
        hide sasha_shocked
        hide mom

        scene hallway
        stop music
        "THE LOOP BREAKS"
        "YOU SAVEd THEM!" 
        

    
    "Leave them":
        
            show sasha_sad at left:
                    zoom 0.6
            s "They're gonna plan to bully him again" 
            play music "audio/calm.mp3"   
            hide sasha_sad
            "At mrs.carter's class"
            scene classroom with fade 
            show mrscarter_normal 
            t "Good evening everyone!!"
            t "Today we're gonna read about laws of voting"
            t "In the US gov........."
            stop music
            play music "audio/fire.mp3"
            show sham_scared at center:
                    zoom 0.6
            show chloe_back at right:
                    zoom 0.6
            c "TEACHERRRRR.............FIREEEEEE!!!!!!!!!! save us "
            t "Don't worry..... I'm right there"
            hide mrscarter_normal
            hide chloe_back
            hide sham_scared
            show sasha_shocked at left:
                zoom 0.6
            s "NONNOONOO....................."
            hide sasha_shocked
            
            stop music
            scene bedroom with fade
            play music "audio/calm.mp3"
            m "Honey get up, I have made your fav pancakes."

            show sasha_angry at right:
                    zoom 0.7
            s "MOMMM!!!!!! "
          
            show mom at left:
                    zoom 0.7
            m "What happened sweetheart??"
            m " Go freshen up again and come on down for breakfast."
            hide sasha_angry
            show sasha_shocked at center:
                    zoom 0.8
            s "NOO....mom.....wait"
            s "What day is it?"
            stop music
            play music "audio/fire.mp3"
            m "It's monday, baby"
            hide mom
            hide sasha_shocked
            scene hallway
            "THE LOOP REPEATS......."
            "YOU COULDN'T SAVE THEM"

            

             