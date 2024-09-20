# Constants
SECONDS_IN_A_YEAR = 60 * 60 * 24 * 365  # Approximate number of seconds in a year

# Prompt the user to enter the number of years they have lived
years_lived = float(input("Enter the number of years you have lived: "))

# Assume a person can live up to 100 years
max_years = 100

# Calculate the remaining years
remaining_years = max_years - years_lived

# Calculate the number of seconds a person can live
seconds_lived = remaining_years * SECONDS_IN_A_YEAR

# Print the result
print(f"Based on a lifespan of 100 years, you have approximately {seconds_lived:.0f} seconds left.")










# Constants
SECONDS_IN_A_YEAR = 60 * 60 * 24 * 365  # Approximate number of seconds in a year

# Prompt the user to enter the number of years they have lived
years_lived = float(input("Enter the number of years you have lived: "))

# Calculate the number of seconds a person has lived
seconds_lived = years_lived * SECONDS_IN_A_YEAR

# Print the result
print(f"You have lived for {seconds_lived:.0f} seconds.")
