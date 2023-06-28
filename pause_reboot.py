import time
import webbrowser
import pyttsx3
import random
from plyer import notification

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print("Break remaining:", timer, end='\r')
        time.sleep(1)
        t -= 1


# Customizable break duration
break_duration = input("Enter the duration of your break (in minutes): ")
break_seconds = int(break_duration) * 60

# Countdown timer for the break
countdown(break_seconds)

# Display message and play video
print("\nBreak time! Enjoy your break.")

# Reminder notification
notification.notify(
    title="Take a Break",
    message="It's time for your break. Enjoy some relaxation!",
    timeout=3
)

# Randomize relaxing video selection
relaxing_videos = [
    "https://www.youtube.com/watch?v=Sg8XVnCneXE",
    "https://www.youtube.com/watch?v=abc123"  # Add more video URLs as per your choice
]
random_video = random.choice(relaxing_videos)

# Speak the message using pyttsx3
engine = pyttsx3.init()
engine.say("Break time! Enjoy your break.")
engine.runAndWait()

# Open a relaxing video in a new browser tab
webbrowser.open(random_video, new=2)



