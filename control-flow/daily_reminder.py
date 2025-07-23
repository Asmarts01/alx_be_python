# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Build the additional part of the reminder based on priority
match priority:
    case "high":
        reminder = ""  # No extra message, just show main line
    case "medium":
        reminder = "It should be handled soon."
    case "low":
        reminder = "Consider completing it when you have a free time."
    case _:
        reminder = "The priority level is unknown."

# Add time-sensitive message
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Final output with your preferred print format
print(f"Reminder: '{task}' is a {priority} priority task. {reminder}")
