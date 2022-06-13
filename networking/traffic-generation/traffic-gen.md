## Traffic generation scheduler
Given a schedule of traffic usage trends (`usagePerHour.py`),
send out waves of fake IP-level traffic between servers using iperf.

For usage:
1. run an iperf server on the recipient using `iperf3 -s`
2. assign the server IP to the `iperf_server_ip` variable in `schedule-stress-test.sh`
3. run `schedule-stress-test.sh` on the client