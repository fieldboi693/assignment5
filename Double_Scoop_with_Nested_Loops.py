# Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at 
# three different
# times of the day (morning, afternoon, evening) for each day of the week. 
# Use nested loops to implement this: 
# the outer loop should iterate over the days, and the inner loop should iterate over 
# the times of the day. 
# For each time, randomly select a mood from a predefined list and print it. 
# Use the random module again to randomly select the mood.



import random

def mood_tracker():
    mood_list = ["happy", "sad", "neutral", "excited", "tired", "calm"]  # List of possible moods
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for day in days:  # Outer loop iterates through days of the week
        print(f"\n--- {day} ---")
        for time in ["Morning", "Afternoon", "Evening"]:  # Inner loop iterates through times of day
            mood = random.choice(mood_list)  # Randomly select a mood
            print(f"{time}: {mood}")

mood_tracker() 