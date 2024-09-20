from datetime import datetime, timedelta

tot = 3333

used = sum(
    [
        621.78,
        0.2042,
        183.88,
        45.78,
        6.02,
        267.43,
        33.3,
        293.03,
        1.36,
        90.37,
        10.87,
        0.316,
        20.28,
        0.522,
        98.37,
    ]
)


current_date = datetime.now()
current_month = current_date.month

sixth_of_current_month = datetime(current_date.year, current_month, 6)

if current_month == 12:
    next_month = 1
    next_year = current_date.year + 1
else:
    next_month = current_month + 1
    next_year = current_date.year

fifth_of_next_month = datetime(next_year, next_month, 5)

remaining_days_to_fifth = (fifth_of_next_month - current_date).days

days_passed = (current_date - sixth_of_current_month).days

print("used:", used / days_passed, "GBpd", "in", days_passed, "days")
print(
    "rem:",
    (tot - used) / remaining_days_to_fifth,
    "GBpd",
    remaining_days_to_fifth,
    "days",
)
print(
    f"""
    {used}/{tot}
    rem: {tot - used}
    used {round(used/tot * 100)}% in {round(days_passed*100/(days_passed+remaining_days_to_fifth))}% of time
    """
)
