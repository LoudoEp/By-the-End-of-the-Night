# The script of the game goes in this file.

################################################################################

### TRANSFORMS ###

transform goodsize:
    xysize (1920, 1080)

################################################################################

### VARIABLES ###

default pov = "anna"

################################################################################

### FEDERICO ###

define F = Character(_("Federico"), color ="#fff", what_prefix='"', what_suffix='"')
define MCF = Character(_("Federico"), color ="#fff", what_prefix='"', what_suffix='"', image="fed")

layeredimage fed:
    zoom 0.45 yoffset 550
    group body:
        attribute base default:
            "images/Federico/Base.png"
        attribute meee:
            "images/Federico/Meee.png"
    group expressions:
        attribute neutral default:
            "images/Federico/Neutral.png"
        attribute annoyed:
            "images/Federico/Annoyed.png"
        attribute concerned:
            "images/Federico/Concerned.png"
        attribute gag:
            "images/Federico/Gag.png"
        attribute happy:
            "images/Federico/Happy.png"
        attribute mad:
            "images/Federico/Mad.png"

image side fed = LayeredImageProxy("fed")

### ANNA ###

define A = Character(_("Anna"), color ="#fff", what_prefix='"', what_suffix='"')
define MCA = Character(_("Anna"), color ="#fff", what_prefix='"', what_suffix='"', image="ann")

layeredimage ann:
    xzoom -1.0 zoom 0.45 yoffset 550
    group body:
        attribute base default:
            "images/Anna/Base.png"
        attribute open:
            "images/Anna/Open.png"
        attribute side:
            "images/Anna/Side.png"
    group expressions:
        attribute neutral default:
            "images/Anna/Neutral.png"
        attribute angry:
            "images/Anna/Angry.png"
        attribute concerned:
            "images/Anna/Concerned.png"
        attribute happy:
            "images/Anna/Happy.png"
        attribute mad:
            "images/Anna/Mad.png"
        attribute vulnerable:
            "images/Anna/Vulnerable.png"

image side ann = LayeredImageProxy("ann")

### RAIMONDO ###

define R = Character(_("Raimondo"), color ="#fff", what_prefix='"', what_suffix='"')
define MCR = Character(_("Raimondo"), color ="#fff", what_prefix='"', what_suffix='"', image="pastrai")

layeredimage rai:
    zoom 0.45 yoffset 550
    group body:
        attribute base default:
            "images/Raimondo/Base.png"
        attribute meee:
            "images/Raimondo/Meee.png"
    group expressions:
        attribute neutral default:
            "images/Raimondo/Neutral.png"
        attribute annoyed:
            "images/Raimondo/Annoyed.png"
        attribute concerned:
            "images/Raimondo/Concerned.png"
        attribute gag:
            "images/Raimondo/Gag.png"
        attribute happy:
            "images/Raimondo/Happy.png"
        attribute mad:
            "images/Raimondo/Mad.png"

image side pastrai:
    zoom 0.45 yoffset 550
    "images/Raimondo/Past1.png"

################################################################################

### BACKGROUNDS ###

image black = "#000"
image car = "images/pexels-Alessandro-Aviles.avif"
image approaching = "images/approaching-Kerche.jpg"
image villafar = "images/villafar-Kerche.jpg"
image parking = "images/unsplash-parking-sebastian-huxley.jpg"
image outside = "images/outside-Kerche.jpg"
image bglight:
    zoom 2.0
    "images/bglight.png"
image chlight:
    zoom 2.0
    "images/chlight.png"

################################################################################

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene test at goodsize

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "You've created a new Ren'Py game."

    show rai neutral at center

    MCR "Once you add a story, pictures, and music, you can release it to the world!"

    show rai mad meee at center

    $ pov = "fede"

    "."

    # This ends the game.

    return
