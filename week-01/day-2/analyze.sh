#!/bin/bash
echo " ERROR lines "
grep -n "ERROR" sample.log

echo ""
echo "Non-INFO lines"
grep -v "INFO"  sample.log > problems.txt
cat problems.txt 
echo ""
echo "Most frequent user"
awk 'NF >= 4 {print $4} ' sample.log | sort | uniq -c | sort -nr | head -1

