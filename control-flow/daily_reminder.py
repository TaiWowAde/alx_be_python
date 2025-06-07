# File: daily_reminder.py

def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match Case for priority
    match priority:
        case "high":
            priority_message = f"'{task}' is a high priority task"
        case "medium":
            priority_message = f"'{task}' is a medium priority task"
        case "low":
            priority_message = f"'{task}' is a low priority task"
        case _:
            priority_message = f"'{task}' has an unknown priority level"

    # Add time-bound message
    if time_bound == "yes":
        priority_message += " that requires immediate attention today!"
    else:
        priority_message += ". Consider completing it when you have free time."

    # Final reminder output (must start with 'Reminder:')
    print(f"\nReminder: {priority_message}")

if __name__ == "__main__":
    main()
