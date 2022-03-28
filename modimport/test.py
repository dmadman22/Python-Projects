import pytz

for tz in sorted(pytz.all_timezones_set):
        print(tz)
print(pytz.country_timezones)