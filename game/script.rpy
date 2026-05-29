# The script of the game goes in this file.

################################################################################

### TRANSFORMS ###

transform goodsize:
    xysize (1920, 1080)

################################################################################

### FEDERICO ###

define F = Character(_("Federico"), color ="#fff", what_prefix='"', what_suffix='"')
define MCF = Character(_("Federico"), color ="#fff", what_prefix='"', what_suffix='"', image="fed")

layeredimage fed:
    zoom 0.3
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
    group body:
        attribute base default:
            "images/Federico/Base.png"
        attribute meee:
            "images/Federico/Meee.png"

image side fed = LayeredImageProxy("fed")

### ANNA ###

define A = Character(_("Anna"), color ="#fff", what_prefix='"', what_suffix='"')
define MCA = Character(_("Anna"), color ="#fff", what_prefix='"', what_suffix='"', image="ann")

layeredimage ann:
    zoom 0.3 xzoom -1.0
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
    group body:
        attribute base default:
            "images/Anna/Base.png"
        attribute open:
            "images/Anna/Open.png"

image side ann = LayeredImageProxy("ann")

### RAIMONDO ###

define R = Character(_("Raimondo"), color ="#fff", what_prefix='"', what_suffix='"')
define MCR = Character(_("Anna"), color ="#fff", what_prefix='"', what_suffix='"', image="rai")

layeredimage rai:
    zoom 0.3
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
    group body:
        attribute base default:
            "images/Raimondo/Base.png"
        attribute meee:
            "images/Raimondo/Meee.png"

image side rai = LayeredImageProxy("rai")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show rai happy at center
    show ann happy at left

    # These display lines of dialogue.

    MCA "You've created a new Ren'Py game."

    show rai neutral at center

    A "Once you add a story, pictures, and music, you can release it to the world!"

    show rai mad meee at center

    "."

    # This ends the game.

    return
