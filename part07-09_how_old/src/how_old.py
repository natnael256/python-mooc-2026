# Write your solution here
from datetime import datetime, timedelta

day = input("Day:")
month = input("Month:")
year = input("Year:")


age = datetime(int(year),int(month),int(day))

new_millennium = datetime(1999,12,31)


how_old  = new_millennium - age

# print (how_old.days)
if age < new_millennium:
    
    print(f"You were {how_old.days} days old on the eve of the new millennium.")  
else:
    print(f"You weren't born yet on the eve of the new millennium.")