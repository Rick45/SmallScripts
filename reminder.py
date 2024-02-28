import time
import pymsgbox


# Set the interval in minutes for the pop-up message
interval_minutes = 1  # Replace X with the desired interval

# Main loop
while True:
    try:
        pymsgbox.alert(
            "Vai beber agua",
            "Lembrete",
            #timeout=10,  # Display the notification for 10 seconds
        )
        # Sleep for the specified interval in seconds
        time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        # Allow the user to exit the loop with Ctrl+C
        break
