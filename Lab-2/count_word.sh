#!/bin/bash

FILE=$1
WORD=$2

if [ -z "$FILE" ] || [ -z "$WORD" ]; then
  echo "Usage: $0 <file> <word>"
  exit 1
fi

COUNT=$(grep -o -i "$WORD" "$FILE" | wc -l)

echo "The word \"$WORD\" appears $COUNT times."
