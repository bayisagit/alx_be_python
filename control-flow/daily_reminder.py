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
        if time_bound == 'yes':
            reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"Reminder: '{task}' is a high priority task. Consider completing it soon."
    case 'medium':
        if time_bound == 'yes':
            reminder = f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
        else:
            reminder = f"Reminder: '{task}' is a medium priority task. You can complete it when time permits."
    case 'low':
        if time_bound == 'yes':
            reminder = f"Reminder: '{task}' is a low priority task but still requires immediate attention today!"
        else:
            reminder = f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered."

# Provide a Customized Reminder
print(reminder)