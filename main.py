import time

def countdown(t):

    while t:
        mins, secs = divmod(t,60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Time Expired")

t = input("Enter the countdown time: ")
countdown(int(t))