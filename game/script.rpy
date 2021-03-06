# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define a = Character("A")
#define b = Character("B")
#define nurse = Character("Nurse")

define narrator = nvl_narrator # Turns on Novel Mode

define a = Character("A", kind=nvl)
define b = Character("B", kind=nvl)
define nurse = Character("Nurse", kind=nvl)


# {w} waits for the user to click before showing more text
# {p} Same as above but displays on a new line as well.
# {w=1.0} to wait for 1 second.
# {p=1.0} to wait for 1 second and then newline.




# The game starts here.

label start:

    play music voiceless fadeout 1.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg waiting room 1
    with Dissolve(1.0)

    pause 2.0

    scene bg waiting room 2
    with Dissolve(1.0)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "It's been too long."
    "I don't entirely know how long, I wasn't designed to keep track. A few weeks, at any rate."
    "But it's been too long."

    nvl clear #for new page of text
    window hide #hide the nvl window


    show a temp #show "name of image" without extensionS
    with Dissolve(1.0)

    pause 1.5

    window show #show the nvl window

    "My name is A."
    "It's not something I was launched with, but it's what my employer took to calling me."
    "I am an android commissioned to work for a six-year government infrastructure initiative. If you're ever by a new road, footpath, or bridge in this city that wasn't there a decade ago, you can thank me and mine."
    "That initiative ended two years ago, and by all rights I was set to be retired."
    "Nothing wrong with that, of course. We'd seen to our purpose, and after that there was no real point to keeping us running."

    nvl clear #for new page of text
    window hide #show the nvl window

    show a temp at left
    with Dissolve(0.5)

    pause 0.5

    show nurse temp
    with Dissolve(0.5)

    show b temp at right
    with Dissolve(0.5)

    window show #show the nvl window

    "In retrospect, though, I'm nothing if not thankful that B still saw some use to me."
    nurse "Excuse me. {w}You must be B's caretaker, is that right?"
    a "At your service."
    b "I could tell you that."
    nurse "Of course! Of course, I'm sorry."

    nvl clear #for new page of text

    nurse "We'll be discharging her today."
    nurse "I'll have to ask you to ensure she avoids any strenuous physical activity for the next six weeks.{w} Ensure she gets plenty of sleep, too.{w} In fact, you'll find a guide to recovering from a craniotomy on-"

    nvl clear #for new page of text
    
    a "Of course. I downloaded it while waiting."
    nurse "Oh, good! The most important thing to remember is that if Mrs. B becomes unwell during the recovery period, you don't hesitate to call for an ambulance. Does that all make sense?"
    a "Certainly."
    nurse "Alright, then.{w} I wish the two of you a very pleasant afternoon."
    b "Hmph."
    a "Thank you. We'll be off, then."

    nvl clear #for new page of text
    window hide #show the nvl window

    pause 1.5

    scene bg waiting room 1
    with Dissolve(1.0)

    show b temp at right
    with Dissolve(0.5)

    b "They talk as if I can't take care of myself."

    show a temp at left
    with Dissolve(0.5)

    window show #show the nvl window

    a "I hate to be the bearer of bad news, but you legally can't."
    a "At any rate, that was a very serious operation you'd just been through. I don't think anybody would expect you to even have the energy."
    b "Shows how much they don't know, then!"

    nvl clear #for new page of text

    "Well, with an attitude like that{cps=5}... {/cps}what can I say? It's as if she's back to her old self already."
    a "Come on, ma'am."
    a "Let's go home."

    nvl clear #for new page of text
    window hide #show the nvl window

    # This ends the game.
    return
