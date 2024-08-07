import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # Overwrite the previous line
        time.sleep(1)
        t -= 1

# Input time in seconds
t = input("Enter the time in seconds: ")
countdown(int(t))
print("Fire in the hole!!")  # Signify the end of the countdown
