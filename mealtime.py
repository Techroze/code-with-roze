def main():
# receive Input for time

    meal_time = input("What time is it? ")

# convert function for time

    time = convert(meal_time)

# breakfast,lunch and dinner time

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")
    else:
        print("It's not time to eat")

def convert(time):

# get hour and minutes

    hours, minutes = time.split(":")

# convert time into float

    new_minute = float(minutes) / 60

# Return the result to main function

    return float(hours) + new_minute

if __name__ == "__main__":
    main()
