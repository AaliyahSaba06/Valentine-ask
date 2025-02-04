import time
import random

def print_slow(str):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

def love_message():
    print_slow("Hey, my favorite coder... 💻💖")
    time.sleep(1)
    print_slow("I wrote a little script just for you... 👀")
    time.sleep(1)
    print_slow("You know, just to ask you something important... 💌")
    time.sleep(1)
    
    responses = [
        "Will you be my Valentine? 💖",
        "I was wondering... would you be my Valentine? 😘",
        "You make my heart skip a beat... will you be my Valentine? 💘",
        "There’s no one else I'd rather spend this day with... will you be my Valentine? 💐"
    ]
    
    # Randomly pick a message to keep it surprising
    print_slow(random.choice(responses))
    time.sleep(1)
    
    print_slow("Just say 'Yes', and you’ll make me the happiest person! 😍")

# Call the function to ask the big question
love_message()
