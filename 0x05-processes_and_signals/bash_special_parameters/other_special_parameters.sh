#!/usr/bin/env bash

# $?  -> gives the exit status of the most recent executed command
# $-  -> prints the options currently set using the set builtin command.
# $_  -> gives the argiment to the previous command. At the shell startup,
#        it gives the absolute filename of the shell script beight executed.


echo -e "$_";  # Absolute name of the file which is being executed

echo
/usr/local/bin/dbhome  # execution of this command fails
# check the exit status
if [ "$?" -ne "0" ]; then
    echo "Sorry, command execution failed!"
fi


echo -e "$-"; # Set options -hB

echo -e "$_"; # Last argument of the previous command
