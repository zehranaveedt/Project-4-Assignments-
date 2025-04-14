import time

def countdown_timer():
    print("=== Countdown Timer ===")
    
    # User input
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    
    total_seconds = minutes * 60 + seconds
    
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_format = f"{mins:02d}:{secs:02d}"
        print(f"\rTime Remaining: {timer_format}", end="")
        time.sleep(1)
        total_seconds -= 1

    print("\n\n⏰ Time's up! Timer completed.")

# Call the function
countdown_timer()
