#!/bin/sh
# A version of the stress test, for testing locally on a simple machine

iperf_server_ip="192.168.0.140"

schedule=$(python3 ./usage-per-hour-small.py)
function scheduleTraffic ()
{
  hour=$1
  Mbps=$2
  # 5s transmission time, instead of 1hr, for testing
  echo "iperf3 -c $iperf_server_ip -u -t 5 -b ${Mbps}M" | at $hour 
  return 0;
}

if [ "$schedule" ]; then
  while IFS="," read -r hour Mbps # For every line in schedule, get the calculated schedule hour and transmission speed
  do
    echo "Server is scheduled to send traffic for an hour at $Mbps Mbps, at:"
    scheduleTraffic $hour $Mbps
  done <<< "$schedule"
fi