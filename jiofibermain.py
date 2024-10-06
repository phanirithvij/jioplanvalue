from datetime import datetime, timedelta

tot = 3300

used = sum(
    [
        5.12,  # in call she told 3294.88 left and 6th 0000 expiry
    ]
)


current_date = datetime.now()
current_month = current_date.month

sixth_of_current_month = datetime(current_date.year, current_month, 6)
if current_date.day < 6:
    sixth_of_current_month = datetime(
        sixth_of_current_month.year,
        sixth_of_current_month.month - 1,
        sixth_of_current_month.day,
    )

if current_month == 12:
    next_month = 1
    next_year = current_date.year + 1
else:
    next_month = current_month + 1
    next_year = current_date.year

sixth_of_next_month = datetime(next_year, next_month, 6)
if current_date.day < 6:
    sixth_of_next_month = datetime(next_year, next_month - 1, 6)

remaining_days_to_sixth = (sixth_of_next_month - current_date).days
if remaining_days_to_sixth == 0:
    remaining_days_to_sixth = 1

days_passed = (current_date - sixth_of_current_month).days
if days_passed == 0:
    days_passed = 1

print("used:", used / days_passed, "GBpd", "in", days_passed, "days")
print(
    "rem:",
    (tot - used) / remaining_days_to_sixth,
    "GBpd",
    remaining_days_to_sixth,
    "days",
)
print(
    f"""
    {used}/{tot}
    rem: {tot - used}
    used {round(used/tot * 100)}% in {round(days_passed*100/(days_passed+remaining_days_to_sixth))}% of time
    """
)
