# daily_reminder.py

# Function to prompt for task details and validate input
def get_task_details():
    task = input("Enter your task: ")
    while not task.strip():  # Check if task is empty
        task = input("Task cannot be empty. Please enter your task: ")
    
    priority = input("Priority (high/medium/low): ").lower()
    while priority not in ['high', 'medium', 'low']:  # Validate priority
        priority = input("Invalid priority. Please enter 'high', 'medium', or 'low': ").lower()
    
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    while time_bound not in ['yes', 'no']:  # Validate time-bound input
        time_bound = input("Please answer with 'yes' or 'no': ").lower()
    
    return task, priority, time_bound

# Get task details from user
task, priority, time_bound = get_task_details()

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
        reminder = f"Reminder: '{task}' is a medium priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". You can complete it when time permits."
    case 'low':
        reminder = f"Reminder: '{task}' is a low priority task"
        if time_bound == 'yes':
            reminder += " but still requires immediate attention today!"
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered."

# Provide a Customized Reminder
print(reminder)