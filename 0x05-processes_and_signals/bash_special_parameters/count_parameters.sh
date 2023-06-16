#!/usr/bin/env bash

# A script that illustrates how to use $# special parameter to count the
# number of command line arguments passed to a bash script.

# $# works like argc in C programming but is slightly different (it doesn't
# include the name of the script in the count)

if [ "$#" -eq "0" ]; then
    echo "Echo no arguments passed!"
    echo "Usage: $0 arg1 arg2"
    exit
fi

i="1"
for item in "$@";
do
    echo "\$"$i" = $item"
    i=$((i + 1))
done
