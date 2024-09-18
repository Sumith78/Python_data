# Prompt the user to enter hours and rate per hour
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))

# Calculate the weekly earning
weekly_earning = hours * rate_per_hour

# Print the weekly earning
print(f"Your weekly earning is {weekly_earning:.2f}")
