import random

print("=== Workout AI 💪 ===")

# Ask user for input
mood = input("How do you feel today? (tired / normal / energetic): ").lower()
goal = input("What is your goal? (strength / endurance / mobility): ").lower()
time = int(input("How many minutes do you have? (10 / 20 / 45): "))

# Some basic workout options
workouts = {
    "strength": [
        "Push-ups 3x12",
        "Squats 3x15",
        "Plank 3x30s",
        "Lunges 3x10 each leg",
        "Dips 3x10"
    ],
    "endurance": [
        "Jumping jacks 2 min",
        "Burpees 3x10",
        "Mountain climbers 3x20s",
        "High knees 3x30s",
        "Skipping rope 3 min"
    ],
    "mobility": [
        "Cat-cow stretch 5 reps",
        "Child’s pose 30s",
        "Hip circles 5 each side",
        "Arm swings 10 reps",
        "Neck rolls 5 each side"
    ]
}

# Pick routine length based on time
if time <= 10:
    num_exercises = 3
elif time <= 20:
    num_exercises = 4
else:
    num_exercises = 5

# Adjust intensity based on mood
if mood == "tired":
    chosen_goal = "mobility"
elif mood == "energetic":
    chosen_goal = goal  # stick to what they want
else:
    chosen_goal = goal  # balanced
    # could add modifications later

# Randomly choose exercises
plan = random.sample(workouts[chosen_goal], num_exercises)

# Print workout plan
print("\n🔥 Your Workout Plan 🔥")
for i, exercise in enumerate(plan, 1):
    print(f"{i}. {exercise}")

print("\nGood luck! Stay consistent 💯")
