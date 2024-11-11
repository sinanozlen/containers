import calendar

print("Welcome to the Calendar application!")

# Yıl bilgisi alma
year = int(input("Please enter any year"))

# Ay bilgisi alma
month = int(input("Please enter a month (1-12): "))


print(calendar.month(year, month))

print("Have a nice day!")

#bu klasörü aşağıdaki komut satırıyla ayağa kaldırın ve deneyin
# docker run -it -v ${PWD}:/app -w /app python python3 calendar-app.py