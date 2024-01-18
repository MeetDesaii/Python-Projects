def convert_seconds(seconds):
    hours = seconds // 3600  # Floor division returns value in integer. For ex. if result will be 2.5 then it will return 2.
    minutes = (seconds - (hours * 3600)) // 60
    remaining_seconds = (seconds - (hours * 3600) - (minutes * 60))
    return hours, minutes, remaining_seconds


# We know it returns two values so that's why we assigned it in three variables!
hours_left, minutes_left, seconds_left = convert_seconds(46000)

print(f"Hours left: {hours_left}\nMinutes left: {minutes_left}\nSeconds left: {seconds_left}")
