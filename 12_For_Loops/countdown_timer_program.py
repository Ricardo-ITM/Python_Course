import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(1, my_time + 1)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) # 1 second

print("TIME'S UP!")

for x in range(3): 
    for y in range(1, 10):
        print(y, end="")
        break
    print()