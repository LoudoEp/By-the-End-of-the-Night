# The script of the game goes in this file.

init python:
    renpy.music.register_channel("ambient", "ambient", loop=True, stop_on_mute=True, tight=False, buffer_queue=True)

################################################################################

### TRANSFORMS ###

transform goodsize:                 #borrowed from Unagi
    xysize (1920, 1080)

transform orb_anim:                 #borrowed from Rekion
    xalign 0.5
    yalign 0.5
    parallel:
        easein 1.5 yalign 0.425
        block:
            ease 3.0 yalign 0.575
            ease 3.0 yalign 0.425
            repeat

################################################################################

### VARIABLES ###

default pov = "anna"

define N = Character(None, what_italic = True)

################################################################################

### FEDERICO ###

define F = Character(_("Federico"), color ="#fff", what_prefix='“', what_suffix='”')
define MCF = Character(_("Federico"), color ="#fff", what_prefix='“', what_suffix='”', image="fed")
define FFB = Character(_("Federico"), color ="#fff", what_prefix='“', what_suffix='”', what_italic = True)

layeredimage fed:
    zoom 0.45 yoffset 550
    group body:
        attribute base default:
            "images/Federico/Base.webp"
    group expressions:
        attribute neutral default:
            "images/Federico/Neutral.webp"
        attribute concerned:
            "images/Federico/Concerned.webp"
        attribute happy:
            "images/Federico/Happy.webp"
        attribute mad:
            "images/Federico/Mad.webp"
        attribute sad:
            "images/Federico/Sad.webp"
        attribute turned:
            "images/Federico/Turned.webp"
    group eyes:
        attribute open default:
            Null()
        attribute closed:
            Null()

image side fed = LayeredImageProxy("fed")

################################################################################

### ANNA ###

define A = Character(_("Anna"), color ="#fff", what_prefix='“', what_suffix='”')
define MCA = Character(_("Anna"), color ="#fff", what_prefix='“', what_suffix='”', image="ann")
define AFB = Character(_("Anna"), color ="#fff", what_prefix='“', what_suffix='”', what_italic = True)

layeredimage ann:
    xzoom -1.0 zoom 0.45 yoffset 550
    group body:
        attribute base default:
            "images/Anna/Base.webp"
        attribute openpaw:
            "images/Anna/Open.webp"
        attribute side:
            "images/Anna/Side.webp"
    group expressions:
        attribute neutral default:
            "images/Anna/Neutral.webp"
        attribute angry:
            "images/Anna/Angry.webp"
        attribute concerned:
            "images/Anna/Concerned.webp"
        attribute happy:
            "images/Anna/Happy.webp"
        attribute mad:
            "images/Anna/Mad.webp"
        attribute sad:
            "images/Anna/Sad.webp"
        attribute sad2:
            "images/Anna/Sad2.webp"
    group eyes:
        attribute open default:
            Null()
        attribute closed:
            Null()

image side ann = LayeredImageProxy("ann")

################################################################################

### RAIMONDO ###

define R = Character(_("Raimondo"), color ="#fff", what_prefix='“', what_suffix='”')
define MCR = Character(_("Raimondo"), color ="#fff", what_prefix='“', what_suffix='”', image="rai")
define RFB = Character(_("Raimondo"), color ="#fff", what_prefix='“', what_suffix='”', image="pastrai", what_italic = True)

layeredimage rai:
    zoom 0.45 yoffset 550
    group body:
        attribute base default:
            "images/Raimondo/Base.webp"
        attribute meee:
            "images/Raimondo/Meee.webp"
    group expressions:
        attribute neutral default:
            "images/Raimondo/Neutral.webp"
        attribute annoyed:
            "images/Raimondo/Annoyed.webp"
        attribute sad:
            "images/Raimondo/Sad.webp"
        attribute gag:
            "images/Raimondo/Gag.webp"
        attribute happy:
            "images/Raimondo/Happy.webp"
        attribute mad:
            "images/Raimondo/Mad.webp"
    group eyes:
        attribute open default:
            Null()
        attribute closed:
            Null()

image side rai = LayeredImageProxy("rai")

image side pastrai:
    zoom 0.45 yoffset 550
    "images/Raimondo/Past1.webp"
    pause 3.0
    zoom 0.45 yoffset 550
    "images/Raimondo/Past2.webp"
    pause 0.5
    zoom 0.45 yoffset 550
    "images/Raimondo/Past1.webp"
    pause 5.0
    zoom 0.45 yoffset 550
    "images/Raimondo/Past2.webp"
    pause 0.5
    zoom 0.45 yoffset 550
    "images/Raimondo/Past1.webp"
    pause 2.0
    zoom 0.45 yoffset 550
    "images/Raimondo/Past2.webp"
    pause 0.5
    repeat
    

################################################################################

### POLYHEDRON ###

define P = Character(_("Polyhedron"), color ="#fff", what_prefix='“', what_suffix='"')

image poly:
    zoom 0.3
    "images/Poly/STATUE_sprite.webp"


################################################################################

### BACKGROUNDS ###

image black = "#000"
image car = "images/pexels-Alessandro-Aviles.avif"
image approaching = "images/approaching-Kerche.jpg"
image parking = "images/unsplash-parking-sebastian-huxley.webp"
image bglight:
    zoom 2.0
    "images/bglight.webp"
image chlight:
    zoom 2.0
    "images/chlight.webp"
image shed = "images/unsplash-shed-ricky-kharawala.webp"
image nightfield = "images/unsplash-nightfield-artur-oliinyk.webp"
image vase = "images/unsplash-vase-kamilla-isalieva.webp"

################################################################################

# The game starts here.

label start:

############################################### ANNA POV ###############################################
scene black with dissolve
stop music fadeout 3.0
pause 1.0
play ambient caronroad fadein 5.0
scene car at goodsize with Dissolve(5.0)

$ _window_show()

"According to Federico, the air conditioning in his car struggles every summer."

"The cool air, it seems, has run out for a while now, leaving it to blow warm air over the both of your
faces."

"You reach over and turn it off."

"It's marginally better."

"The heat makes you sleepy, and the rolling hills of the countryside are hypnotising."

pause 1.0

"Does this friend of his make this drive every day?"

"What kind of person is he?"

#pause 1.0

"Raimondo, from high school."

pause 1.0

"You haven't met any of his friends from his hometown before. He doesn't talk about them much."

"They exist in some vaguely defined “before” or “elsewhere” along with his parents and his Xbox."

"It's easy to forget, when you're surrounded by school, school, school, that there is an entire world
outside of research paper deadlines and the campus mall."

MCF "You see it?"

"You sit up and look forward. Off to the left, in the distance, the trees become orderly. There are
flowers, and a large, rectangular building beyond it."

MCF concerned "You aren't excited?"

MCA side "No, I'm… I'm just tired."

scene black with dissolve
pause 0.1
scene approaching at truecenter:
    zoom 0.5
    matrixcolor BrightnessMatrix(-0.2)
with dissolve

pause 2.0

MCA side "It's big."

MCF neutral "Right?"

"You've come across these kinds of places in the nooks and crannies of Padua: abandoned villas of the
long-dead well-to-do."

"But here there's so much space."

"Carefully trimmed trees and rows of flower beds line the road to the main building."

scene black with dissolve

"Federico turns off into a small gravel field—the parking lot."

"There are only a few cars in it at this time of day, however."

"He parks at the far corner in the shadows of a bushy tree and a single hedge."

#"Stop ambient (car engine)"
stop ambient fadeout 3.0

"You're not trespassing (yet)."

"But he is parking in a particularly out-of-the-way spot."

pause 1.0

MCF "You ready?"

MCA side concerned "…"

MCF "It'll be fine."

pause 1.0

MCA neutral "All right."

scene parking at truecenter
with dissolve

play ambient crickets fadein 3.0

pause 5.0

MCA side "Do you know what Raimondo is wishing for?"

show fed at center:
    xzoom -1.0
with dissolve

F "No."

MCA "I thought you'd tell each other everything."

F "Not everything, no."

F "It's like birthday wishes. You don't announce them before you blow out the candles."

MCA concerned "Hm."

F "If I had to guess, it could be finding a boyfriend? Pickings are pretty slim out here."

MCA neutral "He can't go to the city for that?"

F "Well. I don't know."

#"(Scene bg garden/road)?"

"You don't ask him what his wish is. It would be fishing for a compliment, and besides, he just said they
were secret."

"Walking with him along the rows of flowers in the golden hour is enough."

"This could be your wish. Slow evening walks with Federico, just the two of you and the crickets. A little night music."

scene black with dissolve
pause 0.1
scene meetup at center:
    xalign 1.0 zoom 0.5
with dissolve

"But before long, you reach the great double doors to the Villa von Radetz. A wolf in a hoodie sits on the steps, reading a pocket-sized paperback."

"He gets up to greet you."

show rai happy at center:
    yoffset -700 zoom 0.4 xzoom -1.0
show fed at center:
    xoffset -1300 yoffset -700 zoom 0.4
with dissolve

R "Hey, Fede!"

show fed neutral

"…You didn't know they made hoodies in that pattern."

F "Rai!"

show fed happy:
    linear 3.0 xoffset -300
$ renpy.pause (2.99,hard=True)

"Federico lets go of your hand to do some kind of boy handshake with Raimondo."

show rai neutral

F "This is Anna."

show fed neutral
camera:
    xalign 0.5 yalign 0.5
    linear 5.0 zoom 1.5

F "Anna, this is Raimondo. My best friend."

MCA happy side "Nice to meet you."

R "You too."

pause 2.0

show rai happy

R "So, I assume Federico's already familiarized you with the story of Lady Giuditta?"

MCA "The vigil, right? We stay until sunrise and then…?"

show rai mad

R "The vigil is based on the {i}legend{/i} of Lady Giuditta. But okay."

show rai neutral

R "According to the legends, if you stay the night inside the villa all the way until sunrise, Lady Giuditta
will grant your wish."

R "People wish for a lot of things, but it's mostly love and money."

MCA neutral "Why?"

R "Because of the {i}real{/i} story that I'll tell you later."

show rai happy

R "Anyways, we'll go touch her jewelry, make our wishes, and then her spirit will appear in her old
dressing room!"

show fed happy

F "Stop bullshitting, Rai."

show fed neutral

R "We don't know that her spirit {i}won't{/i} appear."

MCA concerned "Don't you stay overnight every night?"

R "Yeah, but I don't fondle her jewelry. Besides, you need at least two people."

show rai neutral

R "Anyways, we can't go in yet."

R "I can show you my digs in the meantime."

scene black with dissolve

"He takes you to something like a gardening shed around the side of the villa. You can't tell if it's part of
the original construction, but it's clearly not {i}new{/i}."

"He opens the door and traipses right in. It's dark inside. Federico follows right on his tail and for a
moment you are alone."

"You could turn around right now. You don't have to go in."

"But you came here for a reason."

#"You step into the darkness."

stop ambient fadeout 5.0

scene black with Dissolve(5.0)

camera

############################################### FEDE POV ###############################################

$ pov = "fede"

#"Scene black"

"I can tell from the sound of Rai's steps that he slows down almost immediately."

play sound lightswitch

"And then with a click, I'm blinded by the light."

show shed at goodsize

"A bare incandescent bulb dangles from the low ceiling. It was clearly intended to be filtered by some
sort of lampshade."

"Still, its barren appearance matches the room, finally revealed to us in all its disappointing glory."

"It's just a storage space, barely two square meters, filled to the brim with junk that looks as old as the
villa itself."

"A metal garden chair sits awkwardly in the middle of the shed, white paint peeling with age."

"My face heats up and I make a half-hearted attempt to block the view from the doorway."

"I don't dare look back towards Anna. I had hyped up this place so much, and now it feels like letting
her see my messy bedroom once again."

show rai happy
with dissolve

R "Welcome to my kingdom!"

"Rai sounds genuinely proud of this junkyard."

"There was definitely a time when I would have shared his innocent enthusiasm."

"Before I started dating Anna, I didn't know how gross something could look through the eyes of
adults, like we're supposed to be." #TODO

MCF concerned "These are your digs?"

show rai neutral

R "Yeah. I change here, keep my stuff here. We don't have storage lockers in the main building."

show rai:
    linear 1.0 xalign 0.0
show ann concerned at right with dissolve:
    xzoom -1.0

A "At least you have a place to sit."

"I feel myself sinking at her deadpan delivery, but if Rai understands she's damning the room decor with
faint praise, he doesn't show it."

"I try to speak to him in a language he'll understand."

MCF happy "I hope this isn't what they're showing the tourists. We didn't pay for no ticket and I still feel like we're
getting ripped off."

show rai annoyed

R "Cool your jets, the show hasn't started."

show rai neutral

R "And besides."

show rai:
    linear 1.0 yalign 0.5
$ renpy.pause (1.0,hard=True)
show rai:
    linear 1.5 yalign 1.0

"He grabs something from the floor."

show rai happy

R "Here's something to make up for the lame start."

show rai neutral
show ann concerned

"He hands us each a bottle of beer."

#clinking sound
pause 1.0

MCF neutral "Mmm, warm beer."

show rai annoyed

R "Sorry, Your Majesty. As you can see, they don't provide us humble employees with a mini fridge."

show rai happy
show ann neutral

R "Cheers!"

"It had taken a moment to slip back into our normal routine, but now it all feels so natural."

"Of course Raimondo was making no attempt to impress me."

"Anna will have to live with it, for tonight at least."

show rai neutral

A "Is there a reason why we're drinking here, of all places? Why don't we go inside?"

"Rai cranes his neck toward a large, white clock on the opposite wall. I had just assumed it was broken."

R "A few more minutes. There's a cleaning lady who's here until ten on Wednesdays."

show ann sad

A "Ten o'clock?"

F "I'm assuming they don't want her to be cleaning while the visitors are here."

A "But the villa's so far from everything."

show ann mad

"She makes a vague gesture in the direction of the door. I can tell by the way she's furrowing her brows, 
she thinks Rai is being deliberately obtuse by not catching her drift."

A "You'd have to walk to the parking lot in the dark."

A "Alone."

show ann concerned

R "Ah! But she's not alone."

show rai happy

R "I'm right here!"

"He points at himself with his beer bottle. From his proud smug grin, you would think he's actually rescuing women in the parking lot every other week."

"Anna just shakes her head, defeated."

show rai neutral

R "I'll go make a round of the place to make sure it's empty. You two can sit tight here."

"I really don\'t want to be alone in this mess with Anna."

A "I'd prefer to be outside in the garden, if you don't mind."

MCF "It {i}is{/i} dark now."

R "I'll find you when I'm done."

play ambient crickets fadein 3.0
scene black with dissolve
pause 2.0#0.1
show nightfield at goodsize
show gagmoment at goodsize:
    anchor(1.0,0.0) pos(-500,0)
with dissolve
play music uncertainfutures
"Such a pleasant night."

"The few lights around the outside of the villa are the only sources of light for a few miles at least."

"The nearby towns shine in the distance like lighthouses competing to attract a ship."

"And yet the darkness is warm, inviting."

"During summer, night doesn't feel like the end of a day, but rather the beginning of exciting new adventures."

"Anna is standing there, with her back to the villa, peering into the black fields that are singing with the voices of a million cicadas."

"No, not cicadas. Cicadas are louder."

"These are crickets."

show ann concerned at center with dissolve:
    matrixcolor BrightnessMatrix(-0.2)

A "Is he coming back soon?"

MCF "He's just being thorough. I'm sure the cleaning lady hasn't left yet."

hide ann with dissolve

"She turns her head away again."

MCF "Are you ok?"

"I approach her and wrap my arm around her shoulders."

MCA side neutral "Yes."

"I give her time. Just like I learned from her."

MCA sad "I don't know… This feels so stupid."

"I rub her shoulder in a reassuring way, fighting the urge to defend my idea."

MCA "I didn't realize it would be this far out. And what we're doing is still illegal."

MCF "Well, the two things go well together, don't they? No one will see us."

MCF "Plus, I don't even know if this counts as illegal. Rai has the keys and he's letting us in."

"I don't know if I really believe my own bullshit."

"That had been my assumption when discussing this whole monkey business with Rai. But Anna has the ability to reveal childish stupid behaviors for what they are."

"Even if she is right, I'm not letting her discourage me. There's too much at stake."

"I give her a kiss she's happy to receive."

"That's my girl. Let's be childish together."

"Just this once."

stop music fadeout 5.0

"As if it was a sign from the divine providence, we finally see the red taillights of a vehicle driving away down the road we came from."

show nightfield:
    linear 2.0 xpos(2.0)
pause 1.0
show gagmoment at goodsize:
    linear 2.0 xpos(1.0)

pause 3.0

show rai:
    zoom 0.3
    xpos(850) ypos(-150)
    matrixcolor BrightnessMatrix(-0.2)
with dissolve

R "So are you ready or what?"

show rai annoyed

R "Geez, guys, I have nothing against straight people, but do keep it in the bedroom."

#####

scene black with dissolve
pause 0.1
show entrydoor at top with dissolve:
    zoom 0.65
play sound chord1
pause 5.0
show entrydoor:
    linear (5.0) ypos(-1.0)

"The doors are old and massive."

"If both were open at the same time, all three of us could walk inside arm in arm and still have plenty of room for others to join us."

play sound chord2

"When Raimondo and I talked about sneaking in, I couldn't imagine we would enter through {i}this{/i} kind of door."

play sound keys

"But Raimondo is fidgeting with some oversized keys, unperturbed."
play sound unlock
"Click."

"Such a satisfying heavy sound. A modern lock would be far less dramatic."

play sound chord3

MCA side "That's inconvenient that you have to do this every time with the old lock."

MCR "Yep. I need to make sure this door stays locked at all times once I'm on shift. Can't have anyone sneaking inside."

MCR happy "To be honest, this trusty rusty door does half of the job for me."

scene black with dissolve

play sound chord4
play audio doorcreak
stop ambient fadeout 3.0
"He pushes the doors with both hands."

show entryway at goodsize:
    matrixcolor BrightnessMatrix(-0.5)
show rai at center:
    matrixcolor BrightnessMatrix(-0.5)
    zoom 0.4 yoffset -700
with dissolve

R "Madame and monsieur, welcome to Maison von Radetz."

"Raimondo enters the building with a stride, but I find myself hesitating as soon as I cross the threshold."

"The darkness inside the building feels so different compared to the outside. Despite his words, I do not feel welcome."

"The silence weighs heavy, the high ceilings and large room disorient me."

"Is this all in my head? Or are the ghost stories real?"

"A cat can hope."

A "Where's the light?"

"For a moment I worry Anna might be frightened. Instead, I see her tentatively stepping deeper into the room."

play sound flashlight

# light
show entryway at goodsize:
    matrixcolor BrightnessMatrix(0.0)
show bglight behind rai at truecenter
show rai at center:
    matrixcolor BrightnessMatrix(-0.2)
show chlight at truecenter

"A flashlight."

R "Here. I have another one."

MCF concerned "Really, man? Are there no normal lights?"

R "Of course there are, if you want to broadcast to everyone in a few miles radius someone is still inside."

R "Sorry, but these will have to do."

"I feel stupid for having asked. Rai hands me the other flashlight, before going back to close the door again."

MCF neutral "Here, Anna, you can have this one."

show ann base happy at left:
    matrixcolor BrightnessMatrix(-0.2) xzoom -1.0
with dissolve

A "A proper gentleman."

"She sounds genuinely pleased and I'm happy to have made her happy."

show rai gag meee

"Rai, on the other hand, fakes a gagging motion while Anna is shining her light in another direction."

"And I'm happy to reciprocate his masculine sign of affection with a friendly middle finger."

show rai neutral
pause 0.5
show rai base

A "It's fancier on the inside."

show ann:
    xzoom 1.0
with dissolve

"She turns to me."

A "Maybe we should come back and visit it properly. It must be even more lovely during the day."

R "I don't know. I think the night adds to the charm."

R "Don't you think, Fede?"

MCF "I'll have to side with Anna. My ma brought me here when I was little, and I remember all the bright colors making an impression on me."

MCF concerned "Now, everything feels cold."

"“Dead,” is what I want to say, but I want to steer clear of the topic for now."

show rai annoyed

pause 2.0

show rai neutral at center:
    matrixcolor BrightnessMatrix(-0.2)
    zoom 0.4 yoffset -700

"Rai surprises me with an annoyed look that disappears as quickly as it came."

"Was that a trick of the light?"

R "Thankfully I have this whole night to educate you two."

R "Now it's the best time to visit because we get to do what we like! No pesky compulsory tour."

R "Follow me, I'll show you two around."

scene black with dissolve

"Rai's light walks with confidence towards a large flight of stairs."

MCF concerned "So much for no pesky tour."

show vase at goodsize with dissolve

"I turn towards Anna's light, which is still pointed towards a vase resting on a half pillar column behind a glass in the hallway."

"I take her hand, startling her. It occurs to me that between my black fur and me not having a flashlight, I must be as invisible as a ghost."

MCF "Everything ok? Should we follow him?"

MCA side happy "Yeah."

scene black with dissolve
pause 0.1
show grandstairs at goodsize
with dissolve

"Raimondo's light has disappeared above the stairs. He must have reached the next floor already."

"We ascend, hand in hand. Despite the wide steps, there's a childish part of me who would like to climb up two at a time."

"But I doubt I would be able to do it while dragging Anna along."

MCA side happy "You know, this is romantic."

"Now that she says it, I could picture this same scene taking place with wedding music and formal clothing."

MCA sad "Makes me wish it'd be just the two of us."

"She whispers it, as if to herself. Still it stops me dead in my tracks, and I perk my ears, worried her words might echo their way to Raimondo."

"She shines her light in my direction."

MCA neutral "I didn't mean it like that."

MCA happy "Your friend seems fine. Really."

"She squeezes my hand in reassurance. She resumes her ascent, and I follow her with heavier steps."

scene black with dissolve
pause 1.0
show hallway at center:
    zoom 0.5
show rai at center:
    matrixcolor BrightnessMatrix(-0.2)
with dissolve

"When we reach the landing, we find Raimondo waiting."

R "Finally, you slowpokes."

R "Do I wanna know what took you so long?"

show rai:
    linear 2.0 xalign (0.0)
pause 1.0
show ann happy at right with dissolve:
    matrixcolor BrightnessMatrix(-0.2) xzoom -1.0

"Anna responds before I can think of an excuse."

A "You were right. This place is rather charming."

show rai happy

R "Oh, you ain't seen nothing yet. Here's where they keep all the cool exhibits."

show rai neutral

"He points his light towards the wall. There's a placard with directions, so I get close enough to read it."

"Not that I need to, as Raimondo is all too eager to explain what they say."

R "This way…"

show rai:
    linear 2.0 xalign (1.0)
show ann:
    linear 2.0 xalign (0.0)
pause 2.1
show ann:
    xzoom 1.0

"He turns to the right of the stairs."

R "Is where they keep all the interesting originals of the von Radetz family. Things that belonged to them, recreation of how the rooms looked, that kind of stuff."

R "And this way…"

show rai meee

"He points towards a smaller entrance."

R "It's the lady's private quarters. They have an exhibition about “Women Through History”."

R "It was supposed to be temporary, but they've kept it for five years straight, so I think it's permanent by now."

show ann neutral
show rai base

A "Oh? How… topical."

"Rai makes a “so and so” gesture with his hand."

R "It starts out nice enough, but the last few rooms about “modern women” stick like a sore thumb."

MCF "How bad could it—"

show rai mad

R "The last room is about “Women CEOs”."

MCF concerned "Ah…"

show rai neutral

"I point at the placard next to me."

MCF neutral "What about that other arrow?"

"It's hard to make the words out, but I can see there's a third arrow besides “left” and “right”."

"A curvy one, pointing towards the stairs and the next floor above."

R "That's the temporary exhibition. {i}Really{/i} temporary, I mean."

R "Again, it's a bit of an eyesore. What was it again?"

show rai:
    xzoom -1.0

"He approaches the placard and squints his eyes to read it, like I was attempting to do. But unlike me, he has a flashlight."

R "‘Threads of Dreams: The Sense of Whimsy of the Modern Man.’"

show rai gag meee

R "Modern art garbage."

show rai mad base
show ann concerned

A "Modern art is not garbage."

"Her voice is soft, but it has an edge. Like she's stating a fact. I jump in to save Rai from any further controversial opinions."

show ann neutral

MCF neutral "We could check that out as well."

"I don't know I would have given the idea a second thought myself, if Anna wasn't here. But she can appreciate beauty in a lot more things than I do."

"And she is often infectious when she does."

show rai annoyed

R "Yeahhh okay, maybe later."

"Rai doesn't sound particularly convincing."

show rai happy

"But his voice fills with excitement again when he moves back to the original topic. He can be pretty infectious as well."

R "I want to show you the {i}cool{/i} stuff first."

show rai meee

"He shows us his key ring, which emits a nice metal sound as he makes the keys jingle."

R "Including some things only I have the ticket to."

scene black with dissolve
pause 1.0

"We follow him as he picks a direction for our tourless tour through the villa; he ends up picking the right."

show chimney at goodsize with dissolve

"As promised, this part of the villa is kept close to its original glory."

scene black with dissolve
pause 0.1
show bathroom at truecenter with dissolve

"We enter a few rooms, one after the other, and it's pretty easy to guess from the furniture what the original purpose of each room would have been."

scene black with dissolve
pause 0.1
show livingroom at truecenter with dissolve:
    zoom 0.4

"A couple of sofas, yellowed by time, placed around a low rococo coffee table. Probably some kind of living room."

scene black with dissolve

"A square room with a rectangular table in the center, and empty wooden bookshelves against each wall. Obviously the library."

scene black with dissolve
pause 0.1
show bouquet at truecenter:
    zoom 0.4
with dissolve

"The rooms follow one after the other, with no hallway or transition in between."

"It's impressive, but I feel like walking through a movie set."

scene black with dissolve
pause 0.1
show fancychair at truecenter with dissolve:
    zoom 0.4

"It's pretty obvious no one has sat on that chair over there in a long time. No one probably will ever again."

scene black with dissolve
pause 0.1
show china at top with dissolve:
    zoom 0.7

"What makes it exciting, like Raimondo had promised, is doing this at night."

scene black with dissolve
pause 0.1
show dove at truecenter with dissolve:
    zoom 0.7

"It's like we're crossing boundaries we were not supposed to cross."

"I often surprise myself being on the lookout for ghosts angry at this violation of their home, more so than admiring the historical decorations."

"Do I even believe in ghosts? I'm of two minds."

"On one hand, I {i}know{/i} ghosts don't exist. They can't."

"They're stories we've inherited by ancestors who didn't fully understand how the world works."

"On the other hand… Well, I did choose to come here, didn't I?"

"Raimondo finally stops all of a sudden, and I realize Anna hasn't spoken in what feels like a long time."

scene black with Dissolve(5.0)
pause 0.1

############################################### ANNA POV ###############################################

$ pov = "anna"

show ladyportrait at top:
    zoom 0.4
show chlight at truecenter:
    zoom 0.5
with Dissolve(5.0)

play music musicbox

"A large family portrait hangs in a sitting room. There are other paintings around, but this one—this one
is {i}displayed{/i}."

"You noticed it even in the dark."

"A white cat in a ruffled dress—"

"—she looks like you, but with shorter hair—"

"—sits on an upholstered sofa next to an otter in a stiff, shiny-buttoned jacket. Their hands are close,
but not quite touching."

"Would this painting have been scandalous, back in its time?"

"Off to the side is a red fox dressed in black, pouring tea."

"An attendant."

MCA side "Who are they?"

#"Show Raimondo"

show rai at left:
    matrixcolor BrightnessMatrix(-0.2)
with dissolve

R "Giuditta and Ferdinand. The Lady and Lord von Radetz."

show fed concerned at right:
    xzoom -1.0
    matrixcolor BrightnessMatrix(-0.1)
with dissolve

F "Lady and Lord?"

show rai happy

R "The Lady is more important."

show rai neutral
hide fed with dissolve

R "She was once Giuditta the embroideress, from a family of needleworkers—what used to be the middle class back then."

R "She was never the face of the family business—her father and brother were more well-known before this—but one day she got some 
high-profile work for the von Radetzes."

R "She wasn't even their first choice: her father had fallen ill, her brother was off visiting his wife's family."

R "But the von Radetzes had an embroidery emergency."

R "An elaborate wall hanging depicting the birth of Jesus had been ruined by one of the young children, and needed restoring before the 
Archbishop's visit the next day."

R "We're talking golden threads and gemstones here, by the way. Fancy-ass wall hanging."

R "Anyways, they couldn't wait for Giuditta's father to get better, or for her brother to come back to town."

R "So they settled, begrudgingly, for Giuditta."

R "She stayed here all night fixing it."

R "During the night, the eldest son, Ferdinand, couldn't sleep, and he found her at work."

R "She told him stories as she sewed. One after the other, until the sun came up and the embroidery was complete."

R "He was so captivated that that very day he presented her to his parents as his bride-to-be."

R "And so Giuditta the embroideress became Giuditta the lady."

"A veritable Cinderella story. You can see why people come here to wish for love."

R "In reality, Ferdinand marrying a commoner caused a bit of a scandal back then, but the locals found it very inspirational."

R "All accounts indicate the von Radetz family enjoyed a long-lasting popularity after that union. Even when the Habsburgs didn't."

R "The wall hanging was unfortunately lost in a fire, but according to the records…"

stop music fadeout 10.0

############################################### FEDE POV ###############################################

$ pov = "fede"

R "Blah blah"

R "Blah blah blah blah blah blah blah blah blah {size=30}blah blah blah blah blah blah blah blah blah {/size}{size=20}blah blah blah blah blah blah blah blah blah {/size}{size=10}blah blah blah blah blah blah blah blah blah {/size}{size=5}blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah{/size}" #smaller and smaller

"{cps=0}{size=5}Blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah{/size}{/cps}{w=5.0}{nw}" #smaller and smaller

scene black with Dissolve(5.0)
pause 1.0
scene classroomcg2 at goodsize with Dissolve(5.0)

N "It was the first week of the second year of university."

N "My first elective."

N "I was already starting to wonder if I had made the right choice, choosing economics."

N "I'm sure everyone goes through it at some point. Wondering if you're wasting your time."

N "If this choice you had made half-heartedly, just because the time had come to make one, was the right one.
The one you wanted to be stuck with for the rest of your life."

N "I guess that was the reason I was there, in the first class of that particular elective none of my friends had chosen."

N "After barely getting through the first year of classes, this subject looked the only one that may, maybe, rekindle my interest for this course."

N "But as I was sitting among unfamiliar faces in that small room, I was having second thoughts about that choice as well."

N "When she sat next to me, I was shocked."

scene classroomcg at goodsize with Dissolve(5.0)

N "Looking back now, she probably did that without even thinking about it."

N "I doubt she even noticed me."

N "She looked like the kind of girls that had everything figured out."

N "She immediately took out a few books out of her bag and spread her notes on the desk. Every movement she made was so precise,
intentional."

N "She was so close I could smell the faintest fragrance coming from her."

N "You could tell, just by looking at her, that every detail of her appearance had been chosen with care."

N "It must have been the first moment that made me realize that I was attending a college lecture in a sweatshirt, the kind 
I used to wear back in high school."

N "The moment I realized she was not a girl, but a woman. And I was still a boy, who had scarce experience with either."

N "It would have been easy—I felt—saying hello, had she been a he."

N "But she was a woman, and any start felt like a false start."

N "So I just sat there, pretending not to notice her, letting the lecture begin without even saying “hi”."

N "It was only when I noticed a music sheet among her notes, that I asked her, without even thinking."

FFB "Hey, what's that?"

A "{i}Mmm?{/i}"

A "{i}Oh, this is Verdi.{/i}"

#[beat]

FFB "Do you like opera?"

N "She did, in fact."

N "Even though I'd always had a fascination with music, I knew very little about it."

N "My parents had tried to get me to learn the piano, but I never went beyond a few basic lessons."

N "And I knew nothing about opera, or classical music in general. But eventually, I got her to invite me."

N "Or, I guess I invited her, but I asked her to pick the play."

N "I loved it."

N "It was Verdi, of course."

scene black with Dissolve(5.0)

pause

R "Right, Fede?"

F "What?"

show ladyportrait at top:
    zoom 0.4
show chlight at truecenter:
    zoom 0.5
show rai happy at left:
    matrixcolor BrightnessMatrix(-0.2)
show ann concerned at right:
    xzoom -1.0
    matrixcolor BrightnessMatrix(-0.2)

R "Just messing with you."

#"show raimondo neutral"
show rai neutral

R "I forgot that you two aren't usually up this late. You should hit your second wind soon."

R "We can check out the women's exhibits next then."

scene black with Dissolve(5.0)
pause 0.1

############################################### ANNA POV ###############################################

$ pov = "anna"

show wardrobe at truecenter with Dissolve(5.0):
    zoom 0.4

"…"

"Raimondo is right: the lack of sleep is catching up with you."

"“Women Through History” threatens to bore the both of you into napping standing up."

"You're glad the exhibit exists, of course, but so much of it is text on placards."

scene black with dissolve
pause 0.1
show womenthru at truecenter:
    zoom 0.4
show chlight at truecenter:
    zoom 0.5
with dissolve

"You starts recognizing names when it reaches the modern day, but otherwise nothing sticks with you."

"There's only one flashlight between you and Federico, and you read faster than him."

"You slow the pace down, but you're not sure if he's actually reading."

"You turn to check if Federico is done, but he's off in the other room looking at something in the dark.
Or pretending to."

#"Show raimondo neutral"

"Raimondo hasn't been too interested in the exhibits. He's had a long time to familiarize himself with
them, especially this one."

"There's a quiet between you."

MCA side happy "Hey, Raimondo."

show rai neutral at center:
    matrixcolor BrightnessMatrix(-0.2)
with dissolve

R "Yeah?"

MCA "Are you wishing for money or love?"

R "Who's to say I'm not wishing for a third thing?"

MCA concerned "You're just like Fede."

show rai happy

R "I'll take that as a compliment."

MCA happy "How did you two meet?"

show rai neutral

R "We've always been going to the same schools, all the way back since elementary school. Small
town, you know?"

R "But we didn't really start talking to each other until we were on the volleyball team together in middle
school."

R "And then it's like… poof! We begged our teachers to make sure we'd end up in the same class in
high school."

MCA "I know the feeling. I used to play too. You can get really close with people that way."

R "Cool. What position did you play?"

show rai:
    linear 2.0 xalign 0.0
pause 0.1
show fed at right:
    xzoom -1.0
    matrixcolor BrightnessMatrix(-0.1)
with dissolve

F "I didn't know you used to play volleyball."

#"Show anna serious"

MCA neutral "It was a long time ago."

F "Why'd you stop?"

MCA "Why does anyone stop, Federico?"

#"Hide f"

#"Hide r"

scene black with dissolve

"You step into the next exhibit."

show weddingdress at truecenter:
    zoom 0.5
show chlight at truecenter:
    zoom 0.5
with dissolve

#"Scene bg dress"

"A woman on the other side of the room, waiting for you."

"No, a dress on a mannequin."

"A mannequin with no face, pointed towards the exit of the “Modern Women” exhibit, wooden hands
folded in front of her."

"The silk brocade shimmers under the light of your flashlight. Red and orange threads bordered with
gold clasps on velvet."

"It's beautiful."

"Further down the skirt are pieces of turquoise sequins embroidered into the fabric. Not sequins; they're
longer than that."

"Horn shavings? But they're iridescent."

"Looking at the colors shift under your flashlight as you move it around is hypnotizing."

#"Show raimondo neutral"

R "They're beetle shells."

"You turn to Raimondo."

show rai neutral at left:
    matrixcolor BrightnessMatrix(-0.2)
with dissolve

R "Sorry. Didn't mean to spook you."

"Had you jumped? Turned too fast?"

R "They were popular in 19th century England. Some made their way over here."

R "Originally all the way from India. Colonialism and all that."

R "But they're pretty, aren't they?"

MCA side "Can you imagine wearing something like that? Little bug pieces all over your skirt?"

"{i}But they're pretty, aren't they?{/i}"

show rai gag

R "I think I'd rather get married in a suit."

MCA concerned "Married?"

show rai happy meee

R "Hey, I can always move to a city with a civil union registry."

"This doesn\'t answer your question."

show rai neutral base

R "Oh. Yeah, this is her wedding dress. They weren't all white until fairly recently in the broad history of
things."

show rai happy

R "I'm surprised you didn't know."

"There's a sting to this, but he probably doesn't mean anything by it."

MCA concerned "I guess sometimes you assume that things are always like this. The way they are now, I mean."

show rai neutral

R "That's history for you."

"You shine your flashlight over the nearby placards. A brief history of wedding dresses, beetle elytra embroidery, imported silks."

MCA neutral "Where did Federico go?"

show rai mad

R "He's chilling out by the entrance to “Women Through History”."

MCA concerned "I'm not mad."

show rai neutral

R "Didn't say you were."

MCA concerned "…"

#"Sting. "

#extend "Twice."

MCA "We can head back."

scene black with Dissolve(5.0)
pause 0.1

############################################### FEDE POV ###############################################

$ pov = "fede"

show wardrobe at truecenter with Dissolve(5.0):
    zoom 0.4

"The two of them come back to the front of the exhibit, and we group back up before heading to the
lady's quarters."

"It's a small room with jewelry displays past velvet cordons. Rai moves them to let us in."

show rai neutral meee at left:
    matrixcolor BrightnessMatrix(-0.2)
show ann neutral at right:
    xzoom -1.0
    matrixcolor BrightnessMatrix(-0.2)
with dissolve

R "I'm going first."

hide rai with dissolve

"He uses one of his keys (one of the smaller ones this time), to slide a glass. He grabs a necklace with a big pendant."

show rai neutral meee at left:
    matrixcolor BrightnessMatrix(-0.2)
with dissolve

R "This one's actually from before she became Lady."

R "Maybe that makes it lucky."

"There's something on his face again. I can feel it, even in the dark."

show rai closed

"He closes his eyes dramatically, then opens them after a couple of seconds."

show rai open

R "Who's next?"

MCF neutral "Ladies first."

show rai happy meee

R "I already went."

show ann concerned
show rai neutral base

"Anna doesn't entertain the joke."

show ann closed openpaw

"She holds the pendant to her chest and looks the least confident I've ever seen her, though I'm not
sure if it's the darkness."

"Is she not wishing for us to be together?"

"Or worse: she is, and this is how unsure she looks."

show ann open

"I walk over past the cordons and take the pendant she offers."

show ann base

"It's heavy. Gold, maybe."

scene black with dissolve

"I close my eyes and wish."

centered "That after everything I have to tell her tonight, she'll stay with me."

pause 5.0

"Eventually we get to the point where even Rai's enthusiasm is flagging."

"We've ticked off all the big things that he wanted to show us, and besides that, it gets hard for me and
Anna to keep all this information in our heads."

"The tour stops."

"Rai disappears somewhere, and returns with three styrofoam cups of instant noodles and some
individually wrapped cookies like you might find in a convenience store."

"I forgot about food."

"We wander—all three of us, sometimes, or two of us in various combinations."

show ann at center:
    matrixcolor BrightnessMatrix(-0.2)
with dissolve

"When I'm alone with Anna, I think about telling her, but I keep putting it off until we split up or Rai is
back."

hide ann with dissolve
show rai happy at center:
    matrixcolor BrightnessMatrix(-0.2)
with dissolve

"When I'm alone with Rai, he takes my mind off of it with talk of new games, stories of crazy tourists,
what our old classmates have been up to. But it can only last so long."

hide rai with dissolve

"When I'm alone with myself… that's the worst."

#"Scene bg anteroom"
show anteroom at truecenter with dissolve:
    zoom 0.5

"It's the three of us now in a small anteroom with no windows to the outside."

"There's a little lamp and a divan, where Anna reads one of the thrillers Rai keeps to occupy himself on
long nights."

"Rai sits on the floor opposite her, drawing in a large sketchpad. There's a lot to draw in a place like
this, and tonight he has a new subject."

"I clear my throat."

MCF concerned "I—uh."

show rai neutral at left:
    matrixcolor BrightnessMatrix(-0.2)
show ann neutral at right:
    xzoom -1.0
    matrixcolor BrightnessMatrix(-0.2)
with dissolve

#"Show raimondo"

#"Show anna"

MCF neutral "I want to show you something."

R "What'd you find?"

MCF concerned "Just Anna, actually."

"I'm waiting for the remark about us going off together. The quip."

"It doesn’t come."

show rai sad

R "‘Kay."

show ann happy

A "Sure."

"She marks her place with a bookmark and sets it down on the seat."

scene black with dissolve

#"[f has flashlight, dunno how or if to indicate this before he puts it down]"

pause 5.0

A "It's an interesting story, but every time this Bianca is in the same room as the protagonist, it's like—"

"I don\'t know where I'm going. Just walking."

"Carpet. Wood. Tile. Doorways."

A "—of why he would do it. Remember, the ex-wife's been out of the picture for fifteen years at this point, and—"

"Why did I say “I want to show you something”?"

"I can't say “we need to talk.” No one wants to hear “we need to talk.”"

"But the two of them are serious, so they must know that I'm being serious. It must show on my face."

"I almost jump when Anna touches my hand."

MCA side concerned "Fede, what's going on?"

"She must know. She must know I don't know what I'm doing."

show livingroom at truecenter:
    zoom 0.4
show ann openpaw at center:
    matrixcolor BrightnessMatrix(-0.2)
with dissolve

"We stop in an entertainment room with lots of seats and a couple fancy dressers."

"As good a place as any."

"I set the flashlight down on a stack of hardcovers, facing up like a torch lamp."

"It's almost like normal lighting again."

"Do I sit? Do I stand?"

"Deep breaths."

"I stay standing."

MCF concerned "I have something to tell you."

A "Yes."

MCF "You know I like you. I enjoy being with you."

MCF "You're the prettiest girl I've ever met."

show ann sad

A "Where is this going?"

MCF "I like men."

#"Show Anna surprised"

show ann concerned
pause 1.0
show ann neutral

"There. Band-aid ripped off."

"Shit."

MCF "I {i}also{/i} like men, I mean."

MCF "I used to think I might be gay, but then a girl would come along and I definitely wasn't gay."

MCF "It would keep on for a while until I saw a guy who was… good-looking, and then, well, maybe. But
then… girls."

MCF "And you can still be straight and appreciate people's looks."

MCF "You know, I didn't want to be one of those guys where I can't say that someone looks
good just because they're also a guy."

MCF "I work out. I can respect the work."

MCF "But eventually I realised that's not what that was."

MCF "This is just how I am. I don't know why."

MCF "It doesn't change anything between us. I'm still attracted to you."

MCF "And I'm saying this all now because I just…"

MCF "I want you to know."

"I've been talking for a while, and she hasn't said anything."

"I can't tell if she's letting me talk, if she's listening, or what."

MCF "Anna?"

show ann concerned

A "So you're…"

MCF "I like both. And right now I—"

show ann mad

A "I know what a {i}bisexual{/i} is, Federico!"

"What?"

MCF mad "Don’t call me that."

"I hate the way it sounds in her mouth."

MCF "I don't get what this is. You're one hundred percent okay with Raimondo."

show ann angry base

A "I'm not dating Raimondo!"

A "I'm not bringing him home to my parents and telling them, “Hey, this might be your future son-in-law.”"

MCF "You haven't brought me—"

show ann mad

A "“Who, by the way, has probably had a dick in his mouth at some point.”"

show ann angry

MCF "Woah, woah, woah."

A "Well, have you?"

"This isn't how it was supposed to go."

"I came here to tell the truth, but now there's a louder part of me that wants—"

show ann concerned

A "It was Raimondo, wasn't it?"

#"Show fede portrait angry"

"Fuckin'—"

MCF "Don't act like your mouth ain't dirty too."

show ann mad

"This shuts her up."

play sound impact

hide ann with dissolve

#"Hide anna"

"She knocks the flashlight over."

"It spins once, twice, casting rolling shadows over the walls."

"She's gone."

scene black with Dissolve(5.0)
pause 5.0

############################################### ANNA POV ###############################################

$ pov = "anna"

show upstairs at truecenter with Dissolve(5.0):
    matrixcolor BrightnessMatrix(-0.2)
    zoom 0.6

"It's all right for straight men to have gay friends. Preferred, even. It means that they are open-minded
and able to respect people who are not like them."

"Whatever Raimondo did in his personal life was his own business."

"But now, of course, it's yours."

"Your life. Your business."

"Federico had made it so."

"You thought you had been good. Just because they were friends didn't mean anything had happened.
Boyfriends are allowed to have friends who are gay."

"But maybe you had just been stupid. How could you not have seen it?"

"Stupid."

"And now all you can see are images in your mind of them together. Tongues intertwining, hands
wandering."

"Federico gagging on it in the same bed you two had shared together."

pause 1.0

"They're probably together right now. Alone with each other."

"Because of you."

pause 2.0

"Let them."

scene black with Dissolve(5.0)
pause 0.1

############################################### FEDE POV ###############################################

$ pov = "fede"

show anteroom at truecenter:
    zoom 0.5
show rai mad at center:
    matrixcolor BrightnessMatrix(-0.2)
with Dissolve(5.0)

R "The fuck?"

R "Did she really say that?"

"Rai's presence was supposed to make things better. Give me strength."

"But now that things have gone south, I would have preferred to be alone. To have more time before having to tell someone else what had happened."

show rai sad

R "I'm sorry, Fede."

"I kick the nearest wall, managing only to hurt my foot. I grunt in pain."

"I don't want pity."

R "Hey, no need to take it out on the villa."

R "Let's sit a minute, ok?"

hide rai with dissolve

"He sits on a bench, intended for the tourists to pause and take in the room we're currently in."

"If it was anyone but Raimondo, I would have probably went outside already."

"I don't crave for company right now."

"But his voice has the right mixture of softness and understanding to lure me to come closer."

"I plomp down next to him."

#[beat]

"He’s not speaking, he's not even looking at me."

"If these were different circumstances, he would have looked like an actual tourist, contemplating the dresses on the mannequins."

"But his flashlight is pointing to the ground, instead of wherever his gaze is fixated to."

"So I just sit there playing with the strap on my watch, mulling over what just happened for a while."

"I had been scared to share that part of myself for a while now. But even then, I wasn't prepared for this kind of burning rejection."

MCF sad "I'm sorry I dragged you into this."

"Right now, that's the only thing I feel sure about."

MCR sad "Dude, you kidding?"

MCR neutral "I'm glad I can be here for you."

"A warmth spreads over my back, where he's making small stroking motions."

MCR "You think I haven't been through bad coming outs myself? I get you."

"If he did, he never shared it. I can't remember a time when Rai was not his smiling confident self."

"And after discovering Anna was not the person I thought she was, this too stings like a betrayal."

MCF sad "I sincerely doubt that."

"It came out more vitriolic than I intended."

MCF "I don't think you've ever had to worry about the person you're dating holding against you that you've sucked dicks before."

"My argument sounds silly the instant it escapes my lips. But at the same time, defending the uniqueness of my pain feels weirdly important."

"He neither confirms nor denies my accusation."

"Instead, he seems to find renewed interest in the exhibits around us."

MCF concerned "You have, haven't you?"

MCR neutral "Went out with a guy like that? Of course not. Who's ever heard of a gay guy being homophobic? That'd be totally absurd."

"I deserve this ridicule."

MCF mad "Well, maybe I'd have known if you'd told me!"

"Raimondo stares blankly into the void for a while. When he speaks again, he's weighing his words carefully."

MCR mad "Do you need someone to vent against, Federico? If that's what this is all about, I can lay and take it."

MCR "But I think you're angry at Anna, not me."

MCF "Yeah, of course I am!"

"That part is easy to admit."

"Raimondo seems to sense I'm not finished though."

"What he said earlier poked at something that's been in the back of my mind for a while now."

MCF "Maybe I'm a little angry at you too."

"Raimondo's light doesn't flicker."

MCF "You're acting all concerned now, but it feels like we don't talk anymore like we used to."

MCF "I don't really know what's going on in your life."

MCF "And you don't seem all that interested in knowing what's going on in mine."

MCF "I told you I'm dating this girl and you've never asked me any follow-up questions!"

#[beat]

MCR sad "Maybe you're right."

MCR "Had you been dating a guy, I would have been an insufferable gossip."

MCR neutral "I plead guilty."

MCR "I'd have given you no peace until you fessed up all his measurements, that's for sure!"

MCR sad "But with you going straight… It felt like we had less in common, you know? Less things to share."

MCF sad "Well…"

"I gesture towards the dark empty room, in the vague direction where Anna had left."

MCF "I think we've thoroughly established I'm not straight."

MCR "Yeah…"

MCR "You're right. I'm sorry."

MCR "I guess… I felt weird talking about gay stuff with you, once you started to talk about dating women."

"He plays with the drawstring of his hoodie for a bit."

"Finally, he smiles."

MCR neutral "That was really stupid of me. Can you forgive me?"

"It takes me by surprise."

"Not just his apology, but the realization I really needed to hear that."

"For once this night, I can lower my guard. The muscles I didn't realize I was tensing ache as I finally relax them."

MCF concerned "Of c-course."

"I have to fight back some tears. Raimondo closes the distance between us and hugs me tight."

"I reciprocate the embrace."

MCR sad "I'm so sorry it didn't work out with Anna."

MCR "She can't see how lucky she is."

"I lean my face against his shoulder. But he pulls away instead."

"He looks at me straight in eyes. His eyes shine with a pale green light in the dark, although not as intensely as a cat's."

"And then he kisses me."

"I'm assaulted by a taste I haven't felt in a long time."

"Anna has an intense flavor of mint. Monochrome."

"She always has some to pop into her mouth, and that was the flavor she liked for her toothpaste."

"Raimondo is like a whirlpool by comparison. He tastes of the noodles he ate, of the vape he smoked, of the beer he drank,
of {i}his{/i} breath…"

"He tastes like he had the last time we kissed like this."

"This time, though, I don't reciprocate."

"Raimondo hesitantly pulls away, the realization of his mistake written over his face."

"It's only after he's already moved his mouth away that I finally pull from the hug and get up."

MCF mad "What the hell, man."

"I can't deal with this. Not right now."

"It's my turn to storm away."

scene black with Dissolve(5.0)
pause 0.1

############################################### ANNA POV ###############################################

$ pov = "anna"

show wardrobe at truecenter with Dissolve(5.0):
    zoom 0.4

#show upstairs at truecenter with Dissolve(5.0):
#    matrixcolor BrightnessMatrix(-0.2)
#    zoom 0.6

"You hold Lady Giuditta's necklace in your palm. Its pendant is heavy, made out of some precious
metal of the olden days."

"Their happily ever after."

"This stunt, this rumour has brought you none of it."

"You imagine her spirit watching the three of you and laughing, and you want to toss the necklace into
the wall."

"There's no one around to stop you. So you do."

#"Play sound necklace_impact"

pause 0.5

#"Play sound necklace_impact_repeated (loop)"

"Over and over again."

"Will Raimondo get in trouble for this? Maybe."

"But this was his fault. Let him."

#"Stop sound"

play sound locket

"The pendant splits open."

"You're a mix of horrified and glad."

"You broke it, but on the other hand, {i}you broke it{/i}."

"There on the floor, evidence of the existence of Anna Averoldi."

"There's something inside. Stuffing?"

"You kneel down to look closer."

"It's hair. There are two kinds: one is white and straight, like Giuditta's in the painting. The other is a
bright red-orange."

"It does not match Ferdinand's."

scene black with Dissolve(5.0)

############################################### FEDE POV ###############################################

$ pov = "fede"

show ladyportrait at top:
    zoom 0.4
show chlight at truecenter:
    zoom 0.5
with Dissolve(5.0)

"What a crap night."

"Thank you a lot, Raimondo. And you too, you stupid ghost lady."

"You were supposed to help me."

"I shouldn't have brought her here, based on a silly superstition. I shouldn't have accepted Raimondo's idea."

"At least, if I wasn't here, I would have been home by now."

"I wouldn't need to worry about asking Raimondo to let me out."

"I could have let Anna catch a bus instead of having to worry about sharing the drive back."

"I stare at the Lady's portrait again. I ended up back in this room."

#[beat]

"Portraits back then always looked so sad."

"Or was she, maybe, sad for real?"

"Was it wrong for me to expect this dead stranger to lend me a hand in my hour of need?"

#[beat]

"“{i}Spend a whole night there, just like she did back then.”{/i}"

"I peek out of the closest window, in between the gaps in the decrepit shutters."

"The sky is still dark. I guess even if the legend was true, it wouldn't have kicked in yet."

"I look back at the lady's eyes. It feels like she's trying to tell me something."

"Is she judging me? Is she sad for me?"

"Is she trying to tell me something about herself?"

scene black with dissolve

"I step away, having had enough of this room."

show spooky at truecenter:
    zoom 0.5
    matrixcolor BrightnessMatrix(-0.2)
show chlight at truecenter:
    zoom 0.5
with dissolve

"I venture down a hallway I'm pretty sure I haven't been in before. Hoping I don't stumble into anyone else."

"The window at the end of the corridor has no shutters. The light of the moon is pouring in."

"I can just make out the shapes of some beast I can't identify."

"I freeze in my tracks, a primeval instinct in the back of my head yelling at me to run away. Has some wild animal snuck inside?"

#[reveal of the statues]

show spooky2 behind chlight at truecenter:
    zoom 0.5
with dissolve

"Oh."

"They're just sculptures."

"This place has so many random exhibits."

show wolfies at truecenter:
    zoom 0.5
    matrixcolor BrightnessMatrix(-0.2)
show chlight at truecenter:
    zoom 0.5
with dissolve

"They're feral wolves. Three of them."

"What a curious coincidence. Although, I guess only one of us is a wolf."

"Is this the Lady trying to tell me something again?"

"What could she be trying to tell? Stick together, travel in packs?"

"Wolves have this reputation, after their feral brethren, of always being loyal to each other."

"I think back to Raimondo and his kiss."

"I think back to what Anna said."

scene black with dissolve

A "{i}It was Raimondo, wasn't it?{/i}"

pause 2.0

#[beat]

RFB "Want another one?"

show busstopcg at goodsize with Dissolve(5.0)

N "I think I declined the beer. I had more than enough already."

N "Raimondo must have just shrugged and brought the bottle to his lips instead."

N "For such a scrawny guy, he had no issue holding his alcohol."

N "We were probably by the old school's bus stop. I remember the pavement, littered with our crap."

N "I can't remember why we were there specifically."

N "Not that there's anywhere to be in this town anyway."

N "Looking back now, after having gone through so many exciting dates with Anna, my time
spent with Raimondo was mostly uneventful."

N "He'd just say something like “Wanna hang out after dinner?”. “Wanna come by my house?” 
There was never a question about what we'd do specifically, no real plan."

N "There was an unspoken assumption that any time we'd get to spend together would be a good time."

N "That night, we had apparently decided to get wasted."

N "I think it was just the year before I left for university, wasn't it? We could buy all the alcohol we wanted without anyone wondering whether it was legal or not."

N "It must have been a relatively new thrill for us."

#[beat]

N "What was it that led up to it?"

N "We must have been talking a lot. It was literally just us and the bottles."

N "I think we met up by the game shop that day. Some game had just been released."

N "I'm pretty sure we didn't buy it. Too expensive."

N "But a pack of beer was pretty cheap if you bought it at the supermarket instead of the bar."

N "Which is how we ended up with our asses on the pavement."

RFB "Frankly, I'm just glad to be done with it."

N "Oh, right. It was really the last year of high school."

N "We were both slowly coming to the realization of what that meant for us moving forward."

N "I was struggling to settle on one university course, while he had made his decision long ago."

R "{i}My dad knows a guy. He says he could use some extra hands.{/i}"

N "Right."

N "Part of me wanted to argue with him about that. I knew it in my heart he could have aimed for so much more."

N "But I could see the hurt in his eyes, the first time I raised the topic."

N "So I just hummed, noncommittally."

FFB "Mmm."

FFB "I don't think I'll be missing school either."

FFB "I'll be missing our classmates though."

RFB "Why? You can still be friends with them."

RFB "I, for one, don't intend to stop hanging out with any of the few people I actually care about."

RFB "That includes you, by the way, mister Freshman-to-be."

N "I laughed. I remember his words giving me some level of reassurance."

N "Even if they didn't convince me completely."

N "I had gone through changing school twice already. The only time I managed to keep any of the friends I had made 
was with the one person who followed me to the new one."

N "Well, Raimondo was going to be special, of course. Our bond had started all the way back."

RFB "But to be honest, now that my parents are finally letting me drive on my own, I'm beginning to realize 
how little I have in common with most of the boys here."

N "The alcohol in me answered for me."

FFB "You mean they're straight!"

RFB "Damn right!"

N "He licked his bottle by the finish, in an obscene suggestive way."

RFB "Listen, if a guy can't withstand me sharing my love for cocks, then he's going to find me reaaaaal boring."

RFB "Loving cock is my best quality!"

FFB "Oh?"

N "There had been a conspiratorial tone in my voice."

FFB "Is that why I'm your best friend?"

RFB "Of course! No offense, dear, but loving cock is your best quality too."

N "He winked at me."

RFB "Although, I think in your case it's more a theoretical kind of love."

RFB "Or have you finally tried without telling me?"

N "I can't even begin to guess what kind of expression I had made."

N "I'm sure I was embarrassed. Had I, maybe, sounded a little sad as well?"

N "Was that why he reached out to me, and patted me on the shoulder?"

RFB "When you're ready, Fede. You don't need to prove anything."

RFB "And there's no rush."

RFB "Your real best quality, actually, is that you're so hot that all you'll need to do is ask a guy."

scene black with Dissolve(5.0)

N "It was the alcohol talking, that's for sure."

N "Raimondo had never had any qualms about making lewd comments, but that had been the first time he said something that carried such heavy implications."

N "It must have been something about the way he'd said it as well."

N "Whatever it was, it had given me the courage to pull him into a kiss."

N "Yeah. I'm pretty sure I had been the one to take the lead."

N "But as soon as our lips had met, he had leaned into it with such eagerness, almost hunger."

N "My hand had trailed down his back, and he had arched forward as if to invite me to explore further."

N "And I did. One way or another, my hand must have landed on his crotch, because he whispered to me."

RFB "Not in the middle of the road. Follow me."

scene blowjobcg at goodsize with Dissolve(5.0)

N "Yes, Anna. It was Raimondo."

N "I dropped on my knees, while he stood against the back wall of the closed bar, his hand gripping a pile of chairs stacked on top of each other."

N "The alcohol had helped me get to that point, but it was not our ally during the act."

N "I remember despite all my licking I had some trouble to get him hard."

N "I felt like it was my fault at the time, but he had just encouraged me to keep going."

N "Once I finally managed to make him cum, I was so happy I could throw up."

N "He was such a sight. Making that familiar cocky grin melt into a gasp of pure abandonment was euphoric."

scene black with Dissolve(5.0)

N "Eventually it was over, though."

N "As his expression changed, he went back to being the Raimondo I've always known."

N "But I wasn't the same old me. I was still on my knees, and my mouth was full of a pungent taste I had never swallowed before."

N "That taste lingered for a long time after the ecstasy was over."

N "I think it was that taste that brought the reality of what happened home."

N "He must not have noticed my inner turmoil, for he had offered to return the favor."

N "That part is the most painful to remember."

N "First, I bought myself some time."

N "Told him I needed a minute."

N "That I needed to sit down a moment."

N "That I needed some water."

N "That it was the alcohol."

N "Finally, I must have admitted I just wasn't in the mood. I just wanted to go back home."

N "And that had been the end of that night."

pause 2.0

N "Hmph."

N "I remember being so anxious about talking to Raimondo the next day, I was tempted to hide from him."

N "But I didn't. That would have made it more awkward, more conspicuous, once I would inevitably bump into him alone."

N "So I stopped by his desk and he just said “hi” like nothing was weird between us."

N "I was sure he would bring it up later, after class."

N "But we walked together to the bus stop again, the very same one from the previous night. And we just talked about that game we had been wanting to buy instead."

N "Eventually it would come up, I was sure. But it never did."

N "We never mentioned it again."

pause 2.0

"I guess what happened earlier is the closest I've come to acknowledging I sucked Raimondo's dick since it happened."

"And now it's the reason Anna doesn't want to introduce me to her parents… as their future son-in-law? Is that how she phrased it?"

"Has she been thinking about it then? Is that why she's never introduced me to them?"

"No… That doesn't make sense. She can't have known until tonight."

"Heh, Lady Giuditta. I guess I was just trying to borrow a bit of your good luck. Isn't that exactly what happened to you?"

"Your future husband had no qualms about that."

show goodboy at center:
    matrixcolor BrightnessMatrix(-0.2)
    zoom 0.65 yoffset 150
with dissolve

"I look back to the wolves."

"This one kinda looks like Raimondo."

"A little bit. He has his spunk."

"I like it."

"I stretch my hand and pet it as if it was a real dog."

pause 2.0

"Raimondo didn't deserve it, did he?"

"I can't really blame what happened earlier on him if I've never made clear how things stand between us."

"In my heart, I deceived myself into thinking we had both agreed that being best friends was enough for us."

"“Best friend”. Wasn't that how I introduced him to Anna earlier?"

"Wasn't that how I've been introducing him to everyone ever since?"

"I think back to Lady Giuditta again. Isn't her story that she got to be introduced as she wished?"

scene black with dissolve
pause 0.1
show hallway at center with dissolve:
    matrixcolor BrightnessMatrix(-0.2)
    zoom 0.5

"I finally look back to where I came from."

"This whole thing has been so stupid."

"We've all been so stupid. Pinning our hopes on wishes and good luck."

"I brought everyone here to be honest. Time to be honest with him too."

scene black with Dissolve(5.0)
pause 0.1

############################################### ANNA POV ###############################################

$ pov = "anna"

play music polyhedron fadein 5.0

show modernart at truecenter with Dissolve(5.0):
    zoom 0.6
    matrixcolor BrightnessMatrix(-0.2)

"Love is patient, love is kind."

"It does not envy, it does not… keep track…"

"Record?"

"The rest of the verse escapes you."

"You used to know this. You used to think about how a priest would say this at your wedding."

"Not to Federico, necessarily. This was before Federico."

"The paintings and sculptures in this room feel patient and, perhaps, even kind."

show poly at orb_anim with dissolve

"The faces of this polyhedron demand nothing from you."

"“All is dust in the wind,” and all that."

"You briefly wonder if this is sacrilegious, but it's a far cry from idol worship."

"People are allowed to appreciate art in a museum."

P "How are you feeling?"

"Sad. Crushed. Like I want to escape."

P "Escape to where?"

"Here is fine."

P "I see. That's all right. I will be here."

"…"

P "…"

"…"

"So Giuditta was in love with someone else."

P "That is typically what these fur lockets mean."

"From before, though. And she married Ferdinand anyways."

"That whole story about them being in love, getting married, living out their lives in this villa."

"Maybe she looks so sad in these paintings because…"

"It's so sad."

"The crying starts again."

"I hiccup."

"Am I allowed to stay here?"

P "Stay here as long as you need."

P "Let it out, let it out."

P "It's okay. No one can see you here."

stop music fadeout 5.0

scene black with Dissolve(5.0)
pause 0.1

$ pov = "fede"

############################################### FEDE POV ###############################################

show anteroom at truecenter with dissolve:
    zoom 0.5
with Dissolve(5.0)

"He's still sitting where I left him, in the room with the portrait of the Lady."

MCR sad "Hey."

MCF concerned "Hey."

"He doesn't get up. He doesn't look at me"

MCR "Listen, I'm so—"

MCF "No, please!"

MCF neutral "Let me go first."

MCF "You've apologized quite enough for one night."

"Now that I've taken away his initiative, he finally looks."

MCF "You've got nothing to apologize for."

MCF "You know, I've done some thinking, and I've realized I keep telling everyone you're my best friend."

MCF concerned "But I've never bothered to check if that's what you want to be."

MCF "I've never told you how I feel. And for that, it's me who should apologize."

MCF "I—Do you mind if I sit next to you?"

MCF neutral "Feels a little weird to talk down on you like this."

"Raimondo looks at the spot next to him, as if considering his choice carefully. Then he shrugs."

MCR sad "Course."

#"I sit next to him, while trying to maintain a respectful distance between us."

MCF concerned "I won't pretend I've understood how love works."

"Well, that's one way to start this conversation."

MCF sad "There's still so much stuff I'm still trying to figure out."

MCF "I feel pretty confident about a few things though."

MCF "I like women, and I like men too. Even if I don't have the best track record to prove that second part."

MCF neutral "And I love you. I really do."

"I don't look away, I don't slouch. I want to make sure he understands I have no reservations about what I'm saying."

MCF "But there’s also something else I think I learned."

MCF "Back when we were kids, I used to think love, the romantic kind, the kind of love of stories and fables? It was just like other kinds of love, just more intense."

MCF "But now, I think the Greeks were right, you know?"

"I can tell by his expression he does, in fact, not know."

MCF "Different kinds of love are just different kinds of love. They're not on a scale."

MCF "I used to wonder if the reason I don't want to ask you out is that I don't love you enough."

MCF "But that's not it at all! It's just that I love you too much as a friend, and I feel like being anything else would spoil that."

MCF "I was really happy to get to hang out with you again, you know?"

#beat

MCF sad "When we did… that kind of stuff…"

"I stroke some invisible cylinder close to my mouth, before I remind myself I came here with the intention to speak clearly."

MCF concerned "When we had… sex…"

MCF "Even though I wanted it, part of me was so terrified I would be… bad at it."

MCF neutral "I guess now that I've had more experience, that feels like the kind of silliness we all go through when sex is new to us."

MCF concerned "But it wasn't just that. I believe what I really scared me was that sex could become the scale by which we would measure our friendship."

"He's let me talk for a while now."

"There's still stuff I want to say. I don't feel like I've managed to explain everything about how I feel."

"Thankfully I don't need to. I find myself into Raimondo's hug."

"It's a very different hug from earlier. No less tight, no less intense."

"Just different."

MCR neutral "Thank you for telling me."

"We stay like this for a while."

"When our hug ends, the villa is still there. It's patiently been waiting."

"I get up."

MCF concerned "I think I'd like to go out now."

MCR sad "Are you sure? The Lady might still grant your wish."

MCF neutral "I think that boat's sailed."

MCR "Has it?"

MCF sad "I told you what happened."

MCR "Yeah. But I've talked to her myself."

MCR neutral "I don't think I really gave her a fair chance tonight… But we've hung out."

MCR "She might just need some time. Like we all do."

MCR "Relationships are an endless cycle of opportunities to hurt each other."

MCR "I'm not telling you you have to forgive her, if that's not what you want."

MCR "I'm just telling you she might come to regret her first reaction. She might want to be forgiven."

MCR happy "Trust me. We do all the time."

scene black with Dissolve(5.0)
pause 0.1

############################################### ANNA POV ###############################################

$ pov = "anna"

show pianocg at goodsize with Dissolve(5.0)

"You didn't fall in love with Fede the moment you met. Or even on your first date."

"He slouched, and had a bad habit of staring at his feet."

play music federicopiano

"A couple days later you were looking for a friend in the practice rooms at school and heard Fede singing, by pure chance."

"He was belting out “Haven’t Met You Yet” without a care in the world and banging out chords on an out-of-tune piano."

"But it was beautiful. He sounded happy."

"Maybe that wasn't love then, either, but interest. The beginnings of love."

"Had he been… like that, even back then?"

"Is the Fede at the piano somewhere here in the villa right now, waiting for you?"

stop music fadeout 5.0

scene black with Dissolve(5.0)

"You make your way back to the anteroom which leaks light into the adjacent exhibit. A sign of life."

#"Bg lit room"

#"Show raimondo neutral"

show anteroom at truecenter with dissolve:
    zoom 0.5
with dissolve

"Raimondo is alone on the divan, and looks up at you when you enter."

"It would've been romantic in this room with just the two of them. Soft shadows on soft fur."

"But Federico is not here. Raimondo is alone."

MCA side sad2 "Ah… Hello again."

show rai sad at center with dissolve:
    matrixcolor BrightnessMatrix(-0.2)

R "Hey."

MCA "I thought he'd be with you."

R "He left. He asked me to unlock the front door for him, and I did."

R "Sun isn't up yet. Guess he doesn't need the Lady's blessing."

R "Makes you wonder what it was all for."

MCA happy "I got to meet you."

show rai neutral

"He smiles weakly."

R "Sure."

MCA "I have a feeling we'll be seeing each other again."

R "Maybe."

R "I don't think he went far. He wouldn't drive off without you."

R "You should go."

MCA "Goodbye then. And thank you."

R "See ya."

#"Scene bg foyer"

scene black with dissolve
pause 0.1
show entryway at goodsize with dissolve

play sound chord1

"The grand entryway."

"Are you ready?"

#"Scene bg window (Outside is brighter than inside.)"

scene black with dissolve
pause 0.1
show garden at truecenter:
    zoom 0.3
show fed:
    zoom 0.15
    xpos(750) ypos(-150)
    matrixcolor BrightnessMatrix(-1.0)
with dissolve

play sound chord2

"It's a beautiful garden. Same as it was when you arrived."

"Federico stands a short distance from the steps, looking out over the rows of flowers."

"Time to go to him."

scene black with dissolve

"Your hand is on the doorknob. It turns."

play sound chord3

"A twinge."

"You're breaking the rule."

"If you stay inside, stay where you are, maybe lady Giuditta will still grant your wish."

play sound chord4

"But that's foolishness."

play audio doorcreak
play ambient crickets fadein 3.0

pause 2.0

#"Play sound door_open"

#"Play ambient outdoor_night"

#"Play music “uncertain futures”"

#"Scene bg garden"

show night at goodsize
show dawn at goodsize:
    alpha(0.0)
with dissolve

#play music uncertainfutures

play music "<from 79.5 loop 0.0>audio/music/uncertainfutures.ogg"

"The night air is cool and fresh, and the garden opens before you."

"You walk down the steps. Stop."

"Breathe."

"Flowers and vines and outside."

"Walk."

#"Show fede pensive [gaze elsewhere]"

show fed turned at center with dissolve:
    matrixcolor BrightnessMatrix(-0.1)

"He must hear your footsteps on the grass as you approach. But he doesn't stir."

MCA sad2 "Fede?"

F "Anna."

"He says without turning towards you."

MCA sad2 "I love you."

"It hurts to get out. Your face burns."

"It may not be enough, but it is true."

#"Show fede direct [looking at her, same serious expression]"

show fed concerned
pause 1.0
show fed neutral

F "Love you too."

"It's overwhelming."

hide fed with dissolve

play sound hug

"You hug each other. It's the first time in a while you've hugged each other like this. Like each of you
was trying to drown themself in the other."

"Federico is thick and sturdy like he's always been. You know the shape of his body. You know this shirt
because you were the one who bought it for him."

"Does that make it his shirt? Or yours?"

"You'd never thought about it that way until now."

"Federico hums, and his shoulder buzzes against your face."

MCF neutral "Hey."

MCF "The sun's coming up."

"He relaxes his grip, and you want to hold on, but he has decided the moment is over."

"The sky behind Federico is still dark. He motions his head to something over your shoulder."

"You turn to see what he sees."

show dawn:
    linear 25.0 alpha(1.0)

pause (20.0)

stop music fadeout 5.0
stop ambient fadeout 5.0

#"[Fade to black, credits]"

return