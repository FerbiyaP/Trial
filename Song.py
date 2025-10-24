import time
import sys

# Write your song lyrics here
lyrics = """

I wanna come home to roses
And dirty little notes on Post-its
And when my hair starts turning grey
He'll say I'm like a fine wine, better with age
I guess I learned it from my parents
That true love starts with friendship
A kiss on the forehead, a date night
Fake an apology after a fight

I need a man who's patient and kind
Gets out of the car and holds the door
I wanna slow dance in the living room like
We're eighteen at senior prom and grow
Old with someone who makes me feel young
I need a man who loves me like
My father loves my mom

I want a road trip in the summers
I wanna make fun of each other
I wanna rock out to Billy Joel
And flip our kids off when they call us old
He'll accidentally burn our dinner
And let me be the Scrabble winner
And when my body changes shapes
He'll say, "Oh my God, you look hot today"

I need a man who's patient and kind
Gets out of the car and holds the door
I wanna slow dance in the living room like
We're eighteen at senior prom and grow
Old with someone who makes me feel young
I need a man who loves me like
My father loves my mom

And if he lives up to my father
Maybe he can teach our daughter
What it takes to love a queen
She should know she's royalty

I need a man who's patient and kind
Gets out of the car and holds the door
I wanna slow dance in the living room like
We're eighteen at senior prom and grow
Old with someone who makes me feel young
I need a man who loves me like
My father loves my mom
I need a man who loves me like
My father loves my mom




"""

# Split the lyrics into individual words
words = lyrics.split()

# Loop through each word and display it one by one
for word in words:
    sys.stdout.write(word + " ")  # print word without newline
    sys.stdout.flush()  # force immediate display
    time.sleep(0.4)  # delay between words (in seconds)

print("\n\n🎵 End of song 🎵")
