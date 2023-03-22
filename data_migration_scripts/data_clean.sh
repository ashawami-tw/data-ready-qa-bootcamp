#!/usr/bin/env bash

FILE_TO_CLEAN=${1}
NO_DUP_FILE=${1}_nodup.csv

#Check if the file exists
if ! [ -e "${FILE_TO_CLEAN}" ]
then
  echo "${FILE_TO_CLEAN} does not exist"
  exit 1
fi

echo "-----CLEANING FILE ${FILE_TO_CLEAN}"

echo "-----CLEANING ACTION 1: REMOVING DUPLICATES"
FILE_LENGTH_START=$(wc -l ${FILE_TO_CLEAN} | awk '{print $1;}')

(head -n 1 ${FILE_TO_CLEAN}  && tail -n +2 ${FILE_TO_CLEAN} | sort -u) > ${NO_DUP_FILE}

FILE_LENGTH_END=$(wc -l ${NO_DUP_FILE} | awk '{print $1;}')

echo "$((FILE_LENGTH_START-FILE_LENGTH_END+1)) DUPLICATES REMOVED"

echo "-----VALIDITY CHECK 1: REMOVING ROWS WHERE PLAYERS HAVE NO TEAM"

(python3 remove_players_with_no_team.py ${NO_DUP_FILE})

