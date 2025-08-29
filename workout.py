print("=== Workout AI v2 💪 ===")

# Ask user for input
mood = input("How do you feel today? (tired / normal / energetic): ").lower()
goal = input("What is your goal? (strength / endurance / mobility): ").lower()
time = int(input("How many minutes do you have? (10 / 20 / 45): "))

# Base workout templates
templates = {
    "strength": {
        "warmup": "5 min dynamic warm-up (jumping jacks, arm swings)",
        "main": [
            "Push-ups 3x12",
            "Squats 3x15",
            "Lunges 3x10 each leg"
        ],
        "finisher": "Plank 3x30s"
    },
    "endurance": {
        "warmup": "2 min jogging in place",
        "main": [
            "Burpees 3x10",
            "Mountain climbers 3x20s",
            "High knees 3x30s"
        ],
        "finisher": "Skipping rope 2 min"
    },
    "mobility": {
        "warmup": "Neck rolls + shoulder rolls, 1 min",
        "main": [
            "Cat-cow stretch 5 reps",
            "Hip circles 5 each side",
            "Child’s pose 30s"
        ],
        "finisher": "Full body stretch 2 min"
    }
}

# Mood adjustments
if mood == "tired":
    goal = "mobility"  # override
elif mood == "energetic" and goal == "mobility":
    goal = "endurance"  # push harder

# Adjust workout length
if time <= 10:
    plan_type = "short"
elif time <= 20:
    plan_type = "medium"
else:
    plan_type = "long"

# Build plan
chosen = templates[goal]

print("\n🔥 Your Workout Plan 🔥")
print("Warm-up:", chosen["warmup"])

if plan_type == "short":
    print("Main:", chosen["main"][0])
elif plan_type == "medium":
    for exercise in chosen["main"][:2]:
        print("Main:", exercise)
else:  # long
    for exercise in chosen["main"]:
        print("Main:", exercise)

print("Finisher:", chosen["finisher"])
print("\nStay strong! 💯")
