# Rounded, based on NBN data (TBps). The ultimate goal would have been to get the raw data, but alas..
# https://www.nbnco.com.au/content/dam/nbn/images/blog/the-impacts-of-covid-19-response-measures-on-australian-broadband-traffic-on-the-nbn-network.pdf
# We just want the curve for this, and then fit our server TB usage to it.
from math import floor
usage_per_hour = [6,4,3,2,2,2,2,4,4,4,4.5,4.5,5,6,6,6,7.5,8,8,9,10,11,10,8]
usage_sum = 0

# megabits
server_usage_per_hour_Mb = {"00:00": 0,"01:00": 0,"02:00": 0,"03:00": 0, "04:00": 0,"05:00": 0, "06:00": 0,
                            "07:00": 0,"08:00": 0,"09:00": 0,"10:00": 0,"11:00": 0,"12:00": 0,"13:00": 0,
                            "14:00": 0,"15:00": 0,"16:00": 0,"17:00": 0,"18:00": 0,"19:00": 0,"20:00": 0,
                            "21:00": 0,"22:00": 0,"23:00": 0}
server_usage_sum_Mb = 2666400 #333.3GB per server

for hour in usage_per_hour:
  usage_sum += hour

for i, time in enumerate(server_usage_per_hour_Mb):
  coefficient = usage_per_hour[i]/usage_sum
  server_usage_per_hour_Mb[time] = floor(coefficient * server_usage_sum_Mb)

# Format output
for time in server_usage_per_hour_Mb.keys():
  data = "{0},{1}".format(time,server_usage_per_hour_Mb[time]);
  print(data)