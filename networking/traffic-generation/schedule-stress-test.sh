# Scheduled stress test
# Author: Jean Yap
#!/bin/sh
#atd must be enabled in order for this to work
# Schedule a 24hr network test

iperf_server_ip="127.0.0.1"

schedule=$(python3 ./usage-per-hour.py)
function scheduleTraffic ()
{
  hour=$1
  Mbps=$2
  # A (slightly less than) hour-long transmission, to give the link some breathing space
  echo "iperf3 -c $iperf_server_ip -u -t 3530 -b ${Mbps}M" | at $hour 
  return 0;
}

if [ "$schedule" ]; then
  while IFS="," read -r hour Mbps # For every line in schedule, get the calculated schedule hour and transmission speed
  do
    echo "Server is scheduled to send traffic for an hour at $Mbps Mbps, at:"
    scheduleTraffic $hour $Mbps
  done <<< "$schedule"
fi