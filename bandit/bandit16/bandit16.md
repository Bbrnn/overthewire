# BANDIT 16

## LEVEL GOAL

The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

**Commands to use**
ssh, telnet, nc, openssl, s_client, nmap
![commands](image.png)

**Helpful reading material**\
   Port scanner on Wikipedia\
   <https://en.wikipedia.org/wiki/Port_scanner>

## SOLUTION

* Username -bandit16
* Hostname -bandit.labs.overthewire.org
* Port -2220
* Password -JQttfApK4SeyHwDlI9SXGR50qclOAil1

I will login using the credentials above\
    `ssh bandit16@bandit.labs.overthewire.org -p 2220`
Then I perform an nmap scan of the specified ports range\
![nmapscan](image-1.png)

Based on the scan ,I found that port 31790 standsout since it returns a message "enter correct credentials"\
From this ,i think this is the port that we are going to focus on
![nmapscan2](image-2.png)

Port 31790 service uses ssl encryption to mean we need to use openssl
![openssl](image-3.png)
![opensssl1](image-4.png)
After logging in using openssl,I submit bandit 16 password and get an RSA key as the password for bandit17\
This is different from bandit 15 wereby after loggin gin using openssl,you get bandit16 password after submititing the correct bandit 15 password\
![save_key](image-5.png)
