#!/usr/bin/env bash

FILE_TO_CHECK=${1}

#Check if the file exists
if ! [ -e "${FILE_TO_CHECK}" ]
then
  echo "${FILE_TO_CHECK} does not exist"
  exit 1
fi

echo "-----RUNNING CHECKS ON ${FILE_TO_CHECK}"

echo "-----CHECK 1: DUPLICATE VALUE CHECK"
FILE_LENGTH=$(wc -l ${FILE_TO_CHECK} | awk '{print $1;}')
# Factor for CR error in file
FILE_LENGTH=$((FILE_LENGTH+1))

NUM_UNIQUE_LINES=$(sort ${FILE_TO_CHECK} | uniq | wc -l)
NUM_DUPLICATES=$((FILE_LENGTH-NUM_UNIQUE_LINES))
echo "${NUM_DUPLICATES} duplicates found in file ${FILE_TO_CHECK}"

