# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = (f"Reminder: '{task}' is a {priority} priority task")

# Use match-case to provide message based on priority
match priority:
    case "high":
        reminder += ""
    case "medium":
        reminder += " that should be handled soon"
    case "low":
        reminder += " Consider completing it when you have a free time"
    case _:
        reminder = (f"Reminder: '{task}' has an unknown priority")

# Add time-bound urgency
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the final reminder
print(reminder)
