#here, i am prompting a user to enter their age and i'll calculate how long they still have on earth provided they were to live for 90years

user_age = int(input('Enter your age: '))

#these are the days, weeks, and months the user is expected to live

standard_days = 365 * 90
standard_weeks = 52 * 90
standard_months = 12 * 90

#provided the user does'nt live up to 90 years, we want to check their days lived on earth

user_days = 365 * user_age
user_weeks = 52 * user_age
user_months = 12 * user_age

#now, i want to check the lifespan left from 90years.

days_left = standard_days - user_days
weeks_left = standard_weeks - user_weeks
months_left = standard_months - user_months

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left on earth")