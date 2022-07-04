# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("A")
define b = Character("B")
define nurse = Character("Nurse")

#define narrator = nvl_narrator # Turns on Novel Mode


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

    # These display lines of dialogue.

    "It's been too long."

    "I don't entirely know how long, I wasn't designed to keep track. A few weeks, at any rate."

    "But it's been too long."

    "My name is A."

    "It's not something I was launched with, but it's what my employer took to calling me."

    "I am an android commissioned to work for a six-year government infrastructure initiative. If you're ever by a new road, footpath, or bridge in this city that wasn't there a decade ago, you can thank me and mine."

    "That initiative ended two years ago, and by all rights I was set to be retired."

    "Nothing wrong with that, of course. We'd seen to our purpose, and after that there was no real point to keeping us running."

    "In retrospect, though, I'm nothing if not thankful that B still saw some use to me."

    nurse "Excuse me.{w}You must be B's caretaker, is that right?"

    a "At your service."

    b "I could tell you that."

    nurse "Of course! Of course, I'm sorry."

    nurse "We'll be discharging her today.{w} I'll have to ask you to ensure she avoids any strenuous physical activity for the next six weeks.{w} Ensure she gets plenty of sleep, too.{w} In fact, you'll find a guide to recovering from a craniotomy on-"

    a "Of course. I downloaded it while waiting."

    nurse "Oh, good! The most important thing to remember is that if Mrs. B becomes unwell during the recovery period, you don't hesitate to call for an ambulance. Does that all make sense?"

    a "Certainly."

    nurse "Alright, then.{w} I wish the two of you a very pleasant afternoon."

    b "Hmph."

    a "Thank you. We'll be off, then."

    pause 1.5

    scene bg waiting room 1
    with Dissolve(1.0)

    b "They talk as if I can't take care of myself."

    a "I hate to be the bearer of bad news, but you legally can't."

    a "At any rate, that was a very serious operation you'd just been through. I don't think anybody would expect you to even have the energy."

    b "Shows how much they don't know, then!"

    "Well, with an attitude like that{cps=5}... {/cps}what can I say? It's as if she's back to her old self already."

    a "Come on, ma'am."

    a "Let's go home."

    # This ends the game.
    return
