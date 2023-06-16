#!/usr/bin/env bash
# A bash script that runs a ruby script and passes each line of a log file
# `text_messages.log`, to the ruby script as a positional argument.

# The ruby script uses regular expression to match and print relevant parts
# of each of the lines.

while read -r line;
do
    ./100-textme.rb "$line" | cat -e;
    sleep 1s;

done < "text_messages.log"
