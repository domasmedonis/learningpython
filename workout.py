import random
import json
import os

print("=== Workout AI v3 🤖💪 ===")

# Save file for workout history
SAVE_FILE = "workout_history.json"

# Load past data
if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, "r") as f:
        history = json.load(f)
else:
    history = {"sessions": 0, "last_goal": None}

# Ask user
mood = input("How do you feel today? (tired / normal / energetic): ").lower()
goal = input("What is your goal? (strength / endurance / mobility): ").lower()
time = int(input("How many minutes do you have? (10 / 20 / 45): "))

# Exercise pool
workouts = {
    "strength": [
        "Push-ups {reps} reps",
        "Squats {reps} reps",
        "Lunges {reps} reps each leg",
        "Dips {reps} reps",
        "Plank {time}s"
    ],
    "endurance": [
        "Burpees {reps} reps",
        "Mountain climbers {time}s",
        "High knees {time}s",
        "Jumping jacks {time}s",
        "Skipping rope {time}s"
    ],
    "mobility": [
        "Cat-cow stretch {reps} reps",
        "Child’s pose {time}s",
        "Hip circles {reps} reps each side",
        "Arm swings {reps} reps",
        "Neck rolls {reps} reps each side"
    ]
}

# AI Adjustment:
sessions = history["sessions"]

# Increase difficulty every 3 sessions
base_reps = 10 + (sessions // 3) * 2
base_time = 20 + (sessions // 3) * 5

# Tired = easier, energetic = harder
if mood == "tired":
    base_reps = max(5, base_reps - 5)
    base_time = max(10, base_time - 10)
elif mood == "energetic":
    base_reps += 5
    base_time += 10

# Pick exercises (avoid repeating last goal if possible)
if history["last_goal"] == goal:
    chosen_goal = random.choice([g for g in workouts.keys() if g != goal])
else:
    chosen_goal = goal

num_exercises = 3 if time <= 10 else 4 if time <= 20 else 5
plan = random.sample(workouts[chosen_goal], num_exercises)

# Generate workout plan with reps/time filled in
print("\n🔥 Your Adaptive Workout Plan 🔥")
for i, exercise in enumerate(plan, 1):
    print(f"{i}. " + exercise.format(reps=base_reps, time=base_time))

print(f"\n(Session {sessions + 1}) — getting stronger each time 💯")

# Save updated history
history["sessions"] += 1
history["last_goal"] = chosen_goal
with open(SAVE_FILE, "w") as f:
    json.dump(history, f)
