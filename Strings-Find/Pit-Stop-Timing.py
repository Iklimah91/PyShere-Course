# 🏁 Pit Stop Timing Optimizer 
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 
#   They are too slow!"

# Collect inputs
total_race_time = int(input("Enter the total time (in seconds): "))
pit_stops = int(input("Enter the number of pit stops made: "))
average_pit_stop_duration = float(input("Enter the average pit stop duration (in seconds): "))

# Calculate total pit time
total_pit_stop_time = pit_stops * average_pit_stop_duration

# Calculate pit time percentage
percentage_pit_time = ( total_pit_stop_time / total_race_time) * 100
percentage_pit_time = round(percentage_pit_time, 2)

# Print results
print(f"Total pit stop time: {total_pit_stop_time} seconds")
print(f"percentage of pit time: {percentage_pit_time}%")

# Optional Feedback on pit crew
if percentage_pit_time > 5:
    print("You need a new pit crew. They are too slow!")
else:
    print("Your pit crew is doing a great job!")

# End of Pit Stop Timing Optimizer
print("====Pit Stop Timing Optimizer====")
print("Thank you for using the Pit Stop Timing Optimizer!")
print("Safe racing!")
# End of Pit Stop Timing Optimizer