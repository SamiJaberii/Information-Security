#!/bin/bash

DIR=$1

if [ -z "$DIR" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

if [ ! -d "$DIR" ]; then
  echo "Error: Directory does not exist."
  exit 1
fi

find "$DIR" -type f -empty | while read FILE; do
  rm "$FILE"
  echo "Deleted: $FILE"
done
