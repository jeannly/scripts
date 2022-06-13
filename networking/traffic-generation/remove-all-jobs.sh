#!bin/sh
# Remove all atjobs
for i in `atq | awk '{print $1}'`;do atrm $i;done