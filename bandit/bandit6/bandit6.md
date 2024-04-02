# BANDIT 6

## LEVEL GOAL

--The password for the next level is stored somewhere on the server and has all of the following properties:\

    -owned by user bandit7
    -owned by group bandit6
    -33 bytes in size

### Commands to use

ls , cd , cat , file , du , find , grep

#### SSH LOGIN DETAILS

->Username-bandit6

->Host-bandit.labs.overthewire.org

->Port-2220

->Password-
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

![login](<Screenshot from 2024-03-26 09-06-58.png>)

![alt text](<Screenshot from 2024-03-26 09-13-05.png>)

--I researched how to find a file based on the owner and the group.This is the command to use\
**find / -user username -group groupname -ls**

--Using this first command,there were to many errors so i added this command at the end ,2>/dev/null

--The *2>/dev/null* 2 is a file descriptor for stderr and > is redirection.

This command redirects the error messages to /dev/null to mean the errors won't be displayed in the output

--Finally ,I found the file that matches the properties stated

![File and the password](<Screenshot from 2024-03-26 09-20-05-1.png>)
--Level 7 password\
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
