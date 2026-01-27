#!/bin/bash

END_HOUR=18
END_MIN=0

NOW_HOUR=$(date +%H)
NOW_MIN=$(date +%M)

echo "Current time: $(date +%H:%M)"

NOW_TOTAL=$((10#$NOW_HOUR * 60 + 10#$NOW_MIN))
END_TOTAL=$((END_HOUR * 60 + END_MIN))

REMAIN=$((END_TOTAL - NOW_TOTAL))

if [ "$REMAIN" -le 0 ]; then
  echo "Work day is already finished."
  exit 0
fi

HOURS=$((REMAIN / 60))
MINS=$((REMAIN % 60))

echo "Work day ends after ${HOURS} hours and ${MINS} minutes."
