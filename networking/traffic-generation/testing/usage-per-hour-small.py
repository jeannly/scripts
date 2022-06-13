# A version of usage-per-hour.py, for testing on a minute-by-minute basis (as opposed to hourly) for 
#   testing the script locally.
from math import floor
usage_per_hour = [6,4,3,2,2,2,2,4,4,4,4.5,4.5,5,6,6,6,7.5,8,8,9,10,11,10,8]
usage_sum = 0

# megabits
server_usage_per_hour_Mb = {"22:36": 0,"22:37": 0,"22:38": 0,"22:39": 0, "22:40": 0,"22:41": 0, "22:42": 0,
                            "22:43": 0,"22:44": 0,"22:45": 0,"22:46": 0,"22:47": 0,"22:48": 0,"22:49": 0,
                            "22:50": 0,"22:51": 0,"22:52": 0,"22:53": 0,"22:54": 0,"22:55": 0,"22:56": 0,
                            "22:57": 0,"22:58": 0,"22:59": 0}
server_usage_sum_Mb = 150

for hour in usage_per_hour:
  usage_sum += hour

for i, time in enumerate(server_usage_per_hour_Mb):
  coefficient = usage_per_hour[i]/usage_sum
  server_usage_per_hour_Mb[time] = floor(coefficient * server_usage_sum_Mb)

# Format output
for time in server_usage_per_hour_Mb.keys():
  data = "{0},{1}".format(time,server_usage_per_hour_Mb[time]);
  print(data)