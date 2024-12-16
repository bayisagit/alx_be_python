# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = ""

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case 'high':
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it soon."
    case 'medium':
        reminder = f"Note: '{task}' is a medium priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". You can complete it when time permits."
    case 'low':
        reminder = f"Note: '{task}' is a low priority task"
        if time_bound == 'yes':
            reminder += " but still requires immediate attention today!"
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered."

# Provide a Customized Reminder
print(reminder)