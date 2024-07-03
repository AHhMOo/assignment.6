import random

moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Stressed", "Relaxed"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in range(7):  
    random_mood = random.choice(moods)  
    print(f"On {days[day]}, you were feeling {random_mood}.")


