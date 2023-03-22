#!/usr/bin/env bash

FILE_TO_TRANSFORM=${1}

TOP_10_QB_PASS_YARDS="../data/top_10_qb_yards.csv"

#Check if the file exists
if ! [ -e "${FILE_TO_TRANSFORM}" ]
then
  echo "${FILE_TO_TRANSFORM} does not exist"
  exit 1
fi

(csvgrep -c 23 -m "QB" ${FILE_TO_TRANSFORM} | csvcut -c 2,3,23,16,17,18,19,20,21,22 | csvsort -r -c 5 | head) > ${TOP_10_QB_PASS_YARDS}