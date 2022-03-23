import time
import random
# from ctypes import sizeof
# from turtle import width
import PIL.Image 


ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width = 100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CLASSES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Hero:
    def __init__(self, name, health, power, brains):
        self.name = name
        self.health = health 
        self.power = power
        self.brains = brains

class Villans:
    def __init__(self, name, health, power, brains):
        self.name = name
        self.health = health
        self.power = power
        self.brains = brains
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~INSTANCES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hannibal = Hero("Hanniabal", 9, 3, 10)
face = Hero("Face", 9, 3, 8)
ba = Hero("B.A. Barracus", 10, 9, 5)
murdock = Hero("Howling Mad Murdock", 10, 2, 5)
toughGuy = Villans("Bubba", 10, 8, 2)
sneakyGuy = Villans("Lenny", 9, 3, 6)
bossMan = Villans("Chuck", 9, 3, 10)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FUNCTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#ba fights two darryls
def baVersusTwoDarryls ():
    ba.health = 10
    sneakyGuy.health = 9
    ax = input(("""You decide to go for the two derelict Darryl's but unfortunately, they got the drop on you and combine for a massive double-shot punch to the gut!
    OOOF!  As you stumble back, you desperately look around for something to level the playing field.  You see a crate of watermelons and a lawn chair.  Which do you grab?\n
    A) Grab a watermelon\n
    --or--\n
    B) Grab a lawn chair\n
    """))
    if ax == "A":
        ba.health = ba.health - sneakyGuy.power
        print("""\n'You gonna pay for that, suckas!', you say as you grab one of the watermelons out of the nearby crate.  When one of the Darryls tries to tackle you, you 
        smash the watermelon on his head so his head is stuck inside of it and he can no longer see where he is going.  You turn him around and push him towards his other brother Darryl, knocking them both over.
        'Now that's my kind of bowling', you say with a grin.
        """)
        sneakyGuy.health = sneakyGuy.health + 1
        sneakyGuy.health = sneakyGuy.health - ba.power
        print(f"Your health is >>>>>{ba.health}<<<<< while the two Darryl's health is >>>>>{sneakyGuy.health}<<<<<""\n")
        axx = input(("""\nWhile those two bums are bumbling and stumbling around, you survey the scrum.  Seems like your boys are all taking care of business
        should you\n
        A) Finish the two Darryls off?\n 
        --or--\n
        B) Help out your compadres?\n
        """))
        if axx == "A":
            print("""
            You finish the brothers' Darryl off with a figure six super leg-lock.\n
            """)
            print("""
            When you stand up, you see that the rest of your squad made short work
            of Chuck and his cowardly crew as well.  You tie them up so the state authorities can deal with 'em.  You and the rest of the A-team climb into the 
            big-rig, and deliver the Penhall's last batch of watermelons to the L.A. Farmers Market. You successfully sell them, take your share of the proceeds, and give the rest to 
            Penhalls.  The farm and the day are saved.  Thanks to the A-Team! 
            """)
            gameOver()
        elif axx == "B":
            print("""
            You go to help out your boys handle the rest of the riff-raff.  Unfortunately as soon as you turn around, the last thing you see is Bobby raring back his fist and then
            its lights out!   When you finally come to, you discover you are a special guest of your arch enemy, Colonel Lynch, in his all-inclusive barracks.  But this is no vacation, nope looks like 
            you'll be doing some hard time.  For now, you lose.....
            """)
            gameOver()
        else:
            print("You have to pick 'A' or 'B'")
            baVersusTwoDarryls()
    elif ax == "B":
        ba.health = ba.health - sneakyGuy.power
        print("""
        'Have a seat!', you say with a grin, as you jam the lawnchair down over one of the Darryl's heads, spin him around, kick him in the butt, and send him crashing into his other 
        brother Darryl
        """)
        sneakyGuy.health = sneakyGuy.health - ba.power
        print(f"Your health is >>>>>{ba.health}<<<<< while the two Darryl's health is >>>>>{sneakyGuy.health}<<<<<") 
        ayy = input(("""
        While those two bums are bumbling and stumbling around, you survey the scrum.  Seems like your boys are all taking care of business
        should you\n
        A) Finish the two Darryls off?\n
        --or--\n
        B) Help out your compadres?
        """))
        if ayy == "A":
            print(f"Your health is >>>>>{ba.health}<<<<< while the two Darryl's health is >>>>>{sneakyGuy.health}<<<<<")
            print("""
            You put both brothers' heads in a reverse head-lock and administer a double-helpin-DDT that would make Jake the Snake blush! 
            When you stand up, you see that the rest of your squad made short work
            of Chuck and his cowardly crew as well.  You tie them up so the state authorities can deal with 'em.  You and the rest of the A-team climb into the 
            big-rig, and deliver the Penhall's last batch of watermelons to the L.A. Farmers Market. You successfully sell them, take your share of the proceeds, and give the rest to 
            Penhalls.  The farm and the day are saved.  Thanks to the A-Team! 
            """)
            gameOver()
        elif ayy == "B":
            print("""
            You go to help out your boys handle the rest of the riff-raff.  Unfortunately as soon as you turn around, the last thing you see is Bobby raring back his fist and then
            its lights out!   When you finally come to, you discover you are a special guest of your arch enemy, Colonel Lynch, in his all-inclusive barracks.  But this is no vacation, nope looks like 
            you'll be doing some hard time.  For now, you lose.....
            """)
            gameOver()
        else:
            print("You have to pick 'A' or 'B'")
            baVersusTwoDarryls()
    else:
        print("You have to pick 'A' or 'B'")
        baVersusTwoDarryls()
#------------------------------------------
#sceneTwoHannibal
def sceneTwo():
    print("""
    ---------------------------------SCENE TWO-----------------------------------------\n
    You swing by and pick up the rest of the A-Team in the helicopter before heading out to Penhall Produce Farm.  Upon landing, you meet up with old man Penhall 
    and his lovely daughter Ellen.  You get the lowdown on just how dire the situation is.  Not only do the Penhall's only have one more crop of watermelons
    to deliver to market but they are already so ripe they are in danger of spoiling!  These watermelons have to be delivered pronto!  You get the boys
    to work immediately.  The Faceman starts burning up the phone lines to get the best price on your cash crop.  Murdock and BA fire up their welding 
    torches to help fabricate the truck into an inpentrable tank capable of withstanding bullets or LA freeway potholes.  You get to work on the chopper, just in case.  
    \n\n\n
    """)
    time.sleep(5)
    print("""
    🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵🎷🎷🎷🎷🎷🎷🎷🎷🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎷🎷🎷🎷🎷🎷🎷🎷 🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵       
    \n80's montage of dudes making stuff with awesome synth and guitar rock playing in the background(Capped with an awesome sax solo)\n
    🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵🎷🎷🎷🎷🎷🎷🎷🎷🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎷🎷🎷🎷🎷🎷🎷🎷 🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵 
    """)
    time.sleep(3)
    print("""
    \nAs the last note from that killer saxophone solo fades into the distance, you stand back and admire what your crew has put together.  B.A. Barracus and Murdock 
    were able to turn one of the Penhall semi-trucks into a rolling fortress of steel plated beauty!  Face comes out from the farmhouse....he's pretty excited, he found a 
    buyer who is willing to pay 0.40 a bushel!  Wow!  That sounds great!  Is that a good price?  How are you supposed to know!  You are a soldier of fortune who has been on the run from the 
    military police the past ten years for a crime you didn't commit, remember????!!  Finally, you take a look at the modifications
    you were able to make on the huey.  Not too bad if I do say so myself.  Just as you are about to pull out one of your trademark cigars, and say your catchphrase:  "I love it when a plan comes....
    you stop midsentance.
    """)
    time.sleep(3)  
    print("""\nYou see a whole calvacade of cars pull into the Penhall farm.  Oh no!  It's that villainous vaquero of the Valley, Chuck Easterland.  Apparently the croocked local cops tipped him off
    to your shenanigans down at the airfield.  It's not just Chuckie boy though, he's rounded up the entire possee:  Lenny, Bart, Bobby, Larry, Larry's brother Darryl, 
    and Larry's other brother Darryl, plus Bubba from the airfield (and he doesn't look too happy with you after that little skirmish at the airfield!).  
    The hard hitting heavies get out of their cars and assemble for a group sneer.  Ole Chuck Easterland waits a beat for the dramatic pause and then says:  
    """)
    time.sleep(3)
    print(""""You boys done messed up! I'm aiming to make this land mine and what Chuck Easterland wants......Chuck Easterland gets.  Now, I realize you boys aint from 
    around here, so I'm gonna give you one chance to skeedattle on out of here and we'll forget any of this happened.  
    While you mull over Chuck's generous offer (it's been awhile since you had a good skeedattle), you also know the A-Team never backs down from a fight.  The only
    thing you are considering right now is who is gonna get a heaping serving of knuckle sandwich first!  While you would love to give ole Chuck the first serving, 
    he is way at the back of the bunch, surrounded by his crew.  Your best friend Bubba is to the left of you, and one of the Darryl's (you forget which one) is to your right.
    What should you do?
    """)
    time.sleep(3)
    hRanch = input(("""What should you do?\n
    A) Make a rush for Chuck Easterland and hope you make it through the scrum cleanly?\n
    --or--\n
    B) Propose a nonviolent solution to your issues\n
    """))
    if hRanch == "A":
        fightSneakyBadGuySmartGoodGuy()
    elif hRanch == "B":
        trickSneakyGuySmartGoodGuy()
    else:
        print("Please Pick 'A' or 'B'")
        sceneTwo()
#---------------------------------
#sceneTwoBA
def sceneTwoBA():
    print("""
     ---------------------------------SCENE TWO-----------------------------------------\n
    \n\n\nAs you slowly come to, you wake up in a bed on the Penhall Produce Farm.  You are about to go bust some skulls for making you fly again
    but before you can do that, Faceman and Hannibal fill you in on just how dire the situation is.  Not only do the Penhall's only have one more crop of watermelons
    to deliver to market but they are already so ripe they are in danger of spoiling!  These watermelons have to be delivered pronto!  Hannibal has The Faceman start 
    making phone calls to see how much you can get for the watermelons.  You and that crazy sucka, Murdock, fire up your welding torches and start turing the Penhall's
    semi-truck into an inpentrable tank capable of withstanding bullets or LA freeway potholes.    
    """)
    time.sleep(5)
    print("""
    🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵🎷🎷🎷🎷🎷🎷🎷🎷🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎷🎷🎷🎷🎷🎷🎷🎷 🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵       
    \n80's montage of dudes making stuff with awesome synth and guitar rock playing in the background(Capped with an awesome sax solo)\n
    🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵🎷🎷🎷🎷🎷🎷🎷🎷🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎸🎷🎷🎷🎷🎷🎷🎷🎷 🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵🎵🎵🎶🎵🎵 🎶🎵🎵 🎶🎵🎵 
    """)
    time.sleep(3)
    print("""
    \nAs the last note from that killer saxophone solo fades into the distance, you stand back and admire all that you and your crew have put together.  The Penhall semi-trucks 
    is a rolling fortress of steel!  Face comes out from the farmhouse....he's pretty excited, he found a 
    buyer who is willing to pay 0.40 a bushel!  Wow!  That sounds great!  Is that a good price?  How are you supposed to know!  You are a soldier of fortune who has been on the run from the 
    military police the past ten years for a crime you didn't commit, remember????!!  Just as Hannibal gets his cigar out to light and starts to utter his iconic 
    trademarked expression, "I love it when a ..........he stops midsentence. \n
    """)
    print("""A calvacade of cars has pulled into the Penhall farm.  Oh no!  It's that villainous vaquero of the Valley, Chuck Easterland.  Apparently the croocked local cops tipped him off
    to your shenanigans down at the airfield.  It's not just Chuckie boy though, he's rounded up the entire possee:  Lenny, Bart, Bobby, Larry, Larry's brother Darryl, 
    and Larry's other brother Darryl, plus Bubba from the airfield (and he doesn't look too happy with you after that little skirmish at the airfield!).  
    The hard hitting heavies get out of their cars and assemble for a group sneer.  Ole Chuck Easterland waits a beat for the dramatic pause and then says:  
    "You boys done messed up! I'm aiming to make this land mine and what Chuck Easterland wants......Chuck Easterland gets.  Now, I realize you boys aint from 
    around here, so I'm gonna give you one chance to skeedattle on out of here and we'll forget any of this happened.  
    """)
    time.sleep(3)
    print("""You stare down the gang and give them your harshest snarl.  Well, if it's a fight they want, it's a fight they are gonna get.  The only question?  Who to attack first!
    To your left, you got the two Darryls and to your right, somebody who looks like he was a reject for Big-Bad-And-Ugly Contest at the local state fair, Bobby.  
    """)
    time.sleep(3)
    baRanch = input("""What should you do?\n
    A) take on the two Darryls\n
    --or--\n
    B) Take Bobby for a spin on the KO express?
    """)
    if baRanch == "A":
        baVersusTwoDarryls()
    elif baRanch == "B":
        baVersusBobby()
    else:
        print("You can only choose 'A' or 'B'")
        sceneTwoBA()
#----------------------------
#GAME OVER!!!!!!
def gameOver():
    print("Game Over")
    quit() 
#----------------------------
#BUBBA VERSUS BA
def fightToughBadGuyToughGoodGuy():
        toughGuy.health = 10
        ba.health = 10
        toughGuy.health = toughGuy.health - ba.power
        print("You walk up to the security guard standing post.  You ask him whats that there on his shirt?  When he looks down, KABLAMY!  You pop him hard with a vicious upper cut\n")
        time.sleep(3)
        print(f"<<<<<Your health is now {ba.health}>>><<<Bubba's health is now {toughGuy.health}>>>>>""\n")    
        print("""You bashed that sucka square in the jaw and he is staggering...you take a moment to admire your handiwork before deciding...\n""")
        time.sleep(3)
        x = (input("""
        Should you 
        A) Give him the ole' Three Stooges windup knockout punch\n
        --or--\n 
        B) be a gentleman about it and give him a chance to recover")
        """))
        if x == "A":
            print("""
            You don't hesitate as you go to put on the finishing touches.  You wind up like Moe, Larry, and Curly and deliver a knockout blow!
            Lights out, sucka!  Just as you are about to tie him up, you feel a light poke in the back of your shoulder.  It's that darn Hannibal and he's drugged you again to get you
            on that helicopter!  The last thing you remember is Face and Hannibal loading you on the helicopter before you fade off to sleep.
            """)
            sceneTwoBA()
        elif x == "B":
            print("""
            Well, turns out you shouldn't have waited.  Now its a fight.  The big lug shakes the cobwebs out of his head, rubs his jaw, 
            looks up, smiles and comes back for more. This guy's a slow learner, time to take him to the School of Hard Knocks!
            """)
            randomHealthBonus = random.randint(1, 10)
            toughGuyHealth2 = toughGuy.health + randomHealthBonus
            print(f"<<<<<You had knocked Bubba's health down to {toughGuy.health}>>>>>but waiting to attack again has allowed his health to recover by <<<<<{randomHealthBonus}>>>>> giving him a total health of <<<<<{toughGuyHealth2}>>>>>")
            print("""
            Bubba comes right back after you and takes a mighty swing.....and connecting....you suddenly don't feel so good!
            """)
            ba.health = ba.health - toughGuy.power
            print(f"<<<<<Your health is now {ba.health}>>><<<Bubba's health is now {toughGuyHealth2}>>>>>")
            time.sleep(1)
            y = (input("""
            A) Should you attack again?\n
            --or--\n
            B) should you run away
            """))
            if y == "A":
                randomPowerDecreaser= random.randint(1, 5)
                baPower2= ba.power - randomPowerDecreaser
                toughGuyHealth3 = toughGuyHealth2 - baPower2
                if toughGuyHealth3 > 0:
                    print("""You decide to go for the head.  Unfortunately, Bubba sees this coming a mile away.  He easily ducks out of the way and then 
                    pummels you with a series of vicious left/right combinations until you get the knocked out flat on your sick gold chains.  When you 
                    finally come to?  You wake up in a military barracks.  Looks like Colonel Lynch caught up to you.  Your only hope is that the rest of the 
                    guys break you out.  But for you right now?  Your game is over!
                    """)
                    gameOver()
                elif toughGuyHealth3 <= 0:
                    print("""You duck his next swing, turn him around and suplex with little concern for the current condition of his cranium.  
                    \nHe's out cold!  You win!\n
                    Just as you are getting up, you feel a light poke in the back of your shoulder.  It's that darn Hannibal and he's drugged you again to get you
                    on that helicopter!  The last thing you remember is Face and Hannibal loading you on the helicopter before you fade off to sleep.
                    """)
                    sceneTwoBA()
            elif y == "B":
                print("Wow, you dare disrespect Mr. T by suggesting that he would ever run away???????!!  How DARE you???!!  That's it, game over, you lose!")
                gameOver()
            else: 
                print("need to choose a or b")
                fightToughBadGuyToughGoodGuy()   
        else:
            print("need to choose a or b")
            fightToughBadGuyToughGoodGuy()   
#------------------------------------------------------
#BA VERSUS BOBBY
def baVersusBobby():
        toughGuy.health = 10
        ba.health = 10
        print("You decide to pick on somebody your own size and proceed to give Bobby a buy-one-get-one-free deal on your fists!\n")
        toughGuy.health = toughGuy.health - ba.power
        print(f"<<<<<Your health is now {ba.health}>>><<<Bobby's health is now {toughGuy.health}>>>>>""\n")    
        print("You try to punch Bobby again, but he successfully ducks out of harms way and delivers a body blow that would make Iron Mike proud")
        ba.health = ba.health - toughGuy.power
        xxxx = (input("""
        You quickly regroup, but need to make this next shot count......
        Should you\n 
        A) Throat punch him\n
        --or--\n
        B) kick him 
        """))
        if xxxx == "A":
            print("""
            'Unfortunately for you, Bobby, it's Throat Punch Thursday', you exclaim as you pop Bobby in the larynx and follow that up with a rapid
            left hook that knocks the thug straight out!  As you stand over your vaniquished foe and give him one more flex of the pythons of steel, you take a look 
            around you.  It seems that your teammates made short work out of Chuck and his lowly lowlifes. You and Hannibal tie them up so the state authorities can deal 
            with 'em.  You and the rest of the A-team climb into the big-rig, roll out, and deliver the Penhall's last batch of watermelons to the L.A. Farmers Market. 
            You successfully sell them, take your share of the proceeds, and give the rest to the Penhalls.  The farm and the day are saved.  Thanks to the A-Team!
            """)
            gameOver()
        elif xxxx == "B":
            yyyy = input(("""
            You go for a spinning scorpion kick but mistime your jump badly.  You land flat on your back, your gold chains weighing you down to the point that you can't
            get up!  You despearately grasp around you for anything you could use to defind yourself.  You feel something to your right.  You grab it as Bobby jumps in the air to deliver a flying elbow.  Do you....
            A) roll to get out of the way \n 
            --or--\n
            B) use the device to defind yourself
            """))
            if yyyy == "A":
                print("""
                You quickly roll, narrowly getting out of the way before Boddy comes crashing to the Earth with his dry, flaky elbows coming straight 
                for your dome.  Bobby's elbow takes the brunt of his weight as he lands where you used to be.  He writhes around in pain.  You quickly get up 
                and perform a perfect leg drop!
                """)
                toughGuy.health = toughGuy.health - ba.power 
                print(f"<<<<<Your health is now {ba.health}>>><<<Bobby's health is now {toughGuy.health}>>>>>")  
                print("""You WIN!!!!!! \n
                Bobby is knocked out cold!  you take a look around to see if anybody else needs a helping of knuckle sandwiches.  However, it looks like everybody is full.
                Your teammates made short work out of Chuck and his lowly lowlifes. You and Faceman tie them up so the state authorities can deal 
                with 'em.  You and the rest of the A-team climb into the big-rig, roll out, and deliver the Penhall's last batch of watermelons to the L.A. Farmers Market. 
                You successfully sell them, take your share of the proceeds, and give the rest to the Penhalls.  The farm and the day are saved.  Thanks to the A-Team!
                """)
            elif yyyy == "B":
                print("""You quickly grab a hold of it and with dread realize it's nothing but an ordinary yard hose.  Bobby comes crashing to the Earth and knocks you out with his 
                dry, flaky, gross elbows.  When you finally come to, you realize you are in cuffs and in the back of a squad car.  You know it's only a matter of time before they fingerprint
                you, identify you, and then you'll have a one-way ticket back to the military barracks.  The A-Team loses this round......
                """)
                gameOver()
            else:
                print("You can only choose 'A' or 'B'")
                baVersusBobby()
        else: 
            print("You can only choose 'A' or 'B'")
            baVersusBobby()
#--------------------------------------------------------------
#TOUGH BAD GUY VERSUS WEAK GOOD GUY<<<<<DO NOT TOUCH>>>>>

def fightToughBadGuyWeakGoodGuy():
        hannibal.health = 10
        toughGuy.health = 10
        toughGuy.health = toughGuy.health - hannibal.power    
        print("\nYou hit him hard, but unfortunately not hard enough, Bubba is still on his feet and he appears to be slightly irritated with your ruse\n")
        time.sleep(2)
        print(f"<<<<<Your health is now {hannibal.health}>>><<<Bubba's health is now {toughGuy.health}>>>>>")
        
        x = (input("""\nWhat should you do?  Should you:\n
        A = make like a shepherd and get the flock out of there\n
        --or--\n
        B = give the big lug another slug\n
        """))
        if x == "A":
            print("\nWhile lunkhead is still trying to figure out which way is north and which way is south, you decide to cut your losses and beat it to the chopper.  After all, you've always been more of a lover than a fighter.  You sprint to the helicopter and jump into the cockpit.  Adhering to television show rules, the keys to the copter are in the visor.  You fire up the huey and make your getaway while Bubba shakes his fist at you in vain.  Smell ya later!\n")
            time.sleep(5)
            sceneTwo()
        elif x == "B":
            print("""
            you take another crack at the big burly behemoth.\n  
            WHAP!
            """)
            randomHealthBonus = random.randint(1, 10)
            toughGuyHealth2 = toughGuy.health + randomHealthBonus
            toughGuyHealth3 = toughGuyHealth2 - hannibal.power
            if toughGuyHealth3 > 0:
                print(f"This guy appears to be getting stronger as the fight continues!  He's a savage! <<<<<Your health is now {hannibal.health}>>><<<Bubba's health is now {toughGuyHealth3}>>>>>""\n")
                print("You gave it your best shot and he's still on his feet!  This guy can't take a hint!  Should you:\n")
                y = (input("""
                A) give him the Kung Fu Grip Death Punch\n
                --or--\n
                B) make like a banana and split!
                """))
                if y == "A":
                    randomHealthBonus2 = random.randint(1, 10)
                    toughGuyHealth4 = toughGuyHealth3 + randomHealthBonus
                    hannibalHealth2 = hannibal.health - 2
                    print(f"Bubba shakes your latest attack off with ease!  In fact, Bubba seems to be getting his third AND fourth wind, his health increases by {randomHealthBonus2}.  That can't be good for you!\n")
                    print(f"You try roundhouse kicking him into oblivion.....")
                    print(f"But you can't seem to make a dent!  In fact?  You seem to be wearing out, old man!  <<<<<Your health is now {hannibalHealth2}>>>>><<<Bubba's health is now {toughGuyHealth4}>>>>>""\n")
                    toughGuyHealth4 = toughGuyHealth4 - hannibal.power
                    if toughGuyHealth4 > 0:
                        print("Unfortunately, you give it everything you got but you can't knock him out.  After taking a barrage of shots, Bubba rares back and KNOCKS YOU OUT! You don't wake up until next week and from the looks of it, you earned yourself a one way ticket to Colonel Lynch's stockade.")
                        gameOver()
                    elif toughGuyHealth4 <= 0:
                        print("Your kick sends him flying through the air, and he's passed out!  YOU WIN!")
                    else:
                        print("you have to pick 'A' or 'B', dum-dum!")
                elif y == "B":
                    print("""
                    As you turn to make like a hockeystick and get the puck out of there, big ole Bubba puts you in a big ole bear hug and squeezes you until it's lights out
                    for yours' truly.  When you come to, you are behind bars in Colonel Lynch's stockade.  Looks like your soldier of fortune career has been put into early retirement!
                    """)
                    gameOver()
                else:
                    print("you need to pick 'A' or 'B'....you know, maybe Airwolf is more your speed....")
                    fightToughBadGuyWeakGoodGuy()
            elif toughGuyHealth3 <= 0:
                print("Wow!  You got really lucky! You barely survived that fight, maybe next time you'll send B.A. to take care of the dirty work!")
            else:
                print("You need to pick 'A' or 'B'...you know....maybe Knight Rider is more your speed.....")
                fightToughBadGuyWeakGoodGuy()   
        else:
            print("need to choose a or b")
            fightToughBadGuyWeakGoodGuy()   

#---------------------------------------------------
#TOUGH GUY GETS OUTSMARTED BY SMART GOOD GUY
def trickToughGuySmartGoodGuy():
    print("""
    You dip into the A-Team van and pop open your suitcase of disguises.  Your in luck, your security guard uniform got back from the cleaners after all.
    You put on the outfit as well as apply a fake mustache and porkchops, and viola, you are a new man.  You stride up to the unsuspecting
    mark.....'Hey bub, I'm here to spell you for your lunch break.'  Bubba happily agrees and proceeds to leave post haste.  'I love it when a plan comes
    together' you say as you make your way to your newly acquired chopper.
    """)
    time.sleep(3)
    sceneTwo()
#-----------------------------------
def rps():
    x = input(("""
    Welcome to rock paper scissors....A Team style!
    Choose your weapon........\n
    Press 1 for 'Rock'\n
    Press 2 for 'Scissors'\n
    Press 3 for 'Paper'\n
    """))
    if x =="1":
        print("You chose rock.....")
    elif x == "2":
        print("You chose scissors.....")
    else:
        print("You chose paper.....")

    
    
    num = random.randint(1, 9)
    
    if num < 4:
        y = 'Rock'
    elif num > 3 and num < 7:
        y = 'Paper'
    else:
        y = 'Scissors'

    if x == "1" and y == 'Paper':
        print("Chuck went with.....")
        time.sleep(3)
        print("""Paper!  Oh no!  Chuck wins and the Penhalls are ruined! 
        So many thoughts go through your brain....like....how did this happen?  What possessed
        you to leave something so important to the hands of fate?  Is this even
        a legal transaction?  You've got a lot to think about.  You and your team sulk off 
        to your awesome GMC A-Team van and leave Green Valley with your collective tails tucked
        between your legs.
        """)
        gameOver()
    elif x == "1" and y == 'Scissors':
        print("Chuck goes with........")
        time.sleep(3)
        print("""Scissors!  The A-Team wins again!  Chuck is livid!  But he's a man 
        who takes his Rock, Paper, Scissors seriously.  He knows he can't violate the 
        spirit of the game....
        'Well, stranger, you beat me fair and square....looks like I will be leaving the 
        Penhall's alone from now on', he says as he kicks at the dirt at his feet.  
        'Come on boys, lets leave these nice folks alone.'
        The Penhall's celebrate.  You and your crew jump into the cab of the semi, deliever
        the watermelons to the L.A. Farmers Market, sell the produce, and the Penhall's are able 
        keep their farm!  I love it when a plan comes together.....
        """)
        gameOver()
    elif x == "2" and y == 'Paper':
        print("Chuck goes with.....")
        time.sleep(3)
        print("""Paper!  The A-Team wins again!  Chuck is livid!  But he's a man 
        who takes his Rock, Paper, Scissors seriously.  He knows he can't violate the 
        spirit of the game....
        'Well, stranger, you beat me fair and square....looks like I will be leaving the 
        Penhall's alone from now on', he says as he kicks at the dirt at his feet.  
        'Come on boys, lets leave these nice folks alone.'
        The Penhall's celebrate.  You and your crew jump into the cab of the semi, deliever
        the watermelons to the L.A. Farmers Market, sell the produce, and the Penhall's are able 
        keep their farm!  I love it when a plan comes together.....
        """)
        gameOver()
    elif x == "2" and y == 'Rock':
        print("Chuck goes with.....")
        time.sleep(3)
        print("""Rock!  Oh no!  Chuck wins and the Penhalls are ruined! 
        So many thoughts go through your brain....like....how did this happen?  What possessed
        you to leave something so important to the hands of fate?  Is this even
        a legal transaction?  You've got a lot to think about.  You and your team sulk off 
        to your awesome GMC A-Team van and leave Green Valley with your collective tails tucked
        between your legs.
        """)
        gameOver()
    elif x == "3" and y == 'Rock':
        print("Chuck goes with.....")
        time.sleep(3)
        print("""Rock!  The A-Team wins again!  Chuck is livid!  But he's a man 
        who takes his Rock, Paper, Scissors seriously.  He knows he can't violate the 
        spirit of the game....
        'Well, stranger, you beat me fair and square....looks like I will be leaving the 
        Penhall's alone from now on', he says as he kicks at the dirt at his feet.  
        'Come on boys, lets leave these nice folks alone.'
        The Penhall's celebrate.  You and your crew jump into the cab of the semi, deliever
        the watermelons to the L.A. Farmers Market, sell the produce, and the Penhall's are able 
        keep their farm!  I love it when a plan comes together.....
        """)
        gameOver()
    elif x == "3" and y == 'Scissors':
        print("Chuck goes with.....")
        time.sleep(3)
        print("""Scissors!  Oh no!  Chuck wins and the Penhalls are ruined! 
        So many thoughts go through your brain....like....how did this happen?  What possessed
        you to leave something so important to the hands of fate?  Is this even
        a legal transaction?  You've got a lot to think about.  You and your team sulk off 
        to your awesome GMC A-Team van and leave Green Valley with your collective tails tucked
        between your legs.
        """)
        gameOver()
    else:
        print("Chuck goes with......")
        time.sleep(3)
        print("The same thing!  It's a tie! You will have to choose again!")
        rps()
#-----------------------------------
#TWO SMART GUYS; RANDOM OUTCOME
def trickSneakyGuySmartGoodGuy():
    print("""You slowly take your cigar out of your front lapel pocket, light it up, and say with a steady calm voice:  'I got a better idea, Chuckie-boy.....
    Why don't we settle this like gentlemen over a game of.......
    Rock Paper Scissors?
    Chuck sneers at you and replies, 'Alright, stranger, what are you proposing?'
    One game, Chuck, you and me, mano a mano.  I win?  We get to deliver the Penhall's produce and you agree to leave them alone
    You win?  You get the Penhall farm for free.
    Chuck can't believe his luck.  Unbeknownst to you, he was the county Rock Paper Scissors Champ for three straight years....
    He replies, "Alright stranger.....you got yourself a deal, lets do this!
    You walk towards one another and meet in the middle while your respective gangs gather around you in a circle.....
    You could cut the tension with a knife.........
    """)
    rps()

#------------------------------------------------
#HANNIBAL VERSUS BOSSMAN FIGHT
def fightSneakyBadGuySmartGoodGuy():
    hannibal.health = 9
    bossMan.health = 9
    print("""You yell 'Here, catch!' to Bubba as you toss your zippo in his general direction, distracting him and Darryl long enough that you manage
    to get to that heinous herdsman cleanly.  As you start to square off with the leader of this smelly syndicate, the rest of the A-Team jump in as well and before
    you know it, we've got a real brouhaha on our hands!
    """)
    time.sleep(3)
    wheelOfChance = random.randint(1, 8)
    if wheelOfChance % 2 == 0:
        print("You start with a joke:  'Hey Chuck, what did the five fingers say to the face?\n")
        time.sleep(3)
        bossMan.health = bossMan.health - hannibal.power
        print("SLAP!!!!!  Chuck staggers back from the blow!\n")
        time.sleep(3)
        print(f"<<<<<Your health is now {hannibal.health}>>><<<{bossMan.name}'s health is now {bossMan.health}>>>>>""\n")
        time.sleep(3)
        
        print("However, Chuck quickly recovers and connects with a smashing uppercut\n")
        time.sleep(3)
        hannibal.health = hannibal.health - bossMan.power
        print("SHAZAM!\n")
        time.sleep(3)
        print(f"<<<<<Your health is now {hannibal.health}>>><<<{bossMan.name}'s health is now {bossMan.health}>>>>>""\n")
        time.sleep(3)
        
        print("'My mama warned me about getting into fights with ugly people, you always lose!', you say as you grab him by the shirt lapels and slam him into the side of a car\n")
        time.sleep(3)
        bossMan.health = bossMan.health - hannibal.power
        print("KAPOWEE\n")
        time.sleep(3)
        print(f"<<<<<Your health is now {hannibal.health}>>><<<{bossMan.name}'s health is now {bossMan.health}>>>>>""\n")
        time.sleep(3)

        print("Chuck quickly gets off the ground, a little wobbly, but comes back for more....He says, 'How about a nice warm cup of shut the hell up???!!', he says as he smashes a chair across your back\n")
        time.sleep(3)

        hannibal.health = hannibal.health - bossMan.power
        print("CRRAACK!\n")
        time.sleep(3)
        print(f"<<<<<Your health is now {hannibal.health}>>><<<{bossMan.name}'s health is now {bossMan.health}>>>>>""\n")
        time.sleep(3)
        
        print("As you smash your left fist upside his dome you say, 'If I wanted to hurt myself, I'd climb up to your ego and jump down to your IQ level!'\n")
        time.sleep(3)
        bossMan.health = bossMan.health - hannibal.power
        print("VRONK!\n")
        time.sleep(3)
        print(f"<<<<<Your health is now {hannibal.health}>>><<<{bossMan.name}'s health is now {bossMan.health}>>>>>""\n")
        print("""And with that last blow, you knock Chuck into next week.  While he is admiring the cartoon birds and stars circling his head, the rest of his mangy mutts 
        realize they are no match for your crew and quickly give up.  You tie them up so the state authorities can deal with 'em.  You and the rest of the A-team climb into the 
        big-rig, and deliver the Penhall's last batch of watermelons to the L.A. Farmers Market. You successfully sell them, take your share of the proceeds, and give the rest to 
        Penhalls.  The farm and the day are saved.  Thanks to the A-Team! 
        """)
        time.sleep(3)
        gameOver()
    elif wheelOfChance % 2 != 0:
        print("As you come within range, Chuck says: 'First I'm gonna wreck your face than I'm gonna wreck your crew!' as he connects a wild haymaker up side your head\n")
        time.sleep(3)
        hannibal.health = hannibal.health - bossMan.power
        print("WHAP!\n")
        time.sleep(3)
        print(f"<<<<<Your health is now {hannibal.health}>>><<<{bossMan.name}'s health is now {bossMan.health}>>>>>""\n")
        time.sleep(3)
        
        print("'Hey Chuck, I'm not saying your stupid, just that you've got bad luck when it comes to thinking', you reply as you punch Chuck in his paunch\n")
        time.sleep(3)
        bossMan.health = bossMan.health - hannibal.power
        print("OOOOF\n")
        time.sleep(3)
        print(f"<<<<<Your health is now {hannibal.health}>>><<<{bossMan.name}'s health is now {bossMan.health}>>>>>""\n")
        time.sleep(3)

        print("Chuck staggers back but comes back with a quip of his own 'Oh yeah?  Well your mama is so dumb, it takes her two hours to watch 60 minutes!'  He then smashes a chair across your back \n")
        time.sleep(3)
        hannibal.health = hannibal.health - bossMan.power
        print("BIFF!\n")
        time.sleep(3)
        print(f"<<<<<Your health is now {hannibal.health}>>><<<{bossMan.name}'s health is now {bossMan.health}>>>>>""\n")
        time.sleep(3)
        
        print("Well, Chuck, if intelligence skips a generation, your children will be brilliant!' you say as you roundhouse kick him Taekwondo style\n")
        time.sleep(3)
        bossMan.health = bossMan.health - hannibal.power
        print("KAPOW!\n")
        time.sleep(3)
        print(f"<<<<<Your health is now {hannibal.health}>>><<<{bossMan.name}'s health is now {bossMan.health}>>>>>""\n")
        time.sleep(3)

        print("Chuck gathers himself and says: 'Why don't you take a long walk off a short cliff' as he delivers a devastating uppercut square on your jaw!\n")
        time.sleep(3)
        bossMan.health = bossMan.health - hannibal.power
        print("KAPOW!\n")
        time.sleep(3)
        print(f"<<<<<Your health is now {hannibal.health}>>><<<{bossMan.name}'s health is now {bossMan.health}>>>>>")
        time.sleep(3)
        
        print("""And with that.......you are knocked out cold!  'Are you at a loss for words, or did you exhaust your entire vocabulary? harharharhar', says Chuck.  
        As the rest of your team fights valliantly, suddenly a group of military police led by your archrival Colonel Lynch pull up.  Seems that Chuck's crooked police force did a little
        research on you and your crew, discovered you were wanted by the military, and tipped Colonel Lynch on your whereabouts.  It looks like this is curtains for The A-Team! 
        """)
        gameOver()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~INTRO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("""
Farmer Penhall and his daughter, Ellen, two hard working produce farmers just outside the southern California 
town of Green Valley, have spent their whole lives working their family's land. Unfortunately, Penhall Produce Farm 
has fallen on hard times. Due to a couple of seasons of drought, the family was forced to take out a mortgage 
on their land.\n \n""")
time.sleep(3)
print("""Now, the local evil rancher, Chuck Easterland (of Chuck Easterland Ranch) has his eyes set on the 
Penhall Produce Farm land. He already owns half of Green Valley, but nothing can stop his lust for more and more 
land for his bountiful bovine beauties.\n\n
""")
time.sleep(3)
print("""
The Penhall's have tried to get this years crops to market, but the 
dasterdly Chuck Easterland has stopped them at every turn with one crooked move after another. \n\n
""")
time.sleep(3)
print("""He's hijacked the Penhall's trucks, ran off drivers, and bribed local law enforcement to allow him to blockade 
the one road out of the valley; stopping the Penhalls from selling their crops at the L.A. Farmer's Market. \n \n
""")
time.sleep(3)
print("""
Now, the Penhalls have only one crop of watermelon left. They have to get their last crop to the LA Farmer's Market, 
or else they won't be able to make their mortgage payments, they will lose the farm to the bank, 
and then the cowardly Chuck Easterland will swoop in and take their land for pennies on the dollar. \n\n
""")
time.sleep(3)
print("""

The Penhall's back's are against the wall..........\n\n
""") 
time.sleep(2)
print("\t\t\t\t\tThey have a problem......\n\n")
time.sleep(2)
print("\t\t\t\t\t\t\t\t\t\tNo one can help.....\n\n")
time.sleep(2)
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tBut if they can find them....\n\n")
time.sleep(2)
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tmaybe they can hire........\n\n")
time.sleep(2)

def main(new_width=100):
    path = "/Users/jasonreichert/digitalCrafts/week2/day4/aTeamLogo.svg.png"
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid pathname to an image")
    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)
main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def menu():
    while True: 
        answer = (input("""
        Welcome to the A-Team Game!!!!! \n ==============================================\n 
        Which character from the A-Team would you like to play as:\n\n
        1. Lieutenant Colonel John "Hannibal" Smith\n 
        2. Sergeant Bosco Albert "Bad Attitude" Baracus \n  
        3. No thanks, I'd rather play Frogger.  I quit! \n \n What do you want to do (1-3)?\n 
        """))
        if answer == "1":
            def main(new_width=100):
            #attempt to open image from user-input
                path = "/Users/jasonreichert/digitalCrafts/week2/day4/hannibal.jpg"
                try:
                    image = PIL.Image.open(path)
                except:
                    print(path, "is not a valid pathname to an image")
    
                new_image_data = pixels_to_ascii(grayify(resize_image(image)))

                #format
                pixel_count = len(new_image_data)
                ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

                #print result
                print(ascii_image)
            main()
            time.sleep(3)
            print("""
            You are Lieutenant Colonel John "Hannibal" Smith, the brains of this outfit, master tactician, commanding officer, and a cunning master of disguise. 
            As leader of the A-Team, you and your crew have agreed to help poor Farmer Penhall and his daughter Ellen in exchange for 30% of the watermelon crop profits. 
            The only problem? How to get to the Penhall Produce Farm. That rotten rancorous rancher, Chuck Easterland, has got the only way in or out of 
            Green Valley blockaded off, thanks to a bribe to the lousy local law enforcement. \n
            Well, just like when you were trapped three clicks behind the DM Zone back in Nam, if you can't get through a problem, you find a way OVER a problem. 
            So, you go the local airfield to see about acquiring a huey for you to drop you and your boys onto the farm. You peer through your binoculars and scan the airfield.  
            Eureka! You are in luck!  There is a helicopter on the airfield. The only problem, there 
            giant lug-head standing guard at his post.  He looks like one serious customer.  
            His namebadge says "Bubba".  Well, Bubba, your day just went from bad to worst, cause when the A-Team takes a job, they get the job done!  
            So, what will you do? 
            """)
            time.sleep(5)
            h = (input("""
            Should you \n
            A) approach the guard, ask him for a light, and when he reaches for a match, sucker punch him in the jaw?\n
            --OR--\n
            B) go yourself, employing one of your many disguises to scam your way onto the aircraft?\n
            """))
            if h == "A":
                fightToughBadGuyWeakGoodGuy()
            elif h == "B":
                trickToughGuySmartGoodGuy()
            else:
                print("You have to pick 'A' or 'B'")
                menu()
                
                

        elif answer == "2":
            def main(new_width=100):
                path = "/Users/jasonreichert/digitalCrafts/week2/day4/mrT3.jpg"
                try:
                    image = PIL.Image.open(path)
                except:
                    print(path, "is not a valid pathname to an image")
    
                new_image_data = pixels_to_ascii(grayify(resize_image(image)))
                pixel_count = len(new_image_data)
                ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

                print(ascii_image)
            main()
            time.sleep(3)
            ba = input(("""
            You are Seargeant Bosco Albert "Bad Attitude" Baracus. You are the "muscle" for the A-Team, capable of performing exceptional feats of strength. 
            You are also the team's mechanic, master at arms, demolition and weapons specialist. While you dislike that crazy fool Murdock, 
            you agree with him that the team should help the Penhall Farm. The only problem? How to get to the Penhall Produce Farm. 
            That hated heffer herder, Chuck Easterland, has got the only way in or out of Green Valley blockaded off. 
            Hannibal thinks that the only way to get to the farm is by helicopter, but you have a bad case of the aviophobias 
            and you ain't gettin' on no helicoipter, sucka! Hannibal asks you to help acquire the helicopter, but that's it, 
            you can keep both feeted firmly planted on terra firma. You go down to the local airfield where you find a helicopter 
            sitting in the middle of an old commuter plane hangar. The only problem, how to get it? There's a big ole meathead that's standing post.
            Do you\n
            A) bust that obtuse oaf across his thickhead and make off with the helicopter before he comes to? \n
             --or--\n
            B) quit the A-Team and visit your cousin in Chicago, James "Clubber" Lang, and help him train for his upcoming title fight?
            """))
            if ba == "A":
                fightToughBadGuyToughGoodGuy()
            elif ba == "B":
                print("""
                You tell the crew: "I told you fools, I ain't gettin' on no plane!" You promptly quit the A-Team and hop a Greyhound to your hometown of Chicago.\n 
                You help your cousin James "Clubber" Lang prepare for his upcoming heavyweight championship bout, where he knocks out Rocky Balboa in the second 
                round to become heavyweight champion of the world.\n 
                After that, you run a successful Boys Club on the South Side of Chicago, where you live out 
                your days polishing your gold chains and rings; pitying all fools.  While B.A. Barracus won? You, dear player, LOST.
                """)
                gameOver()
                
                
            else:
                ("You have to press 'A' or 'B'")
                menu()
        elif answer == "3":
            quit()

        else:
            print("You can only push 1, 2, or 3.  Please try again")
            menu()
    
menu()
        
