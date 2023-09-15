#user input of days
days = int(input("Enter days: "))
# conversion of days to years and weeks
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7       

print(f'YEARS: {years}')
print(f'WEEKS: {weeks}')
print(f'DAYS: {remaining_days}')