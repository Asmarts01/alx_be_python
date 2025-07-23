Task = input ("Enter your task: ")
# This program sets a daily reminder based on user input.
priority = input("Enter the priority (high/medium/low): ").strip().lower()
time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()
match priority:
    case "high":
        print(f"Reminder set for high priority task: {Task}")
        if time_bound == "yes":
            print("This task needs immediate attention.")
        else:
            print("You can complete this task at your convenience.")
    case "medium":
        print(f"Reminder set for medium priority task: {Task}")
        if time_bound == "yes":
            print("This task should be completed soon.")
        else:
            print("You can complete this task when you have time.")
    case "low":
        print(f"Reminder set for low priority task: {Task}")
        if time_bound == "yes":
            print("This task can wait, but try to finish it eventually.")
        else:
            print("You can complete this task whenever you find time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
# This program sets a daily reminder based on user input.