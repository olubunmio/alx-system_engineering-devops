#!/usr/bin/env bash

# A script that prints the process id of the shell and of the last executed
# background process.
#
# $$ - PID of shell
# $! - PID of last executed background process

echo -e "Process ID = $$ (current script)"

sleep 20 &  # quickly run ps before 20 seconds runs out
echo -e "Background Process ID = $!"
