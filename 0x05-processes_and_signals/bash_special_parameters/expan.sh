#!/usr/bin/env bash

# NOTE: $* and $@ can both be use like argv in C programming. They are both
#       used to parse argumnts to bash scripts.
#
# This script demonstrates the difference between $* and $@


# -----------------> 1. Printing data available in $* <-------------------
export IFS='-'
count=1
echo 'Values of $*:'

for arg in "$*";  # if you remove the double quotes $* will output the same
	          # result as $@
do
    echo "Arg #$count = $arg"
    let "count += 1"
done

# ------------------------------------------------------------------------
echo

echo $1
echo $2
echo $3

echo
# ------------------------------------------------------------------------

# ----------------> 2. Printing data available in $@ <--------------------
count=1
echo 'Values of $@'

for arg in "$@";
do
    echo "Arg #$count = $arg"
    let "count += 1"
done

# ------------------------------------------------------------------------


# NOTES: When printing the each value of special parameter "$*", it gives
#        only one value which is the whole positional parameter delimited by
#        IFS. Whereas, "$@" gives you each parameter as a seperate word.

