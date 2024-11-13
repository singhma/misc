from datetime import datetime, timedelta

start_date = datetime(2024, 11, 26)
end_date = datetime(2025, 1, 27)

# Initialize a counter for Wednesdays
wednesday_count = 0

# Initialize a counter for weeks
week_count = 0

fees_savings = 0
petrol_savings=0
holiday_savings=0
rail_tickets_savings=0
kharcha_pani_savings=0
savings_month= False

# Iterate through the dates and count Wednesdays on a fortnightly basis
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() == 2 and week_count % 2 == 0:  # Wednesday is 2 in the weekday() function
        wednesday_count += 1
        if current_date.month ==12 or current_date.month ==1 :    
            savings_month = True
            fees_savings +=830+350
            petrol_savings+=40*2
            #holiday_savings +=200
            rail_tickets_savings+=40*2
            kharcha_pani_savings +=150*2        
    current_date += timedelta(days=1)
    if current_date.weekday() == 0:  # If it's Monday, increment week count
        week_count += 1
    

start_date=start_date.strftime("%b %d, %Y")
end_date=end_date.strftime("%b %d, %Y")

print(f"Number of Wednesdays between ( {start_date} and {end_date} ) on a fortnightly basis:", wednesday_count)
print(f"Fees that can be saved in {wednesday_count} weeks is {fees_savings +830}")
if(savings_month):
    print(f"Miscellaneous Savings Between December and January is {petrol_savings+rail_tickets_savings+kharcha_pani_savings}")
    print(f"\t Petrol Savings : {petrol_savings}")
    print(f"\t Railways Tickets Savings : {rail_tickets_savings}")
    print(f"\t Kharcha Pani Savings : {kharcha_pani_savings}")
