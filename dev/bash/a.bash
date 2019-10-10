#!/bin/bash

cnt=1

while read  LINE; do
    echo ${cnt}: ${LINE}
    ((cnt++))
done < file.txt
