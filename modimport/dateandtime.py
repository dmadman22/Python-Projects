# import time
#
# print("The epoch of this system starts at", time.strftime("%c", time.gmtime(0)))
#
# print("The current time zone it {0} with an offset of {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\tDaylight savings time is in effect for this location")
#     print("\tThe DST timezone is " + time.tzname[1])
#
# print("Local time is \t" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC time is \t" + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())